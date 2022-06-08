from functools import wraps
from flask import Blueprint, render_template , redirect , request, url_for, session, jsonify
from funcoes import Funcoes , LogEnum

bp_quemSomos = Blueprint('quemSomos',__name__, url_prefix="/quemSomos", template_folder= 'templates')

@bp_quemSomos.route("/" )
def quemSomos():
    return render_template('QuemSomos.html')