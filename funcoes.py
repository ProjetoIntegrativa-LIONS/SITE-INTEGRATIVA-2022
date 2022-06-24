from datetime import datetime
from hashlib import sha3_256
from enum import Enum
from flask import render_template, session

from Dominio_project.ControlLogHistorico import ControlLogHistorico, LogHistorico


class LogEnum(Enum):
    INFO='INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    DEBUG = 'DEBUG'
    CRITICAL = 'CRITICAL'
    login = 'login'
    falhaLogin = 'falha login'
    logoff = 'logoff'
    excecao = 'exceção'
    save = 'salvando informações'
    redirect = 'redirecionamento'
    load = 'carregamento dados'
    sqlInsert = 'Insert'
    sqlupdate = 'Update'
    sqldelete = 'Delete'
    sqlSelect = 'Select'
    banco = 'comando banco'

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
