from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.TiendaInformatica

# crear una funcion que permita actualizar los valores de una coleccion
def update():
    try:
        criteria = input("Ingrese el id del registro a actualizar\n")

        #Ingresar los datos de la coleccion a actualizar
        cedula_ruc = input("Ingrese la cedula correcta: ")
        nombres = input("Ingrese los nombres correctos: ")
        apellidos = input("Ingrese los apellidos correctos: ")

        #Vamos a utilizar la coleccion correcta para almacenar la data
        db.cliente.update_one(
        {"id": criteria},
        {
            "$set":{"cedula_ruc": cedula_ruc,
             "nombres": nombres,
             "apellidos" : apellidos
            }
        }
     )
        print("""!!!!!!!!!!!!!!!!!!!!!!!!!!!!
          Registro actualizado correctamente
          ???????????????????????????????????
        """ )  
    except ImportError:
        platform_specific_module = None
        print(str(e))
        print("No se localizo el registro ingresado en el criterio de busqueda")