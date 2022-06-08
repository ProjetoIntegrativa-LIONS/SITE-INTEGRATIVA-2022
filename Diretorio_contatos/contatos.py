from functools import wraps
from flask import Blueprint, render_template , redirect , request, url_for, session, jsonify
from funcoes import Funcoes , LogEnum

bp_contatos = Blueprint('contatos',__name__, url_prefix="/contatos", template_folder= 'templates')

@bp_contatos.route("/" )
def contatos():
    return Funcoes.CarregarRota(caminhoDesktop="contatosDesktop.html",caminhoMobile="contatosMobile.html")