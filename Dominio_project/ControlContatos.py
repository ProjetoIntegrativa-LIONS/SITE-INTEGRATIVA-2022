from bancoDados import Banco

class Contato():

    def __init__(self, id=0,nome ="",telefone=""):
        self.id_contato = id;
        self.nome_contato = nome;
        self.telefone_contato = telefone

    def ToString(self):
        return f"Id: {self.id_contato}, Nome: {self.nome_contato}, Telefone: {self.telefone_contato}";

class ControlContato():

    def __init__(self):
        self.banco = Banco();

    def SelectAll(self):    
        return ""
        
    def selectName(self, nome):
        return ""
    
    def SelectId(self, contatoId):
        return ""

    def Drop(self, contatoId):
        return ""
