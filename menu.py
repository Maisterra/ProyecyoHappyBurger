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

    def obtener_menu(self):
        # Obtener todos los productos de menu de la tabla
        self.cursor.execute("SELECT * FROM Menu")
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        # Cerrar la conexión a la base de datos
        self.conexion.close()

def pedir_datos_menu():
    #Ingresar un nuevo producto al Menú
    clave = input("Ingrese la clave del producto: ")
    nombreProducto = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    return clave, nombreProducto, precio




    #Menu de funcionalidad de la base de datos

def mostrar_lista_menu(base_datos_menu):
    #Mostrar lista de productos en el menú
    menus = base_datos_menu.obtener_menu()
    print("Lista de productos en el Menu:")
    for menu in menus:
        print(menu)

def agregar_menu(base_datos_menu):
    #Agregar un nuevo producto al Menú
    clave, nombreProducto, precio = pedir_datos_menu()
    base_datos_menu.agregar_menu(clave, nombreProducto, precio)
    print("Producto agregado correctamente al Menú.")

def modificar_menu(base_datos_menu):
    #Modificar datos de un producto por número de clave
    clave = input("Ingrese el número de clave del producto a modificar: ")
    
    # Solicitar los nuevos datos del producto del Menú
    nuevo_clave = input("Ingrese la nueva clave del producto del Menú: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    nuevo_precio = input("Ingrese el nuevo precio: ")
    
    # Actualizar los datos del producto en la base de datos
    base_datos_menu.cursor.execute("UPDATE Menu SET clave=?, nombreProducto=?, precio=? WHERE clave=?",
                                   (nuevo_clave, nuevo_nombre, nuevo_precio, clave))
    base_datos_menu.conexion.commit()
    print("Producto modificado correctamente del Menú.")
    


def eliminar_menu(base_datos_menu):
    #Eliminar producto por número de clave
    clave = input("Ingrese el número de clave del producto a eliminar: ")
    base_datos_menu.cursor.execute("DELETE FROM Menu WHERE clave=?", (clave,))
    base_datos_menu.conexion.commit()
    print("Producto eliminado correctamente del Menú.")


def mostrar_menu():
    print("Menú:")
    print("1. Ver lista de productos en el Menú")
    print("2. Agregar producto al Menú")
    print("3. Modificar producto del Menú")
    print("4. Eliminar producto del Menú")
    print("5. Regresar al menú principal")
    print("----------------------------")

def main():
    base_datos_menu = BaseDatosMenu()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_lista_menu(base_datos_menu)
        elif opcion == '2':
            agregar_menu(base_datos_menu)
        elif opcion == '3':
            modificar_menu(base_datos_menu)
        elif opcion == '4':
            eliminar_menu(base_datos_menu)
        elif opcion == '5':
            print("----------------------------")
            print("Menú principal.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    base_datos_menu.cerrar_conexion()

if __name__ == "__main__":
    main()