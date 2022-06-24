from datetime import datetime
from xmlrpc.client import DateTime
from bancoDados import Banco

class Projeto():

    def __init__(self, id =0, nome ="", descricao = "", data="", imagem="", descricaoImagem="") :
        self.id = id;
        self.nome = nome;
        self.descricao= descricao;
        self.data = data;
        self.imagem = imagem;
        self.descricaoImagem = descricaoImagem;

class ControlProjeto():
 
    def __init__(self) :
        self.banco = Banco();

    def SelectAll(self):    
        listaProjeto = [];        
        query = """
            SELECT *
            FROM `tb_projeto`; """
        dados = self.banco.ExecutarSelect(query,());
        for dado in dados:
            projeto = Projeto(id=dado[0],nome=dado[0],descricao=dado[0],data=dado[0]);
            listaProjeto.append(projeto);

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
        query = """
        
        """
        self.banco.ExecutarComando(query,({}));

