from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL

app=Flask(__name__)

#MYSQL conexion
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "prubaflask" #le pido que se conecte a la base de datos prueba flask
#cuando pongo el puerto no anda
mysql = MySQL(app)

#iniciamos sesion(guarda datos en una memoria para luego usarlos)
app.secret_key="mysecretkey"


#en templates guardo todo lo que se ve

@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contacts")
    data = cur.fetchall()
    return render_template("index.html", contactos=data) #mando a renderizar una pagina html

@app.route("/add_contact", methods=['POST'])
def add_contact():
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        print(nombre)
        print(email)
        print(telefono)
        cur = mysql.connection.cursor() #me conecto con la BDD
        cur.execute("INSERT INTO contacts (nombre,telefono,email) VALUES (%s, %s, %s)", 
        (nombre, telefono, email)) #hago la consulta SQL
        mysql.connection.commit() #guardo los cambios
        flash("contacto agregado satifactoriamente") #envia mesajes entre vistas
        return redirect(url_for("index")) #hago que se vuelva a cargar index.html al agregar un contacto


@app.route("/borrar/<string:id>")#recibo un parametro tipo string
def borrar_contacto(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM contacts WHERE id = " + id )
    mysql.connection.commit() #guardo los cambios
    flash("contacto eliminado satifactoriamente") #envia mesajes entre vistas
    return redirect(url_for("index"))



@app.route("/editar/<id>")
def agregar_contacto(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contacts WHERE ID = " + id )
    data = cur.fetchall()
    print(data[0])
    flash("contacto editado satisfactoriamente") #envia mesajes entre vistas
    return render_template("editar-contacto.html", contacto=data[0])


@app.route("/actualizar/<id>", methods=["POST"])
def act(id):
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        print(nombre)
        print(email)
        print(telefono)
        cur = mysql.connection.cursor() #me conecto con la BDD
        cur.execute("""
                    UPDATE contacts
                    SET nombre = %s,
                    telefono = %s,
                    email = %s
                    WHERE id=%s
        """,(nombre, telefono, email,id)) #hago la consulta SQL
        mysql.connection.commit() #guardo los cambios
        flash("contacto modificado satifactoriamente") #envia mesajes entre vistas
        return redirect(url_for("index")) #hago que se vuelva a cargar index.html al agregar un contacto


    
if __name__ == "__main__":
    app.run(port = 3000, debug = True) #hacemos que se refresque solo


    #flask usa un motor de plantilla, no es html puro, tiene otras cosillas