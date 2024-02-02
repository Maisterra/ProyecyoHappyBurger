from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

    # Ruta para manejar las consultas de pedidos
@app.route('/consultar_pedidos', methods=['POST', 'GET'])
def consultar_pedidos():
    if request.method == 'POST':
        # Verificar si se presionó el botón "Consultar Pedido" o "Consultar Todos los Pedidos"
        if 'consultar_todos' in request.form:
            # Realizar la consulta a la base de datos para obtener todos los pedidos
            resultados = []
            with sqlite3.connect('happyBurger.db') as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM Pedidos")
                resultados = cursor.fetchall()

            return render_template('resultados.html', resultados=resultados)
        else:
            # Obtener los parámetros de búsqueda del formulario HTML
            numero_pedido = request.form['numero_pedido']
            nombre_cliente = request.form['nombre_cliente']

            # Realizar la consulta a la base de datos
            resultados = []
            with sqlite3.connect('happyBurger.db') as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM Pedidos WHERE numero_pedido=? OR nombre_cliente=?", (numero_pedido, nombre_cliente))
                resultados = cursor.fetchall()

            return render_template('resultados.html', resultados=resultados)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
"""   
    
    # Ruta para manejar las consultas de pedidos
@app.route('/consultar_pedidos', methods=['POST', 'GET'])
def consultar_pedidos():
    # Ruta para manejar las consultas de pedidos
@app.route('/consultar_pedidos', methods=['POST', 'GET'])
def consultar_pedidos():
    if request.method == 'POST':
        # Verificar si se presionó el botón "Consultar Pedido" o "Consultar Todos los Pedidos"
        if 'consultar_todos' in request.form:
            # Realizar la consulta a la base de datos para obtener todos los pedidos
            resultados = []
            with sqlite3.connect('happyBurger.db') as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM Pedidos")
                resultados = cursor.fetchall()

            return render_template('resultados.html', resultados=resultados)
        else:
            # Obtener los parámetros de búsqueda del formulario HTML
            numero_pedido = request.form['numero_pedido']
            nombre_cliente = request.form['nombre_cliente']

            # Realizar la consulta a la base de datos
            resultados = []
            with sqlite3.connect('happyBurger.db') as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM Pedidos WHERE numero_pedido=? OR nombre_cliente=?", (numero_pedido, nombre_cliente))
                resultados = cursor.fetchall()

            return render_template('resultados.html', resultados=resultados)
    else:
        return render_template('index.html')
"""

