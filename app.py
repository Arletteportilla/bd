#crear la clase que permita llamar a todos lo metodos que se van a relacional con MongoDB
import insertar
import leer
import actualizar
import borrar
class Programa:
    def __init__(self):
        self.dato = 1
    
    def menu(self):
        while self.dato:
            seleccion = input("""
                        seleccione: 
                        1. Insertar
                        2. Actualizar
                        3.Leer
                        4.Borrar
                        """)
            if seleccion =="1":
                #llamar la seleccion insertar
                #print("Insertar")
                insertar.insertar()
            elif seleccion =="2":
                #Llamar a la opcion actualizar 
                #print("Actualizar")
                actualizar.update()
            elif seleccion == "3":
                #print("Leer")
                leer.consultar()
            elif seleccion == "4":
                #print("Borrar")
                borrar.delete()
            else:
                print("Error")            
mongo = Programa()
mongo.menu()