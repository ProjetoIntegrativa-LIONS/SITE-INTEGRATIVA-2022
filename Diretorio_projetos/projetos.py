from flask import Blueprint, render_template , request, session

from funcoes import Funcoes

bp_projetos = Blueprint('projetos',__name__, url_prefix="/projetos", template_folder= 'templates')

@bp_projetos.route("/")
def projetos():
    return Funcoes.CarregarRota(caminhoDesktop= "projetosDesktop.html",caminhoMobile="projetosMobile.html")