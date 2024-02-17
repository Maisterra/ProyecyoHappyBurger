#Módulo de Menú
import sqlite3

"""Módulo de Menú (clase BaseDatosMenu): Permite gestionar la información de los productos en el menú registrados.
Incluye: clave, nombreProducto y precio del producto.
    """

class BaseDatosMenu:
    
    def __init__(self, nombre_archivo="happyBurger.db"):
        self.nombre_archivo = nombre_archivo
        self.conexion = sqlite3.connect(nombre_archivo)
        self.cursor = self.conexion.cursor()

    def agregar_menu(self, clave, nombreProducto, precio):
        # Agregar un producto de menu a la tabla
        self.cursor.execute("INSERT INTO Menu (clave, nombreProducto, precio) VALUES (?,?,?)",
                            (clave, nombreProducto, precio))
        self.conexion.commit()
        print("Producto agregado correctamente al Menú.")

    def obtener_menu(self):
        # Obtener todos los productos de menu de la tabla
        self.cursor.execute("SELECT * FROM Menu")
        menus=self.cursor.fetchall()
        
        print("Lista de productos en el Menu:")
        for menu in menus:
            print(menu)
        return menus
        
    
    def modificar_menu(self, clave, nuevo_clave, nuevo_nombre, nuevo_precio):
        #Modificar datos de un producto por número de clave
        self.cursor.execute("UPDATE Menu SET clave=?, nombreProducto=?, precio=? WHERE clave=?",
                            (nuevo_clave, nuevo_nombre, nuevo_precio, clave))
        self.conexion.commit()
        
        
    def eliminar_menu(self, clave):
       #Eliminar producto por número de clave
        self.cursor.execute("DELETE FROM Menu WHERE clave=?", (clave,))
        self.conexion.commit()
        print("Producto eliminado correctamente del Menú.")
    

    def pedir_datos_menu(self):
        #Ingresar un nuevo producto al Menú
        clave = input("Ingrese la clave del producto: ")
        nombreProducto = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        return clave, nombreProducto, precio

    
        

    def gestion_menu(self):
    #Direccionar a la funcionalidad correspondiente
        
        while True:
            print("Menú:")
            print("1. Ver lista de productos en el Menú")
            print("2. Agregar producto al Menú")
            print("3. Modificar producto del Menú")
            print("4. Eliminar producto del Menú")
            print("5. Regresar al menú principal")
            print("----------------------------")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.obtener_menu()
            elif opcion == '2':
                clave, nombre, precio = self.pedir_datos_menu()
                self.agregar_menu(clave, nombre, precio)
            
            elif opcion == '3':
                clave = input("Ingrese el número de clave del producto a modificar: ")
                nuevo_clave, nuevo_nombre, nuevo_precio = self.pedir_datos_menu()
                self.modificar_menu(clave, nuevo_clave, nuevo_nombre, nuevo_precio)
                print("Producto modificado correctamente del Menú.")
            elif opcion == '4':
                print ("Existen estos productos: ")
                self.obtener_menu()
                clave = input("Ingrese el número de clave del producto a eliminar: ")
                self.eliminar_menu(clave)
            elif opcion == '5':
                print("----------------------------")
                print("Menú principal.")
                
                self.conexion.close()
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

        
