import os

from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "database.db"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

@app.route("/")
def inicio():
    return render_template("home.html")

@app.route("/Acerca_de/")
def acerca_de():
    return "acerca_de.html"

#    return render_template("acerca_de.html")


@app.route("/Trilladoras/")
def trilladoras():
    return "trilladoras.html"

#    return render_template("trilladoras.html")


@app.route("/Foro/")
def foro():
    return "foro.html"

#    return render_template("Foro.html")

@app.route("/Calculo_fr/")
def calculo_fr():
    return "calculo_fr.html"

@app.route("/Informate/")
def informate():
    return "informate.html"

@app.route("/Registro/", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        # lee del campo nickname del form
        nickname = request.form["nickname"]

        # lee del campo password del form, y lo encripta
        password = generate_password_hash(request.form["password"], method="sha256")

        new_user = User(nickname=nickname, password=password)
        db.session.add(new_user)
        db.session.commit()
        print("registro añadido")
        return redirect(url_for('registro'))
    return render_template("registro.html")

@app.route("/Login/")
def login():
    return "login.html"

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
