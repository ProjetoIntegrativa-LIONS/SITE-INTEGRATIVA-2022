from flask import Blueprint, render_template , redirect , request
from funcoes import Funcoes 
from Dominio_project.ControlQuemSomos import QuemSomos,ControlQuemSomos
bp_quemSomos = Blueprint('quemSomos',__name__, url_prefix="/quemSomos", template_folder= 'templates')

@bp_quemSomos.route("/" )
def quemSomos():
    controlador = ControlQuemSomos()
    dados = controlador.SelectId();
    return Funcoes.CarregarRota('QuemSomosDesktop.html', 'QuemSomosMobile.html',dados=dados)    