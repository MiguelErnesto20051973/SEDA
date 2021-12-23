from os import close, name
import re
from flask import Flask, app, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL, MySQLdb
from werkzeug.datastructures import TypeConversionDict

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'app_citas'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template("contenido.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form('email')
        password = request.form('password')

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Users WHERE email=%s",(email, ))
        user = cur.fetchone()
        cur.close()

        if len(user)>0:
            if password == user["password"]:
                session['name'] = user['name']
                session['email'] = user['email']
                session['tipo'] = user['id_tip_usu']

                if session['tipo'] == 1:
                    return render_template("premiun/home.html")
                elif session['tipo'] == 2:
                    return render_template("estandar/homeTwo.html")
                else:
                    return "Error, Correo o contraseña no valida"
            else:
                return "No exisite el usuario"
        else:
            return render_template("login.html")        
    
@app.route('/registro', methods= ["GET", "POST"])
def registro():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tip_usu")
    tipo = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM gen_interes")
    interes = cur.fetchall()

    cur:close()

    if request.method == 'GET':
        return render_template("registro.html", tipo = tipo, interes = interes)

    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        tip = request.form['tipo']
        interes = request.form['interes']   

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, password, id_tip_usu, interes) VALUES(%s, %s, %s, %s, %s)", (name, email, password, tip, interes))  
        mysql.connection.comit()
        return render_template

if __name__ == '__main__':
    app.run(debug=True)