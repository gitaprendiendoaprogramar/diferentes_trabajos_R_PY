from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Inicio():
    return render_template("index.html")

@app.route("/Acercade")
def Acerca():
    return render_template("Acerca.html")

@app.route("/Trilladoras")
def Trilladoras():
    return render_template("Trilladoras.html")

@app.route("/Foro")
def Foro():
    return render_template("Foro.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/login")
def loginn():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
