from datetime import datetime
from re import I
from tkinter.messagebox import RETRY
from xmlrpc.client import DateTime
from bancoDados import Banco

class Projeto():

    def __init__(self, id =0, nome ="", descricao = "", data="") :
        self.id = id;
        self.nome = nome;
        self.descricao= descricao;
        self.data = data;

    def ToString(self):
        return f"Id: {self.id}, Nome: {self.nome}";


class ControlProjeto():
 
    def __init__(self) :
        self.banco = Banco();

    def SelectAll(self):    
        listaProjeto = [];
        dat = datetime.now()
        
        #DEVE BUSCAR OS DADOS DO BANCO DADOS
        listaProjeto.append(Projeto(descricao="descricao 1",nome="PROJETO 1",id=1,data= datetime.now()));
        listaProjeto.append(Projeto(descricao="descricao 2",nome="PROJETO 2",id=2,data= datetime.now()));
        listaProjeto.append(Projeto(descricao="descricao 3",nome="PROJETO 3",id=3,data= datetime.now()));
        listaProjeto.append(Projeto(descricao="descricao 4",nome="PROJETO 4",id=4,data= datetime.now()));

        return listaProjeto;
        #return self.banco.ExecutarComando("select * from tb_endereco")
        
    def SelectId(self, id):
        return Projeto(descricao="descricao 1",nome="TESTE 1",id=1)


    def Drop(self):
        pass

    def Update(self):
        pass

    def Insert(self):
        return self.banco.ExecutarComando("insert into tb_endereco (cidade, estado, rua, numero) values (?, ?, ?, ?)", ["lages","SC","Miranda","SN"])