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
from flask import Flask, render_template # le dice a flaks renderiza un archivo html

#Create app
app = Flask(__name__)




#Define route for home app
@app.route("/") # the main page

#function executed when user enters "/"
def home():
    #response returned to browser
    #return "<h1> Hello there Flask, nice to meet you </h1>"
    return render_template("home.html")



#route for about 
@app.route("/about")

#function executed when user enters "about.html"
def about():
    return render_template("about.html")



#route for services
@app.route("/services")

#function when user enters "services.html"
def services():
    return render_template("services.html")







#verify if file is executed directly
if __name__ == "__main__":

    #run Flask server in debug mode
    app.run(debug=True) #developer mode

