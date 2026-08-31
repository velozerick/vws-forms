#Este modulo se encarga de recibir peticiones HTTP relacionadas con las paginas principales de la aplicacion
#Aqui definimos que debe hacer flask cuando un usuario visitle la ruta principal /

#Creamos un bluieprint para agrupar las rutas principales , nos permite agrupar rutas relacionasdas en un moduilo separado y despues conectar ese grupo con la app 
from flask import Blueprint, render_template, request
#render template es para trabajar con plantillas html

main = Blueprint("main", __name__)



#RUTA PRINCIPAL
#cuando el navegador solicite "/" Flask ejecuara esta funcion
@main.route("/")
def home():
    #return "Hola, somos VWS"
    return render_template ("home.html")


"""
#ruta que mostrara el formulario
@main.route("/formulario")
def formulario():
    return render_template ("formulario.html")



#ruta que mostrara el formulario
@main.route("/formulario", methods=["GET","POST"])
def formulario():
    return render_template ("formulario.html")
"""


#ruta que mostrara el formulario
@main.route("/formulario", methods=["GET","POST"])
def formulario():

    if request.method == "POST":
        negocio = request.form.get("negocio")
        nombre = request.form.get("nombre")
        telefono = request.form.get("telefono")
        email = request.form.get("email")
        print(f"""
        Negocio: {negocio}
        Nombre: {nombre}
        Telefono: {telefono}
        Email: {email}""")
        


    return render_template ("formulario.html")



#ruta que mostrara el agradecimiento
@main.route("/agradecimiento")
def agradecimiento():
    return render_template("agradecimiento.html")


