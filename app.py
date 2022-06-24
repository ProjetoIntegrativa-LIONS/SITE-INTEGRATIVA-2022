from flask import Flask , render_template,  session, request
import os

from Diretorio_home.home import bp_home
from Diretorio_projetos.projetos import bp_projetos
from Diretorio_login.login import bp_login
from Diretorio_admin.admin import bp_admin
from Diretorio_quemSomos.quemSomos import bp_quemSomos
from Diretorio_contatos.contatos import bp_contatos
from funcoes import Funcoes


app = Flask(__name__) 
application = app

app.secret_key = os.urandom(12).hex()

app.register_blueprint(bp_home)
app.register_blueprint(bp_projetos)
app.register_blueprint(bp_login)
app.register_blueprint(bp_admin)
app.register_blueprint(bp_quemSomos)
app.register_blueprint(bp_contatos)

@app.errorhandler(404)
def rotaErro404(error):
    return render_template("form_404.html"), 404

#Antes do primeiro request
@app.before_request
def before_request():
    session.permanent = True
    user_agent = request.headers.get('User-Agent')    
    session['dispositivo'] = Funcoes.PegarTipoDispositivo(user_agent)    


if __name__ == "__main__":
    app.run(debug= True, port= 5000)
