#Importamos blueprint para crear grupo de rutas y render para mostrar archivos html
from flask import Blueprint, render_template,request #request es la peticion que llega

#Creamos el grupo de rutas principal
main = Blueprint("main", __name__)


#Ruta principal del sitio
@main.route("/",methods=["GET","POST"]) #Esta ruta acepta GET y POST

def home():
    #Mostramos el html

    #verificamos si el usuario envio el formulario
    if request.method == "POST":

        #Obtener dato, desde el formulario
        negocio = request.form.get("negocio")
        
        #Mostrar dato en temrinal
        print(f"Negocio: {negocio}")
    return render_template ("home.html")



