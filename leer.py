from pymongo import MongoClient

# Crear las conexiones para establecer el enlace con mongo
cliente = MongoClient('localhost:27017')
db = cliente.TiendaInformatica

def consultar():
    try:
        #consultar toda la tabla d ela base de datos 
        ordenadores = db.ordenador.find()
        print("presentamos los datos obtenidos de la base de datos")

        for ordenador in ordenadores:
            print(ordenador)

    except ImportError:
        platform_specific_module = None
        print(str(e))
