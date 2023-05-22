# TXT-translator
App basada en Flask para traducir texto. Proporciona las siguientes funcionalidades:

- Subir y traducir archivos de texto.
- Ingresar texto manualmente para su traducción.
- Mostrar el texto traducido en formato HTML.
- Ajustar el tamaño de fuente del texto traducido.

## Instalación

1. Clona el repositorio:

   ```
   git clone https://github.com/arefome/TXT-translator.git
   ```

2. Navega hasta el directorio del proyecto:

   ```
   cd TXT-translator
   ```

3. Crea un entorno virtual:

   ```
   python -m venv venv
   ```

4. Activa el entorno virtual:

   - Para Windows:

     ```
     venv\Scripts\activate
     ```

   - Para macOS/Linux:

     ```
     source venv/bin/activate
     ```

5. Instala las dependencias necesarias:

   ```
   pip install -r requirements.txt
   ```

6. Inicia el servidor de desarrollo de Flask:

   ```
   flask run
   ```

7. Abre tu navegador web y visita [http://localhost:5000](http://localhost:5000).

## Uso

1. Sube un archivo de texto o ingresa texto manualmente en el formulario provisto.
2. Haz clic en el botón "Traducir" para traducir el texto.
3. Ajusta el tamaño de fuente utilizando los botones "+" y "-".
4. El texto traducido se mostrará en formato HTML.


### Ejecutar en Google Colab

Haz clic en el siguiente enlace para traducir un TXT desde Google Colab:

[![Ejecutar en Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arefome/TXT-translator/blob/master/notebooks/TXT_translator.ipynb)
