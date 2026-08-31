#Run es el punto de entrada de nuestra aplicacion , su responsabilidad es obtener la aplicacion flask y arrancarla 

#importamos desde nuestro paquete app la funcion que crea la aplicacion
from app import create_app

#Ejecutamos create_app() y guiardamos lo que devuleve app
app = create_app()


#
if __name__ == "__main__":
    app.run(debug=True)

#debug true activa herramientas de depuracion durante el desarollo y al momento de publicarlo se coloca app.run(debug=False)