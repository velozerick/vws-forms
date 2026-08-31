#Este modulo se encarga de recibir peticiones HTTP relacionadas con las paginas principales de la aplicacion
#Aqui definimos que debe hacer flask cuando un usuario visitle la ruta principal /

#Creamos un bluieprint para agrupar las rutas principales , nos permite agrupar rutas relacionasdas en un moduilo separado y despues conectar ese grupo con la app 
from flask import Blueprint

main = Blueprint("main", __name__)



#RUTA PRINCIPAL
#cuando el navegador solicite "/" Flask ejecuara esta funcion
@main.route("/")
def home():
    return "Hola, somos VWS"



#ruta que mostrara el formulario
@main.route("/formulario")
def formulario():
    return "aqui estara el formulario"


#ruta que mostrara el agradecimiento
@main.route("/agradecimiento")
def agradecimiento():
    return "Aqui estará el mensaje de agradecimiento"

    