# Importamos create_app desde la carpeta app
#create_app sera una funcion que construye la aplicacion flask 
from app import create_app

#Ejecutamos create_app()
app = create_app()

#Esto verifica si run.py se ejecuto directamente 
if __name__ == "__main__":

    #levanta el servidor flask en modo desarrollo
    app.run(
        debug = True,
        host="0.0.0.0"
        )

