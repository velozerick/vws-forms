#Importamos blueprint para crear grupo de rutas y render para mostrar archivos html
from flask import Blueprint, render_template

#Creamos el grupo de rutas principal
main = Blueprint("main", __name__)


#Ruta principal del sitio
@main.route("/")

def home():
    #Mostramos el html
    return render_template ("home.html")


