from flask import Blueprint, render_template
from Dominio_project.ControlInicio import ControlInicio

bp_home = Blueprint('home',__name__, url_prefix="/", template_folder= 'templates')

@bp_home.route("/")
def rotaHome():
    nomeTela = "inicio"
    controlador = ControlInicio();
    dados = controlador.SelectInicio();
    return render_template("homeDesktop.html", dados=dados, tela=nomeTela)
