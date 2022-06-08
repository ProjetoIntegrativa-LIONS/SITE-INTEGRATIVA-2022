from flask import Blueprint, render_template , request, session

bp_projetos = Blueprint('projetos',__name__, url_prefix="/projetos", template_folder= 'templates')

@bp_projetos.route("/")
def projetos():
    dispositivo = session['dispositivo']
    if dispositivo == "desktop":
        return render_template("projetosDesktop.html")
    else:
        return render_template("projetosMobile.html")