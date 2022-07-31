import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect

from werkzeug.exceptions import abort

app = Flask(__name__)
#Declaracion de rutas 
def index():
    return render_template('/index.html')
 

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

@app.route('/consultas')
def consultas():
    return render_template('consultas.html')

@app.route('/ventas')
def ventas():
    return render_template('ventas.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')


if __name__ == '__main__':
    app.run(debug=True)
