from flask import Flask
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_PASSWORD"] = "localhost"
app.config["MYSQL_USER"] = "localhost"
app.config["MYSQL_DB"] = "pruebaflask" #le pido que se conecte a la base de datos prueba flask

mysql = MySQL(app)

#en templates guardo todo lo que se ve

@app.route("/")
def index():
    return "hello world"

if __name__ == "__main__":
    app.run(port = 3000, debug = True)