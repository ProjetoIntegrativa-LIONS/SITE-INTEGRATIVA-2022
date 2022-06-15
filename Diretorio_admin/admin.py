from ast import Pass
from atexit import register
from functools import wraps
from pydoc import describe
from turtle import title
from flask import Blueprint, render_template , redirect , request, url_for, session, jsonify
from bancoDados import Banco
from funcoes import Funcoes , LogEnum
from Diretorio_login.login import validarSessao
from Dominio_project.ControlContatos import Contato, ControlContato
from Dominio_project.ControlInicio import  Inicio, ControlInicio
from Dominio_project.ControlProjeto import Projeto, ControlProjeto
from Dominio_project.ControlQuemSomos import QuemSomos, ControlQuemSomos


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
    registro = controlador.SelectId(id_inicio=1);        
    return render_template("InicioAdminDesktop.html" , registro = registro, tela=discionarioTelas.get('inicio'))

@bp_admin.route("/modificarInicio", methods = ['POST'] )
@validarSessao
def modificarInicio():    
    if request.method == "POST":
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        titulo2 = request.form['titulo2']
        imagem = request.files['arquivo-1']
        objetoInicio = Inicio(descricao=descricao,segundoTitulo=titulo2,titulo=titulo,imagem=imagem);
        #SALVAR NO BANCO DE DADOS aqui
    return redirect(url_for('admin.homeAdmin'));
#endregion

#region QUEM SOMOS ADMINISTRADOR

@bp_admin.route("/AdmQuemSomos" )
@validarSessao
def AdmQuemSomos():
    controlador = ControlQuemSomos();
    registro = controlador.SelectId(id=0);
    return render_template("QuemSomosAdminDesktop.html", registro = registro , tela=discionarioTelas.get('quemSomos'))

@bp_admin.route("/modificarQuemSomos", methods = ['POST'] )
@validarSessao
def modificarQuemSomos():
    if request.method == "POST":
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        titulo2 = request.form['titulo2']
        imagem = request.files['arquivo-1']
        objetoQuemSomos = QuemSomos(imagem=imagem,descricao=descricao,primeiroTitulo=titulo, segundoTitulo=titulo2);
        #SALVAR NO BANCO DE DADOS aqui
    return redirect(url_for('admin.AdmQuemSomos'));

#endregion

#region PROJETOS ADMINISTRADOS
@bp_admin.route("/AdmProjetos" )
@validarSessao
def AdmProjetos():
    controlador = ControlProjeto();
    registro = controlador.SelectAll();
    return render_template("ProjetosAdminDesktop.html", registro = registro ,tela=discionarioTelas.get('projetos'))

@bp_admin.route("/modificarProjeto", methods = ['POST'] )
@validarSessao
def modificarProjeto():
    if request.method == "POST":

        objetoProjeto = Projeto();
        #SALVAR NO BANCO DE DADOS

    return redirect(url_for('admin.AdmProjetos'));

@bp_admin.route("/deletarEditarProjeto",methods = ['POST'])
@validarSessao
def deletarEditarProjeto():
    tipo = request.form['tipo']
    idProjeto = request.form['id_projeto']   

    if tipo == "Adicionar Novo":
        pass;

    controlador = ControlProjeto();
    controlador.SelectId(id=idProjeto);

    if tipo =="Editar":
        pass;
    if tipo =="Excluir":
        pass;

    return redirect(url_for('admin.AdmProjetos'));

#endregion

#region CONTATO ADMINISTRADOR
@bp_admin.route("/AdmContato" )
@validarSessao
def AdmContato():
    
    return render_template("ContatoAdminDesktop.html", tela=discionarioTelas.get('contato'))

#endregion


    