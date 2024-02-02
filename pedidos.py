# Modulo Pedidos
# Módulo Pedidos
import sqlite3
from menu import BaseDatosMenu  # Importar la clase BaseDatosMenu desde el módulo menu

class BaseDatosPedidos:
    def __init__(self, nombre_archivo="happyBurger.db"):
        self.nombre_archivo = nombre_archivo
        self.conexion = sqlite3.connect(nombre_archivo)
        self.cursor = self.conexion.cursor()

    def agregar_pedido(self, pedido, nombre, producto, precio):
        self.cursor.execute("INSERT INTO Pedidos (numero_pedido, nombre_cliente, producto, precio) VALUES (?, ?, ?, ?)",
                            (pedido, nombre, producto, precio))
        self.conexion.commit()

    def obtener_pedidos(self):
        self.cursor.execute("SELECT * FROM Pedidos")
        return self.cursor.fetchall()

    def modificar_pedido(self, pedido, nuevo_pedido, nuevo_nombre, nuevo_producto, nuevo_precio):
        self.cursor.execute("UPDATE Pedidos SET numero_pedido=?, nombre_cliente=?, producto=?, precio=? WHERE numero_pedido=?",
                            (nuevo_pedido, nuevo_nombre, nuevo_producto, nuevo_precio, pedido))
        self.conexion.commit()

    def eliminar_pedido(self, pedido):
        self.cursor.execute("DELETE FROM Pedidos WHERE numero_pedido=?", (pedido,))
        self.conexion.commit()

    def cerrar_conexion(self):
        self.conexion.close()

def mostrar_menu_productos():
    # Crea una instancia de la clase BaseDatosMenu
    base_datos_menu = BaseDatosMenu()
    # Obtiene los productos del menú
    productos_menu = base_datos_menu.obtener_menu()
    # Muestra los productos al usuario
    print("----------------------------")
    print("Estos son los productos disponibles y sus precios:")
    for producto in productos_menu:
        print(f"{producto[2]} - Precio: {producto[3]}")
        print("----------------------------")

def pedir_datos_pedido():
    pedido = input("Ingrese el número de pedido: ")
    nombre = input("Ingrese el nombre de la persona: ")
    producto = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    return pedido, nombre, producto, precio

def mostrar_lista_pedidos(base_datos_pedidos):
    pedidos = base_datos_pedidos.obtener_pedidos()
    print("Lista de pedidos:")
    for pedido in pedidos:
        print(pedido)

def agregar_pedido(base_datos_pedidos):
    mostrar_menu_productos()  # Mostrar los productos disponibles y sus precios
    pedido, nombre, producto, precio = pedir_datos_pedido()
    base_datos_pedidos.agregar_pedido(pedido, nombre, producto, precio)
    print("Pedido agregado correctamente.")
    
# Imprimir el ticket simulado en la consola
    print("Ticket:")
    print(f"Pedido: {pedido}")
    print(f"Cliente: {nombre}")
    print(f"Producto: {producto}")
    print(f"Precio: {precio}")
    print("----------------------------")

def modificar_pedido(base_datos_pedidos):
    pedido = input("Ingrese el número de pedido que desea modificar: ")
    nuevo_pedido, nuevo_nombre, nuevo_producto, nuevo_precio = pedir_datos_pedido()
    base_datos_pedidos.modificar_pedido(pedido, nuevo_pedido, nuevo_nombre, nuevo_producto, nuevo_precio)
    print("Pedido modificado correctamente.")

def eliminar_pedido(base_datos_pedidos):
    pedido = input("Ingrese el número de pedido que desea eliminar: ")
    base_datos_pedidos.eliminar_pedido(pedido)
    print("Pedido eliminado correctamente.")

def mostrar_menu_pedidos():
    print("Menú:")
    print("1. Ver lista de pedidos")
    print("2. Agregar pedido")
    print("3. Modificar pedido por número de pedido")
    print("4. Eliminar pedido por número de pedido")
    print("5. Regresar al menú principal")
    print("----------------------------")

def main():
    base_datos_pedidos = BaseDatosPedidos()
    
    while True:
        mostrar_menu_pedidos()  # Mostrar el menú de opciones de pedidos
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_lista_pedidos(base_datos_pedidos)
        elif opcion == '2':
            agregar_pedido(base_datos_pedidos)
        elif opcion == '3':
            modificar_pedido(base_datos_pedidos)
        elif opcion == '4':
            eliminar_pedido(base_datos_pedidos)
        elif opcion == '5':
            print("----------------------------")
            print("Menú principal.")

            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    base_datos_pedidos.cerrar_conexion()

