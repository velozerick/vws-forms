#Importar Flask
from flask import Flask

#funcion encargada de crear la aplicacion
def create_app():

    #creamos aplicacion flask
    app = Flask(__name__)

    #Importamos el grupo de rutas principales
    from app.routes.main_routes import main

    #Registramos esas rutas dentro de flask
    app.register_blueprint(main)

    return app
