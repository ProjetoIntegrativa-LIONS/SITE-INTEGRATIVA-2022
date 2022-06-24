from flask import Blueprint, render_template 
from Dominio_project.ControlProjeto import Projeto,ControlProjeto

bp_projetos = Blueprint('projetos',__name__, url_prefix="/projetos", template_folder= 'templates')

@bp_projetos.route("/")
def projetos():
    nomeTela = "projetos"
    controlador = ControlProjeto();
    dados = controlador.SelectAll();    
    return render_template("projetosDesktop.html", dados=dados, tela=nomeTela)
