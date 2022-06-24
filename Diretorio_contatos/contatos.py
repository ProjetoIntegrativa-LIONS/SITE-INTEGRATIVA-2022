from flask import Blueprint, render_template , redirect , request, url_for, session, jsonify
from funcoes import Funcoes , LogEnum
from Dominio_project.ControlContatos import Contato,ControlContato

bp_contatos = Blueprint('contatos',__name__, url_prefix="/contatos", template_folder= 'templates')

@bp_contatos.route("/" )
def contatos():
    nomeTela = "contato"
    controlador = ControlContato();
    dados = controlador.SelectAll();
    return render_template("contatosDesktop.html", dados=dados, tela=nomeTela)
    # return Funcoes.CarregarRota(caminhoDesktop="contatosDesktop.html",caminhoMobile="contatosMobile.html", dados=dados)

@bp_contatos.route("/cadastrarContato",methods = ['POST'] )
def cadastrarContato():
    if request.method == "POST":        
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        motivo = request.form['motivo']
        descricao = request.form['descricao']
        contato = Contato(descricao=descricao,email=email,telefone=telefone,motivo=motivo,nome=nome);
        controlador = ControlContato();
        controlador.InsertContato(contato=contato);
        print("contato inserido")
    return redirect(url_for('contatos.contatos'));

