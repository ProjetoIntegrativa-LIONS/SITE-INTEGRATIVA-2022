from flask import Blueprint, render_template , request, session
from Dominio_project.ControlInicio import Inicio,ControlInicio
from funcoes import Funcoes

bp_home = Blueprint('home',__name__, url_prefix="/", template_folder= 'templates')

@bp_home.route("/")
def rotaHome():
    controlador = ControlInicio();
    dados = controlador.SelectInicio();
    return Funcoes.CarregarRota(caminhoDesktop="homeDesktop.html",caminhoMobile="homeMobile.html", dados=dados)