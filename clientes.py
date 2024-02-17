
#Módulo de clientes
import sqlite3

"""Módulo de Clientes (clase BaseDatosClientes): Permite gestionar la información de los clientes registrados. 
Incluye: clave, nombre, dirección, email y teléfono.
    """

class BaseDatosClientes:
    def __init__(self, nombre_archivo="happyBurger.db"):
        self.nombre_archivo = nombre_archivo
        self.conexion = sqlite3.connect(nombre_archivo)
        self.cursor = self.conexion.cursor()

    def agregar_cliente(self, clave, nombre, direccion, email, telefono):
        # Agregar un cliente a la tabla
        self.cursor.execute("INSERT INTO clientes (clave, nombre, direccion, email, telefono) VALUES (?,?,?,?,?)",
                            (clave, nombre, direccion, email, telefono))
        self.conexion.commit()
        print("Cliente agregado correctamente")

    def obtener_clientes(self):
        # Obtener todos los clientes de la tabla
        self.cursor.execute("SELECT * FROM clientes")
        clientes=self.cursor.fetchall()
        print("Lista de clientes")
        for cliente in clientes:
            print(cliente)

    #def cerrar_conexion(self):
        # Cerrar la conexión a la base de datos
        #self.conexion.close()


    def eliminar_cliente(self, clave):
        #Eliminar cliente por clave de cliente
        #clave = input("Ingrese la clave del cliente que desea eliminar: ")
        self.cursor.execute("DELETE FROM clientes WHERE clave=?", (clave,))
        self.conexion.commit()
        print("Cliente eliminado correctamente.")
        
        
    def modificar_cliente(self, clave, nueva_clave, nuevo_nombre, nueva_direccion, nuevo_email, nuevo_telefono):
        #Modificar cliente existente por clave de cliente
        clave = input("Ingrese la clave del cliente que desea modificar: ")
        
        self.cursor.execute("UPDATE clientes SET clave=?, nombre=?, direccion=?,email=?, telefono=? WHERE clave=?",
                                   (nueva_clave, nuevo_nombre, nueva_direccion, nuevo_email, nuevo_telefono, clave))
        self.conexion.commit()
        print("Cliente modificado correctamente.")
    

    def pedir_datos_cliente(self):
        #Ingresar datos de cliente nuevo
        clave = input("Ingrese la clave del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")
        email = input("Ingrese el email del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        return clave, nombre, direccion, email, telefono
        print("Cliente agregado con éxito")


    def gestion_clientes(self):
        #Direccionar a la función correspondiente
        while True:
            print("Menú:")
            print("1. Ver lista de clientes")
            print("2. Agregar cliente")
            print("3. Modificar cliente por clave")
            print("4. Eliminar cliente por clave")
            print("5. Regresar al menú principal")
            print("----------------------------")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.obtener_clientes()
            elif opcion == '2':
                clave, nombre, direccion, email, telefono = self.pedir_datos_cliente()
                self.agregar_cliente(clave, nombre, direccion, email, telefono)
            elif opcion == '3':
                print("Esta es la lista actual de clientes: ")
                self.obtener_clientes()
                nueva_clave, nuevo_nombre, nueva_direccion, nuevo_email, nuevo_telefono = self.modificar_cliente()
                self.modificar_cliente(clave, nueva_clave, nuevo_nombre, nueva_direccion, nuevo_email, nuevo_telefono)
            elif opcion == '4':
                print("Esta es la lista actual de clientes: ")
                self.obtener_clientes()
                clave = input ("Ingrese el número de clave del cliente a eliminar")
                self.eliminar_cliente(clave)
            elif opcion == '5':
                print("----------------------------")
                print("Menú principal.")
                self.conexion.close()
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
                
        self.conexion.close()
        

    