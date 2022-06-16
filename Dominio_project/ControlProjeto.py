from datetime import datetime
from re import I
from tkinter.messagebox import RETRY
from xmlrpc.client import DateTime
from bancoDados import Banco

class Projeto():

    def __init__(self, id =0, nome ="", descricao = "", data="", imagem="") :
        self.id = id;
        self.nome = nome;
        self.descricao= descricao;
        self.data = data;
        self.imagem = imagem;

    def ToString(self):
        return f"Id: {self.id}, Nome: {self.nome}";


class ControlProjeto():
 
    def __init__(self) :
        self.banco = Banco();

    def SelectAll(self):    
        listaProjeto = [];        
        #DEVE BUSCAR OS DADOS DO BANCO DADOS
        listaProjeto.append(Projeto(descricao="descricao 1",nome="PROJETO 1",id=1,data= datetime.now()));
        listaProjeto.append(Projeto(descricao="descricao 2",nome="PROJETO 2",id=2,data= datetime.now()));
        listaProjeto.append(Projeto(descricao="descricao 3",nome="PROJETO 3",id=3,data= datetime.now()));
        listaProjeto.append(Projeto(descricao="descricao 4",nome="PROJETO 4",id=4,data= datetime.now()));

        return listaProjeto;
        
    def SelectId(self, id):
        #SELECIONAR UM REGISTRO DO BANCO
        return Projeto(descricao="descricao 1",nome="TESTE 1",id=1,data=datetime.now(),imagem="")


    def Drop(self, id):
        #DELETAR REGISTRO DO BANCO
        pass

    def Update(self, projeto):
        #ATUALIZAR REGISTRO DO BANCO
        pass

    def Insert(self, projeto):
        #INSERIR UM NOVO REGISTRO NO BANCO
        pass;
