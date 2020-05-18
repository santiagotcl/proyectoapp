from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_USER"] = "password"
app.config["MYSQL_PORT"] = "3000"
app.config["MYSQL_DB"] = "pruebaflask" #le pido que se conecte a la base de datos prueba flask

mysql = MySQL(app)

#en templates guardo todo lo que se ve

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_contact", methods=['POST'])
def add_contact():
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        print(nombre)
        print(email)
        print(telefono)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (nombre,telefono,email) VALUES (%s, %s, %s)", 
        (nombre, telefono, email))
        mysql.connection.commit()
        return "contacto añadido"

if __name__ == "__main__":
    app.run(port = 3000, debug = True)