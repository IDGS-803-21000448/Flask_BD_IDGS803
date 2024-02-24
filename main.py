from flask import Flask, render_template, request, Response
import forms
from flask import g
from flask import flash
from flask import redirect
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.secret_key = "esta es la clave secreta"


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
#-------------------------------
@app.before_request
def before_request():
    #g.nombre = "Daniel"
   
    print("before_request")


# --------------------
    
@app.after_request
def after_request(response):
    print('ultimo')
    g.nombre = " "
    if 'Daniel' not in g.nombre and request.endpoint not in ['index']:
        return redirect('index')
    return response

# ---------------------    
@app.route("/index")
def index():
    g.nombre = "Jose"

    escuela = "UTL!!!"
    alumnos = ["Mario", "Pedro", "Luis", "Dario"]
    return render_template("index.html",escuela = escuela, alumnos = alumnos)

@app.route("/hola")
def hola():
    return "<p> <h1> Hola desde HOLA!!!!! <h1> </p>"

@app.route("/user/<string:name>")
def user(name):
    return "<h1> Hola "+name+"</h1>"

@app.route("/numero/<int:n>")
def numero(n):
    return "El numero es: {}".format(n)

@app.route("/user/<int:id>/<string:name>")
def func(id, name):
    return f"ID: {id} Nombre: {name}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"La suma es {n1} + {n2} = {n1+n2}"

@app.route("/default")
@app.route("/default/<string:ab>")
def func1(ab = "UTL"):
    return "El Valor es "+ab

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    print("Dentro de alumnos")
    print(f"Hola {g.nombre}")
    nom = ''
    apa = ''
    ama = ''
    alum_form = forms.UsersForm(request.form)
    if request.method == "POST" and alum_form.validate():
        nom = alum_form.nombre.data
        apa = alum_form.apaterno.data
        ama = alum_form.amaterno.data

        mensaje = f"Bienvenido {nom}"
        flash(mensaje)
    
    return render_template("alumnos.html",
                            form = alum_form,
                            nom=nom, apa=apa, ama=ama)

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")


@app.route("/multiplicar", methods=["GET", "POST"])
def multiplicar():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")

        return f"<h1> La multiplicacion es: {str(int(num1) * int(num2))} </h1>"
    else:
        return '''
                    <input type= "text" name="n1"/> </br>
                    <label>N2: </label>
                    <input type= "text" name="n2"/> </br>
                    <input type="submit"/>
                <form action="/multiplicar" method="POST">
                    <label>N1: </label>
                </form>
             '''

@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")

@app.route("/resultado",  methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")

        return f"<h1> La multiplicacion es: {str(int(num1) * int(num2))} </h1>"

@app.route("/formulario2")
def formulario2():
    nom = apa = ama = ''
    alumn_form = Forms.UserForm(request.form)


    return render_template("formulario2.html")


if __name__ == "__main__":
    app.run(debug=True)
