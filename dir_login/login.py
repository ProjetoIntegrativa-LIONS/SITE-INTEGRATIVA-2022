from functools import wraps
from flask import Blueprint, render_template , redirect , request, url_for, session, jsonify
#from dao_project.ModelUsuario import DAOUsuario, Usuario
from funcoes import Funcoes , LogEnum


bp_login = Blueprint('login',__name__, url_prefix="/login", template_folder= 'templates')

@bp_login.route("/", methods = ['POST' , 'GET'] )
def login():
    return render_template("login.html" , falhalogin = 0)

#ABRINDO FORMULARIO DE CADASTRODE CONTAS NOVAS
@bp_login.route("/formCadastro", methods =['POST', 'GET'])
def formularioCriacao():
    return render_template("cadastroLogin.html")

#CRIANDO UMA CONTA NOVA E GUARDANDO NO BANCO
@bp_login.route("/criarConta", methods= ['POST'])
def CadastrarConta():
    """
    nome = request.form['name']
    email = request.form['email']
    bancoUsuario = DAOUsuario()
    senhaCripto = Funcoes.cifrarSenha(request.form['senha1'])
    
    if ( (bancoUsuario.VerificarExistencia(email)) == False ):
        user = Usuario(email=email, nome=nome, senha=senhaCripto)
        bancoUsuario.Insert(user)
        Funcoes.criaLog(LogEnum.INFO, LogEnum.save, request.path, "", "Cadastro de conta com sucesso")
        return render_template("login.html")
    else:
        return render_template("cadastroLogin.html", falhalogin=1)
        """
    return render_template("cadastroLogin.html", falhalogin=1)

#PEGANDO OS DADOS DO CAMPO DE LOGIN, VERIFICANDO AUTENTIFICAÇÃO, CRIANDO O LOGIN NA SESSION
@bp_login.route("/login", methods = ['POST'])
def CriarLogin():
    if request.method == "POST":
        nome = request.form['nome']
        senhaCripto = Funcoes.cifrarSenha(request.form['senha'])
        bancoUsuario = DAOUsuario()
        loginValido = bancoUsuario.SelectLoginSenha(senhaCripto, nome)
    if loginValido:
        #LIMPANDO E ADICIONANDO A SESSÃO DO USUARIO
        session.clear()
        session['nome'] = nome
        Funcoes.criaLog(LogEnum.INFO, LogEnum.login, request.path, nome, "Login Realizado com sucesso!")
        return redirect(url_for("home.rotaHome"))
    else :
        Funcoes.criaLog(LogEnum.WARNING, LogEnum.falhaLogin, request.path, nome, "Tentativa de login!")
        return redirect(url_for('login.login' , falhalogin =1))

#VERIFICANDO COM JASON (assíncrono) PARA VERIFICAR SE O EMAIL JÁ TEM CADASTRO NA BASE
@bp_login.route("/verificar", methods = ['POST'])
def verificar():
    email = request.form['email']
    print(email)
    banco = DAOUsuario()
    return jsonify(login_existe = banco.VerificarExistencia(email))

#FAZENDO LOGOFF NA SESSION
@bp_login.route('/logoff' , methods = ['GET'])
def logoff():
    if 'nome' not in session:
        Funcoes.criaLog(LogEnum.INFO, LogEnum.logoff, request.path, "sn", "Loggof realizado!")
    else:
        Funcoes.criaLog(LogEnum.INFO, LogEnum.logoff, request.path, session['nome'], "Loggof realizado!")
    #SERVE PARA LIMPAR UM VALOR INDIVIDUAL
    session.pop('nome' , None)
    #LIMPA TODA A SESSION
    session.clear()
    return redirect(url_for('login.login'))

#VALIDANDO SE O LOGIN EXISTE NA SESSION
def validarSessao(f):
    @wraps(f)
    #criando uma função aqui dentro do wraps
    def decorated_function(*args, **kwargs):
        if 'nome' not in session:
            Funcoes.criaLog(LogEnum.WARNING, LogEnum.redirect, request.path, "sn", "Tentativa de acesso sem Login!")
            return redirect(url_for('login.login', falhalogin = 1))
        else:
            return f(*args, **kwargs)
    #retornando a função que acabamos de criar
    return decorated_function
