# Importa las bibliotecas necesarias: Flask para la aplicación web y render_template para generar respuestas HTML.
from flask import Flask, render_template
# Crea una instancia de la aplicación Flask. '__name__' es el nombre del módulo actual.
app = Flask(__name__)

# Define una ruta que recibe un parámetro 'name' a través de la URL
@app.route('/greet/<name>')
# Esta función recibe el parámetro 'name' y lo pasa al render_template para generar la respuesta.
def greet(name):
    return render_template('greet.html', name=name)  # render_template genera una respuesta HTML usando el archivo 'greet.html' y pasa el parámetro 'name' a la plantilla.

if __name__ == '__main__':  # Este bloque asegura que el servidor se ejecute solo cuando el archivo se ejecuta directamente, no cuando es importado como módulo.
    app.run(port=8080)  # Inicia la aplicación Flask. en el puerto http://127.0.0.1:8080.
