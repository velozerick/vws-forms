#Importamos clase flask desde el paquete flask
#Este paquete nos permite crear nuestra aplicacion web

from flask import Flask

#Esta funcion sera responsable de crear y configurar

def create_app():

    #creamos una instancia de flask 
    app = Flask(__name__)


    #Importamos el grupo de rutas principales
    from app.routes.main import main

    #registramos esas rutas dentro de la app de flask
    app.register_blueprint(main)


    #devolvemos la aplicacion ya creada
    return app

    