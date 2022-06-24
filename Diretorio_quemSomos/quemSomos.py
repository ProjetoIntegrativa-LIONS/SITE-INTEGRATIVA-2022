from functools import wraps
import imp
from flask import Blueprint, render_template , redirect , request, url_for, session, jsonify
from funcoes import Funcoes , LogEnum
from Dominio_project.ControlQuemSomos import QuemSomos,ControlQuemSomos
bp_quemSomos = Blueprint('quemSomos',__name__, url_prefix="/quemSomos", template_folder= 'templates')

@bp_quemSomos.route("/" )
def quemSomos():
    nomeTela = "quemSomos"
    controlador = ControlQuemSomos()
    dados = controlador.SelectId();
    return render_template("QuemSomosDesktop.html", dados=dados, tela=nomeTela)
    # return Funcoes.CarregarRota('QuemSomosDesktop.html', 'QuemSomosMobile.html',dados=dados)    