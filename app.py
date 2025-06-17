import os
import threading
import webbrowser
from flask import Flask, redirect
from dotenv import load_dotenv
from blueprint.index import index_bp

# Cargar variables de entorno
load_dotenv()

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Creación de la aplicación Flask
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = os.getenv('FLASK_SECRET_KEY') or 'dev-key-solo-para-desarrollo' 
app.register_blueprint(index_bp)

@app.route('/')
def index():
    return redirect('/inicio/')

def abrir_navegador():
    # Esperar un poco para asegurar que el servidor esté listo
    webbrowser.open_new("http://localhost:3000/inicio/")

if __name__ == '__main__':  
    # Solo abrir el navegador durante el desarrollo inicial
    if os.environ.get("FLASK_ENV") != "production" and not os.environ.get("WERKZEUG_RUN_MAIN"):
        threading.Timer(1.25, abrir_navegador).start()
    
    # Configuración del servidor
    app.run(
        host='0.0.0.0', 
        port=3000, 
        debug=os.environ.get("FLASK_ENV") == "development",
        threaded=True
    )