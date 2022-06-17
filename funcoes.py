from datetime import datetime
from hashlib import sha3_256
import logging
from enum import Enum
from flask import render_template, session
from werkzeug.utils import redirect


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
            #print("iphone");
            return "mobile";            
        elif "android" in user_agent:            
            #print("android")
            return "mobile";            
        else:
            #print("desktop");
            return "desktop"
            

    @staticmethod
    def criaLog(tipo, status, rota, usuario, mensagem):
        #definindo as configurações basicas e o caminho do arquivo.
        
        logging.basicConfig(filename='arquivoLog.log',format=f'%(levelname)s|%(name)s|%(asctime)s|%(message)s',
                            datefmt='%d/%m/%Y %H:%M:%S', encoding='utf-8', level= logging.INFO)   
        #Criando a mensagem com os dados
        _msg = f'{status}|{rota}|{usuario}|{mensagem}'
        
        #Verificando o tipo para atribuição
        if tipo == LogEnum.INFO:
            logging.info(_msg)
        elif tipo == LogEnum.WARNING:
            logging.warning(_msg)
        elif tipo == LogEnum.ERROR:
            logging.error(_msg)
        elif tipo == LogEnum.DEBUG:
            logging.debug(_msg)
        elif tipo == LogEnum.CRITICAL:
            logging.critical(_msg)