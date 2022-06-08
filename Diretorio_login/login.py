from functools import wraps
from flask import Blueprint, render_template , redirect , request, url_for, session, jsonify
from funcoes import Funcoes , LogEnum

bp_login = Blueprint('login',__name__, url_prefix="/login", template_folder= 'templates')

@bp_login.route("/" )
def login():
    return render_template("loginDesktop.html" , falhalogin = 0)

@bp_login.route("/logoff", methods = ['POST' , 'GET'] )
def logoff():
    session.pop('nome' , None)
    return redirect(url_for('home.rotaHome'))

@bp_login.route("/logar", methods = ['POST' , 'GET'] )
def logar():
    loginEhValido = False;
    if request.method == "POST":
        nome = request.form['nome']
        senhaCripto = Funcoes.cifrarSenha(request.form['senha'])
        if(nome == "admin" and senhaCripto==Funcoes.cifrarSenha("admin")):  
            loginEhValido = True;
    if loginEhValido:        
        session['nome'] = "loginValido"        
        return redirect(url_for("admin.homeAdmin"))
    else:
        return render_template( "loginDesktop.html" , falhalogin=1)



def validarSessao(f):
    @wraps(f)
    #criando uma função aqui dentro do wraps
    def decorated_function(*args, **kwargs):
        if 'nome' not in session:
            return redirect(url_for('login.login', falhalogin = 1))
        else:
            return f(*args, **kwargs)
    #retornando a função que acabamos de criar
    return decorated_function