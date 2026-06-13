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
    mensaje = None

    #verificamos si el usuario envio el formulario
    if request.method == "POST":

        #Obtener datos, desde el formulario
        #negocio = request.form.get("negocio")

        #Hacer uso de diccionario
        form_data = {
                "negocio": request.form.get("negocio"),
                "nombre": request.form.get("nombre"),
                "telefono": request.form.get("telefono"),
                "email": request.form.get
                ("email")
                }
        
        
        #Enviar dato a form_service
        process_data(form_data)
        #Mostrar mensaje lluego de enviar elformulario
        mensaje = f"Gracias {form_data['nombre']}, recibí tus respuestas, en breve me comunicaré contigo."

        return render_template ("thanks.html", mensaje=mensaje)

        
    return render_template ("home.html")



