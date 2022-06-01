from dis import dis
from flask import Flask , render_template,  session, request
from datetime import timedelta
import os

from Diretorio_home.home import bp_home
from funcoes import Funcoes
#from dir_login.login import bp_login

app = Flask(__name__) 

app.secret_key = os.urandom(12).hex()

app.register_blueprint(bp_home)




@app.errorhandler(404)
def rotaErro404(error):
    return render_template("form_404.html"), 404

#Antes do primeiro request
@app.before_first_request
def before_request():
    session.permanent = True
    user_agent = request.headers.get('User-Agent')
    dispositivo = Funcoes.PegarTipoDispositivo(user_agent)    
    session['dispositivo'] = dispositivo
    print(dispositivo)   


if __name__ == "__main__":
    app.run(debug= True, port= 5000)
