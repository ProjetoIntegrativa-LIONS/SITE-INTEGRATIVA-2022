from functools import wraps
from flask import Blueprint, render_template , redirect , request, url_for, session, jsonify
from funcoes import Funcoes , LogEnum
from Diretorio_login.login import validarSessao

bp_admin = Blueprint('admin',__name__, url_prefix="/admin", template_folder= 'templates')

discionarioTelas = {
    'inicio' : 'inicio',
    'quemSomos' : 'quemSomos',
    'projetos' : 'projeto',
    'contato' : 'contato'
}

@bp_admin.route("/", methods = ['POST' , 'GET'] )
@validarSessao
def homeAdmin():
    tela = 1
    return render_template("InicioAdminDesktop.html" , tela=discionarioTelas.get('inicio'))


@bp_admin.route("/AdmQuemSomos" )
@validarSessao
def AdmQuemSomos():
    tela = 1
    return render_template("QuemSomosAdminDesktop.html", tela=discionarioTelas.get('quemSomos'))

@bp_admin.route("/AdmProjetos" )
@validarSessao
def AdmProjetos():
    tela = 1
    return render_template("ProjetosAdminDesktop.html", tela=discionarioTelas.get('projetos'))

@bp_admin.route("/AdmContato" )
@validarSessao
def AdmContato():
    tela = 1
    return render_template("ContatoAdminDesktop.html", tela=discionarioTelas.get('contato'))



    