if __name__ == "__main__":
    main()




"""

#Modulo Pedidos
import sqlite3
from menu import BaseDatosMenu

class BaseDatosPedidos:
    def __init__(self, nombre_archivo="happyBurger.db"):
        self.nombre_archivo = nombre_archivo
        self.conexion = sqlite3.connect(nombre_archivo)
        self.cursor = self.conexion.cursor()

    def agregar_pedido(self, pedido, nombre, producto, precio):
        self.cursor.execute("INSERT INTO Pedidos (numero_pedido, nombre_cliente, producto, precio) VALUES (?, ?, ?, ?)",
                            (pedido, nombre, producto, precio))
        self.conexion.commit()

    def obtener_pedidos(self):
        self.cursor.execute("SELECT * FROM Pedidos")
        return self.cursor.fetchall()

    def modificar_pedido(self, pedido, nuevo_pedido, nuevo_nombre, nuevo_producto, nuevo_precio):
        self.cursor.execute("UPDATE Pedidos SET numero_pedido=?, nombre_cliente=?, producto=?, precio=? WHERE numero_pedido=?",
                            (nuevo_pedido, nuevo_nombre, nuevo_producto, nuevo_precio, pedido))
        self.conexion.commit()

    def eliminar_pedido(self, pedido):
        self.cursor.execute("DELETE FROM Pedidos WHERE numero_pedido=?", (pedido,))
        self.conexion.commit()

    def cerrar_conexion(self):
        self.conexion.close()
        
def mostrar_menu():
    # Crea una instancia de la clase BaseDatosMenu
    base_datos_menu = BaseDatosMenu()
    # Obtiene los productos del menú
    productos_menu = base_datos_menu.obtener_menu()
    # Muestra los productos al usuario
    print("Estos son los productos disponibles y sus precios:")
    for producto in productos_menu:
        print(f"{producto[1]} - Precio: {producto[2]}")  # Suponiendo que el nombre y el precio están en la segunda y tercera posición de cada tupla


def pedir_datos_pedido():
    pedido = input("Ingrese el número de pedido: ")
    nombre = input("Ingrese el nombre de la persona: ")
    producto = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    return pedido, nombre, producto, precio

def mostrar_lista_pedidos(base_datos_pedidos):
    pedidos = base_datos_pedidos.obtener_pedidos()
    print("Lista de pedidos:")
    for pedido in pedidos:
        print(pedido)

def agregar_pedido(base_datos_pedidos):
    pedido, nombre, producto, precio = pedir_datos_pedido()
    base_datos_pedidos.agregar_pedido(pedido, nombre, producto, precio)
    print("Pedido agregado correctamente.")

def modificar_pedido(base_datos_pedidos):
    pedido = input("Ingrese el número de pedido que desea modificar: ")
    nuevo_pedido, nuevo_nombre, nuevo_producto, nuevo_precio = pedir_datos_pedido()
    base_datos_pedidos.modificar_pedido(pedido, nuevo_pedido, nuevo_nombre, nuevo_producto, nuevo_precio)
    print("Pedido modificado correctamente.")

def eliminar_pedido(base_datos_pedidos):
    pedido = input("Ingrese el número de pedido que desea eliminar: ")
    base_datos_pedidos.eliminar_pedido(pedido)
    print("Pedido eliminado correctamente.")

def mostrar_menu():
    print("Menú:")
    print("1. Ver lista de pedidos")
    print("2. Agregar pedido")
    print("3. Modificar pedido por número de pedido")
    print("4. Eliminar pedido por número de pedido")
    print("5. Salir")

def main():
    base_datos_pedidos = BaseDatosPedidos()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_lista_pedidos(base_datos_pedidos)
        elif opcion == '2':
            agregar_pedido(base_datos_pedidos)
        elif opcion == '3':
            modificar_pedido(base_datos_pedidos)
        elif opcion == '4':
            eliminar_pedido(base_datos_pedidos)
        elif opcion == '5':
            print("Volver al menu principal.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    base_datos_pedidos.cerrar_conexion()

if __name__ == "__main__":
    main()


"""