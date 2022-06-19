from bancoDados import Banco

class Contato():

    def __init__(self, id=0,nome ="",telefone="", email="", motivo="", descricao=""):
        self.id = id;
        self.nome = nome;
        self.telefone= telefone
        self.email = email;
        self.motivo = motivo;
        self.descricao = descricao;

    def ToString(self):
        return f"Id: {self.id_contato}, Nome: {self.nome_contato}, Telefone: {self.telefone_contato}";
 
class ControlContato():

    def __init__(self):
        self.banco = Banco();

    def SelectAll(self):    
        listaContato = [];        
        listaContato.append(Contato(id=1,nome="CONTATO 1",telefone="48 89239-8877",descricao="Descricao do contato 1",email="Leonardo@gmai.com",motivo="Qualquer motivo 1"));
        listaContato.append(Contato(id=2,nome="CONTATO 2",telefone="49 79239-6655",descricao="Descricao do contato 2",email="Leonardo@gmai.com",motivo="Qualquer motivo 2"));
        listaContato.append(Contato(id=3,nome="CONTATO 3",telefone="47 99239-4455",descricao="Descricao do contato 3",email="Leonardo@gmai.com",motivo="Qualquer motivo 3"));
        listaContato.append(Contato(id=4,nome="CONTATO 4",telefone="46 69239-8834",descricao="Descricao do contato 4",email="Leonardo@gmai.com",motivo="Qualquer motivo 4"));
        return listaContato;        
    
    def InsertContato(self, contato):
        pass;
        
    def SelectId(self, contatoId):
        return Contato(id=contatoId,nome="CONTATO 1",telefone="48 89239-8877",descricao="Descricao do contato 1",email="Leonardo@gmai.com",motivo="Qualquer motivo 1")

    def Drop(self, contatoId):
        return ""
