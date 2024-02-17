
# Módulo Pedidos
import sqlite3
from menu import BaseDatosMenu  # Importar la clase BaseDatosMenu desde el módulo menu

"""Módulo de Pedidos (clase BaseDatosPedidos): Permite gestionar la información de los pedidos.
Incluye: clave, nombreProducto y precio del producto. Muestra, agrega, modifica y eñimina pedidos.
    """

class BaseDatosPedidos:
    def __init__(self, nombre_archivo="happyBurger.db"):
        self.nombre_archivo = nombre_archivo
        self.conexion = sqlite3.connect(nombre_archivo)
        self.cursor = self.conexion.cursor()

    def agregar_pedido(self, pedido, nombre, producto, precio):
        # TXT Abrir archivo de texto en modo de escritura para agregar al final del archivo cada pedido 
        with open("pedidos.txt", "a") as archivo:
            # Escribir la información del pedido en el archivo
            archivo.write(f"Pedido: {pedido}\n")
            archivo.write(f"Cliente: {nombre}\n")
            archivo.write(f"Producto: {producto}\n")
            archivo.write(f"Precio: {precio}\n")
            archivo.write("-------------------------\n")
        
        
        #Abrir la base de datos happyBurger e inserta un nuevo pedido
        self.cursor.execute("INSERT INTO Pedidos (numero_pedido, nombre_cliente, producto, precio) VALUES (?, ?, ?, ?)",
                            (pedido, nombre, producto, precio))
        self.conexion.commit()
        print("Pedido agregado correctamente")

    def obtener_pedidos(self):
        #Obtener los datos de los pedidos existentes
        self.cursor.execute("SELECT * FROM Pedidos")
        pedidos=self.cursor.fetchall()
        print("Estos son los pedidos actuales")
        for pedido in pedidos:
            print(pedido)

    def modificar_pedido(self, pedido, nuevo_pedido, nuevo_nombre, nuevo_producto, nuevo_precio):
        #Modificar un pedido ya existente con base en el número de pedido
        self.cursor.execute("UPDATE Pedidos SET numero_pedido=?, nombre_cliente=?, producto=?, precio=? WHERE numero_pedido=?",
                            (nuevo_pedido, nuevo_nombre, nuevo_producto, nuevo_precio, pedido))
        self.conexion.commit()

    def eliminar_pedido(self, pedido):
        #Eliminar un pedido con base en el número de pedido
        self.cursor.execute("DELETE FROM Pedidos WHERE numero_pedido=?", (pedido,))
        self.conexion.commit()
        print("Pedido eliminado correctamente")




    def pedir_datos_pedido(self):
    #Pedir los datos del nuevo pedido: número, nombre del cliente, nombre del producto y precio
        pedido = input("Ingrese el número de pedido: ")
        nombre = input("Ingrese el nombre de la persona: ")
        producto = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        # Imprimir el ticket simulado en la consola
        print("Ticket:")
        print(f"Pedido: {pedido}")
        print(f"Cliente: {nombre}")
        print(f"Producto: {producto}")
        print(f"Precio: {precio}")
        print("----------------------------")
        return pedido, nombre, producto, precio
        
    
    
    def gestion_pedidos(self):
        #Direccionar a la función correspondiente
        
        while True:
            #Imprimir en consola Menú de funcionalidades del módulo pedidos
            print("Menú:")
            print("1. Ver lista de pedidos")
            print("2. Agregar pedido")
            print("3. Modificar pedido por número de pedido")
            print("4. Eliminar pedido por número de pedido")
            print("5. Regresar al menú principal")
            print("----------------------------")
            
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.obtener_pedidos()
        

                
            elif opcion == '2':
                # Crea una instancia de la clase BaseDatosMenu
                base_datos_menu = BaseDatosMenu()
                # Obtiene los productos del menú
                productos_menu = base_datos_menu.obtener_menu()
                # Muestra los precios y productos existentes en el Menú al usuario 
                print("----------------------------")
                print("Estos son los productos disponibles y sus precios:")
                for producto in productos_menu:
                    print(f"{producto[2]} - Precio: {producto[3]}")
                    print("----------------------------")
                pedido, nombre, producto, precio = self.pedir_datos_pedido()
                self.agregar_pedido(pedido, nombre, producto, precio)
                
            elif opcion == '3':
                pedido = input("Ingrese el número de pedido a modificar: ")
                nuevo_pedido, nuevo_nombre, nuevo_producto, nuevo_precio = self.pedir_datos_pedido()
                self.modificar_pedido(pedido, nuevo_pedido, nuevo_nombre, nuevo_producto, nuevo_precio)
                print("Pedido modificado correctmente")
                
            elif opcion == '4':
                print("Existen estos pedidos:")
                self.obtener_pedidos()
                pedido=input("Ingrese el número de pedido que desea eliminar: ")
                self.eliminar_pedido(pedido)
                
            elif opcion == '5':
                print("----------------------------")
                print("Menú principal.")
                self.conexion.close()
                break
            else:
                
                print("Opción inválida. Por favor, seleccione una opción válida.")
        
        
        
    
    
    
    








"""def mostrar_menu_productos():
    # Crea una instancia de la clase BaseDatosMenu
    base_datos_menu = BaseDatosMenu()
    # Obtiene los productos del menú
    productos_menu = base_datos_menu.obtener_menu()
    # Muestra los precios y productos existentes en el Menú al usuario 
    print("----------------------------")
    print("Estos son los productos disponibles y sus precios:")
    for producto in productos_menu:
        print(f"{producto[2]} - Precio: {producto[3]}")
        print("----------------------------")"""