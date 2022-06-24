from hashlib import sha3_256
from flask import render_template, session

from Dominio_project.ControlLogHistorico import ControlLogHistorico, LogHistorico

class Funcoes(object):

    @staticmethod
    def cifrarSenha(senha):
        return sha3_256(senha.encode('utf-8')).hexdigest()

    @staticmethod
    def CarregarRota(caminhoDesktop, caminhoMobile, dados=""):
        dispositivo = session['dispositivo']
        if dispositivo == "desktop":
            return render_template(caminhoDesktop, dados=dados)
        else:
            return render_template(caminhoMobile, dados=dados)

    @staticmethod
    def PegarTipoDispositivo(user_agent):        
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return "mobile";            
        elif "android" in user_agent:            
            return "mobile";            
        else:
            return "desktop"
            
    @staticmethod
    def criaLog(status, rota, usuario, mensagem):
        log = LogHistorico(mensagem=mensagem,rota=rota,usuario=usuario,status=status);
        controlador = ControlLogHistorico();
        controlador.InserirLog(log);
