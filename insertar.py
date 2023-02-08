from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.TiendaInformatica

# crear la funcion para guardar los ojetos creados


def insertar():
    try:
        modelo = input("ingrese el modelo: ")
        marca = input("Ingrese la marca: ")
        precio = input("Ingrese el precio: ")
        anio = float(input("ingrese el año de fabricacion: "))

        db.ordenador.insert_one({
            "modelo": modelo,
            "marca": marca,
            "precio": precio,
            "anio": anio,
        })
        print("objeto guardado satisfactoriamente")
    except ImportError:
        print("Error de conexion con la base de datos")
        print("Error con la conexion en la base de datos")
    


