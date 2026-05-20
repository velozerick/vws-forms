"""
flask necesita:

-importar flask
-crear aplicacion
-Escuchar URL
-Ejecutar logica
-Devolver respuesta
-Levantar servidor

"""

#import
#from flask import Flask
from flask import Flask, render_template, request # le dice a flaks renderiza un archivo html,importamos request

#request representa la peticion que llego desde el navegador

#Create app
app = Flask(__name__)




#Define route for home app
@app.route("/", methods=["GET","POST"]) # the main page
#function executed when user enters "/"
#la ruta acepta GET y POST

def home():
    #response returned to browser
    #return "<h1> Hello there Flask, nice to meet you </h1>"

    #verify if request recived POST, when user submmits form
   if request.method == "POST":
        #Backend logic will go here
        
        #get value from input named "nombre"
        negocio = request.form["negocio"]
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        print(f"""
        Negocio: {negocio} 
        Nombre: {nombre}
        Telefono: {telefono}
                """)
   return render_template("home.html")







#verify if file is executed directly
if __name__ == "__main__":

    #run Flask server in debug mode
    app.run(debug=True) #developer mode

