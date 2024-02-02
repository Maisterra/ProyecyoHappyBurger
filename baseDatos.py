import sqlite3

# Conectar a la base de datos (creará el archivo si no existe)
conexion = sqlite3.connect('happyBurger.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Definir los comandos SQL para crear las tablas
tablaPedidos = """
CREATE TABLE IF NOT EXISTS Pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_pedido INTEGER NOT NULL,
    nombre_cliente TEXT NOT NULL,
    producto TEXT NOT NULL,
    precio FLOAT NOT NULL
)
"""

tablaClientes = """
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    clave TEXT NOT NULL,
    nombre TEXT NOT NULL,
    direccion TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL
)
"""

tablaMenu = """
CREATE TABLE IF NOT EXISTS Menu (
    id INTEGER PRIMARY KEY,
    clave TEXT NOT NULL,
    nombreProducto TEXT NOT NULL,
    precio FLOAT NOT NULL
)
"""

# Ejecutar los comandos SQL
cursor.execute(tablaPedidos)
cursor.execute(tablaClientes)
cursor.execute(tablaMenu)

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
