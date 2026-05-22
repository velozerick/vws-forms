#Importamos blueprint para crear grupo de rutas y render para mostrar archivos html
from flask import Blueprint, render_template,request #request es la peticion que llega

#Importamos form_services
from app.services.form_service import process_data


#Creamos el grupo de rutas principal
main = Blueprint("main", __name__)


#Ruta principal del sitio
@main.route("/",methods=["GET","POST"]) #Esta ruta acepta GET y POST

def home():
    #Mostramos el html

    #verificamos si el usuario envio el formulario
    if request.method == "POST":

        #Obtener datos, desde el formulario
        #negocio = request.form.get("negocio")

        #Hacer uso de diccionario
        form_data = {
                "Negocio": request.form.get("negocio"),
                "Nombre": request.form.get("nombre"),
                "Telefono": request.form.get("telefono")
                }
        
        #Enviar dato a form_service
        process_data(form_data)

    return render_template ("home.html")



