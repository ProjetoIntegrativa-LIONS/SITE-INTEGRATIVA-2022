import imp
from flask import Blueprint, render_template , request, session
from Dominio_project.ControlProjeto import Projeto,ControlProjeto
from funcoes import Funcoes

bp_projetos = Blueprint('projetos',__name__, url_prefix="/projetos", template_folder= 'templates')

@bp_projetos.route("/")
def projetos():
    nomeTela = "projetos"
    controlador = ControlProjeto();
    dados = controlador.SelectAll();    
    return render_template("projetosDesktop.html", dados=dados, tela=nomeTela)
    # return Funcoes.CarregarRota(caminhoDesktop= "projetosDesktop.html",caminhoMobile="projetosMobile.html",dados=dados)