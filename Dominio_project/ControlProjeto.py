from datetime import datetime
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
            projeto = Projeto(id=dado[0],nome=dado[1],descricao=dado[2],data=dado[3],descricaoImagem=dado[4]);
            localImagem =  "assets/images/downloads/";
            localImagem+= projeto.descricaoImagem;
            projeto.descricaoImagem = localImagem
            listaProjeto.append(projeto);

        return listaProjeto;
        
    def SelectId(self, id):
        query = """
            SELECT *
            FROM `tb_projeto` where `id` = %(id)s; """
        dados = self.banco.ExecutarSelect(query,({'id':id }));

        for dado in dados:
            projeto = Projeto(id=dado[0],nome=dado[1],descricao=dado[2],data=dado[3],descricaoImagem=dado[4]);
            localImagem =  "assets/images/downloads/";
            localImagem+= projeto.descricaoImagem;
            projeto.descricaoImagem = localImagem

        return projeto;        


    def Drop(self, id):
        query = """
            DELETE FROM `tb_projeto`
            WHERE id = %(id)s;
        """
        self.banco.ExecutarComando(query, ({'id':id }));

    def UpdateSemImagem(self, projeto):
        query = """
                UPDATE `tb_projeto`
                    SET
                    `titulo` = %(titulo)s,
                    `descricao` = %(descricao)s,
                    `data` = %(data)s
                WHERE `id` = %(id)s;"""
        self.banco.ExecutarComando(query, ({'id':projeto.id ,'titulo':projeto.nome,'descricao':projeto.descricao,'data':projeto.data}));

    def Update(self, projeto):
            query = """
                UPDATE `tb_projeto`
                    SET
                    `titulo` = %(titulo)s,
                    `descricao` = %(descricao)s,
                    `data` = %(data)s,
                    `nome_imagem` = %(imagem)s
                WHERE `id` = %(id)s;"""
            self.banco.ExecutarComando(query, ({'id':projeto.id ,'titulo':projeto.nome,'descricao':projeto.descricao,'data':projeto.data, 'imagem':projeto.descricaoImagem}));



    def Insert(self, projeto):
        query = """INSERT INTO `tb_projeto`
            (`titulo`, `descricao`, `data`, `nome_imagem`)
            VALUES
            (%(titulo)s , %(descricao)s, %(data)s, %(imagem)s); """
        projeto.data = datetime.now();
        
        self.banco.ExecutarComando(query,({'titulo':projeto.nome,'descricao':projeto.descricao,'data':projeto.data, 'imagem':projeto.descricaoImagem}));

