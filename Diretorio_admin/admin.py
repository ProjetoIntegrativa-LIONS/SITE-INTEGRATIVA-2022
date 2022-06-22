from asyncio.windows_events import NULL
from datetime import datetime
from flask import Blueprint, render_template , redirect , request, url_for, session, jsonify
from Diretorio_login.login import validarSessao
from Dominio_project.ControlContatos import Contato, ControlContato
from Dominio_project.ControlInicio import  Inicio, ControlInicio
from Dominio_project.ControlProjeto import Projeto, ControlProjeto
from Dominio_project.ControlQuemSomos import QuemSomos, ControlQuemSomos
import os

bp_admin = Blueprint('admin',__name__, url_prefix="/admin", template_folder= 'templates')

discionarioTelas = {
    'inicio' : 'inicio',
    'quemSomos' : 'quemSomos',
    'projetos' : 'projeto',
    'contato' : 'contato'
}

#region INICIO ADMINISTRADOR
@bp_admin.route("/", methods = ['POST' , 'GET'] )
@validarSessao
def homeAdmin():
    controlador = ControlInicio();    
    registro = controlador.SelectInicio();        
    return render_template("CadastroInicioAdminDesktop.html" , registro = registro, tela=discionarioTelas.get('inicio'))

@bp_admin.route("/modificarInicio", methods = ['POST'] )
@validarSessao
def modificarInicio():    
    if request.method == "POST":
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        titulo2 = request.form['titulo2']
        imagem = request.files['arquivo-1']

        #DIRETORIO = url_for('static', filename='assets/imagens/downloads')
        DIRETORIO = "static\\assets\\images\\downloads"
        print(DIRETORIO)
        print(imagem.content_type)
        
        nome_do_arquivo = "NOME"
        imagem.save(os.path.join(DIRETORIO, nome_do_arquivo))
        #objetoInicio = Inicio(descricao=descricao,segundoTitulo=titulo2,titulo=titulo,imagem=imagem);



        #SALVAR NO BANCO DE DADOS aqui
    return redirect(url_for('admin.homeAdmin'));
#endregion

#region QUEM SOMOS ADMINISTRADOR

@bp_admin.route("/AdmQuemSomos" )
@validarSessao
def AdmQuemSomos():
    controlador = ControlQuemSomos();
    registro = controlador.SelectId(id=0);
    return render_template("CadastroQuemSomosAdminDesktop.html", registro = registro , tela=discionarioTelas.get('quemSomos'))

@bp_admin.route("/modificarQuemSomos", methods = ['POST'] )
@validarSessao
def modificarQuemSomos():
    if request.method == "POST":
        titulo1 = request.form['titulo1']
        texto1 = request.form['texto1']
        texto2 = request.form['texto2']
        imagem2 = request.files['arquivo-2']
        descicaoImagem = imagem2.content_length;
        print(descicaoImagem);

        objetoQuemSomos = QuemSomos(descricaoImagem2="",imagem2=imagem2,texto1=texto1,texto2=texto2,titulo1=titulo1,id=0);

        #SALVAR NO BANCO DE DADOS aqui
    return redirect(url_for('admin.AdmQuemSomos'));

#endregion

#region PROJETOS ADMINISTRADOS
@bp_admin.route("/AdmProjetos" )
@validarSessao
def AdmProjetos():
    controlador = ControlProjeto();
    registro = controlador.SelectAll();
    return render_template("ViewProjetosAdminDesktop.html", registro = registro ,tela=discionarioTelas.get('projetos'))

@bp_admin.route("/telaCadastroProjetos")
@validarSessao
def telaCadastroProjetos(id):
    print(id);
    controlador = ControlProjeto();
    if id == 0:
        projeto = Projeto(nome="",descricao="",data="",id=0, imagem="");
    else:
        projeto = controlador.SelectId(id);

    print(projeto.descricao)
    print(projeto.nome)
    return render_template("CadastroProjetosAdminDesktop.html", dados = projeto ,tela=discionarioTelas.get('projetos'))

@bp_admin.route("/cadastroEmBancoDeProjeto", methods = ['POST'] )
@validarSessao
def cadastroEmBancoDeProjeto():
    if request.method == "POST":
        
        id = request.form['id_projeto']
        titulo = request.form['titulo']
        descricao = request.form['descricao']        
        imagem = request.files['arquivo-1']

        objetoProjeto = Projeto(data=datetime.now(),titulo=titulo,descricao=descricao,imagem=imagem,id=id);

        banco = ControlProjeto();
        if id== 0:
            banco.Insert(objetoProjeto);
        if id != 0:
            banco.Update(projeto=objetoProjeto);

    return redirect(url_for('admin.AdmProjetos'));

@bp_admin.route("/deletarEditarInserirProjeto",methods = ['POST'])
@validarSessao
def deletarEditarInserirProjeto():
    tipo = request.form['tipo']
    idProjeto = request.form['id_projeto']   

    if tipo == "Adicionar Novo":
        return telaCadastroProjetos(id=0);        

    if tipo =="Editar":
        return telaCadastroProjetos(id=idProjeto);

    if tipo =="Excluir":
        banco = ControlProjeto();
        banco.Drop(idProjeto);
        print("Dropou o projeto")

    return redirect(url_for('admin.AdmProjetos'));
#endregion

#region CONTATO ADMINISTRADOR
@bp_admin.route("/AdmContato" )
@validarSessao
def AdmContato():
    controlador = ControlContato();
    dados = controlador.SelectAll();
    return render_template("ViewContatoAdminDesktop.html",dados=dados, tela=discionarioTelas.get('contato'))

@bp_admin.route("/visualizarContato", methods = ['POST'])
@validarSessao
def visualizarContato():
    if request.method == "POST":
        id = request.form['id']
        controlador = ControlContato();
        contato = controlador.SelectId(contatoId=id);
        if(contato == NULL):
            return redirect(url_for('admin.AdmContato'))
        else:
            return render_template("ViewContatoUnicoAdminDesktop.html",dados=contato, tela=discionarioTelas.get('contato'))
#endregion


    