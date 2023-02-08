from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.TiendaInformatica

# crear una funcion que permita actualizar los valores de una coleccion
def update():
    try:
        criteria = input("Ingrese el id del registro a actualizar\n")
        db.client.delete_many(
            {'id': float(criteria)}  
        )
        print("Registro", criteria, " Eliminado correctamente")
    except  ImportError:
        platform_specific_module = None
        print(str(e))
        

