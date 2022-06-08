from functools import wraps
from flask import Blueprint, render_template , redirect , request, url_for, session, jsonify
from funcoes import Funcoes , LogEnum
from Diretorio_login.login import validarSessao

bp_admin = Blueprint('admin',__name__, url_prefix="/admin", template_folder= 'templates')


@bp_admin.route("/", methods = ['POST' , 'GET'] )
@validarSessao
def homeAdmin():
    return render_template("baseAdminDesktop.html" , falhalogin = 0)
