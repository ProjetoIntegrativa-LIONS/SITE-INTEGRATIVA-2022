from bancoDados import Banco


class LogHistorico():

    def __init__(self, status="", rota="", usuario="", mensagem=""):
        self.status= status
        self.rota=rota;
        self.usuario=usuario;
        self.mensagem=mensagem;


class ControlLogHistorico():

    def __init__(self) :
        self.banco = Banco();

    def InserirLog(self, log):
        #GRAVAR O HISTORICO NO BANCO DE DADOS
        pass;
