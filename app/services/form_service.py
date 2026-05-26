#FORM_SERVICE

#Esta funcion recibe datos de formulario
#se encrga de procesarlo

def process_data(form_data):

    #Abrir archivo modo append
    # "a" agregar sin borrar contenido
    with open("data.txt", "a") as file:
        #Escribir datos en el archivo
        file.write(f'negocio:{form_data["negocio"]}\n')
        file.write(f"nombre: {form_data["nombre"]}\n")
        file.write(f"telefono: {form_data["telefono"]}\n")
        file.write(f'email:{form_data["email"]}\n')

        file.write("-------------\n")



    #print(form_data)


