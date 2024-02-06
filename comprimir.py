from PIL import Image, ExifTags
import os
import tkinter as tk
from tkinter import filedialog, ttk
import shutil

# Definir variables globales para los entry widgets y el combobox
entry_calidad = None
entry_dimension = None
combobox_formato = None
label_resultado = None

def reducir_tamano_imagen(input_path, output_path, calidad=100, max_dimension=1200, formato='WEBP'):
    try:
        with Image.open(input_path) as img:
            # Verificar si se pueden obtener los metadatos EXIF y la orientación de la imagen
            exif = img._getexif()
            if exif:
                orientation_tag = next((tag for tag, value in exif.items() if tag in ExifTags.TAGS and ExifTags.TAGS[tag] == 'Orientation'), None)
                if orientation_tag is not None:
                    orientation = exif[orientation_tag]

                    # Rotar la imagen según la orientación
                    if orientation == 3:
                        img = img.rotate(180, expand=True)
                    elif orientation == 6:
                        img = img.rotate(270, expand=True)
                    elif orientation == 8:
                        img = img.rotate(90, expand=True)

            # Redimensionar la imagen sin perder calidad
            img.thumbnail((max_dimension, max_dimension), Image.ANTIALIAS)
            
            # Guardar la imagen en el formato seleccionado con calidad ajustada
            img.save(output_path, formato, quality=calidad)
        
        print(f'Imagen convertida y guardada en: {output_path}')

    except Exception as e:
        print(f'Error al procesar la imagen: {e}')

def procesar_imagenes_en_directorio(directorio, calidad_deseada=100, max_dimension=1200, formato='WEBP'):
    total_carpetas_afectadas = 0
    log_path = os.path.join(directorio, 'procesamiento_log.txt')
    
    with open(log_path, 'w') as log_file:
        for root, dirs, files in os.walk(directorio):
            for archivo in files:
                if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                    ruta_input = os.path.join(root, archivo)
                    
                    # Crear una estructura de carpetas similar en el directorio de salida
                    ruta_relativa = os.path.relpath(root, directorio)
                    ruta_output = os.path.join('imagenes_procesadas', ruta_relativa, f'optimizado_{archivo}.{formato.lower()}')
                    ruta_output_absoluta = os.path.join(directorio, ruta_output)

                    # Crear los directorios necesarios en caso de no existir
                    os.makedirs(os.path.dirname(ruta_output_absoluta), exist_ok=True)

                    # Llamar a la función para reducir el tamaño de la imagen
                    reducir_tamano_imagen(ruta_input, ruta_output_absoluta, calidad_deseada, max_dimension, formato)
                    total_carpetas_afectadas += 1
                    log_file.write(f'Imagen procesada: {ruta_input} -> {ruta_output_absoluta}\n')
    
    return total_carpetas_afectadas, log_path

def procesar_directorio():
    directorio_seleccionado = filedialog.askdirectory()
    if directorio_seleccionado:
        calidad = int(entry_calidad.get())
        dimension = int(entry_dimension.get())
        formato = combobox_formato.get()
        total_carpetas_afectadas, log_path = procesar_imagenes_en_directorio(directorio_seleccionado, calidad, dimension, formato)
        label_resultado.config(text=f'Total de carpetas afectadas: {total_carpetas_afectadas}. Puedes revisar el log en: {log_path}')

def mostrar_interfaz_grafica():
    global label_resultado
    
    root = tk.Tk()
    root.title("Procesador de Imágenes")
    
    label_instrucciones = tk.Label(root, text="Seleccione un directorio para procesar las imágenes:")
    label_instrucciones.pack()

    boton_seleccionar_directorio = tk.Button(root, text="Seleccionar Directorio", command=procesar_directorio)
    boton_seleccionar_directorio.pack()

    label_calidad = tk.Label(root, text="Porcentaje de Calidad:")
    label_calidad.pack()
    global entry_calidad
    entry_calidad = tk.Entry(root)
    entry_calidad.pack()

    label_dimension = tk.Label(root, text="Tamaño Máximo (px):")
    label_dimension.pack()
    global entry_dimension
    entry_dimension = tk.Entry(root)
    entry_dimension.pack()

    label_formato = tk.Label(root, text="Formato de Salida:")
    label_formato.pack()
    global combobox_formato
    combobox_formato = ttk.Combobox(root, values=["JPEG", "WEBP"], state="readonly")
    combobox_formato.current(1)  # Seleccionar WEBP por defecto
    combobox_formato.pack()

    label_resultado = tk.Label(root, text="")
    label_resultado.pack()

    root.mainloop()

# Llama a la función para mostrar la interfaz gráfica
mostrar_interfaz_grafica()
