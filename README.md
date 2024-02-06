# Procesador de Imágenes

Este es un proyecto que permite procesar imágenes en un directorio seleccionado, reduciendo su tamaño y cambiando su formato si es necesario.

## Funcionalidades

- Selección de directorio para procesar imágenes.
- Configuración de calidad y tamaño máximo de las imágenes procesadas.
- Selección del formato de salida (JPEG o WEBP).
- Procesamiento de las imágenes encontradas en el directorio seleccionado.
- Generación de un registro de procesamiento en un archivo de registro.

## Instalación

1. Clona este repositorio: `git clone https://github.com/celvintr/procesador-imagenes.git`
2. Navega hasta el directorio del proyecto: `cd procesador-imagenes`
3. Instala las dependencias: `pip install -r requirements.txt`
4. Ejecuta la aplicación: `python main.py`

## Uso

1. Ejecuta la aplicación y selecciona un directorio con imágenes.
2. Configura la calidad, tamaño máximo y formato de salida.
3. Haz clic en "Procesar Directorio" para iniciar el procesamiento.
4. El resultado se mostrará en la interfaz y se guardará un archivo de registro en el directorio de origen.

## Requisitos

- Python 3
- Biblioteca PIL (Python Imaging Library)
- Tkinter (instalado por defecto en la mayoría de las distribuciones de Python)

## Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios: `git checkout -b feature/nueva-funcionalidad`
3. Realiza tus cambios y haz commit: `git commit -am 'Agrega nueva funcionalidad'`
4. Haz push a la rama: `git push origin feature/nueva-funcionalidad`
5. Envía un pull request desde tu rama a la rama `master` del repositorio original.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
