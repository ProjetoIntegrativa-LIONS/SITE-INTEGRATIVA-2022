from flask import Blueprint, render_template , request, session

bp_home = Blueprint('home',__name__, url_prefix="/", template_folder= 'templates')

@bp_home.route("/")
def rotaHome():
    dispositivo = session['dispositivo']
    if dispositivo == "mobile":
        return render_template("homeDesktop.html")
    else:
        return render_template("homeMobile.html")