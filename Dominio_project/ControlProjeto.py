from bancoDados import Banco

class Projeto():

    def __init__(self, id =0, nome ="", descricao = "") :
        self.id_projeto = id;
        self.nome_projeto = nome;
        self.descricao_projeto= descricao;

    def ToString(self):
        return f"Id: {self.id_projeto}, Nome: {self.nome_projeto}";


class ControlProjeto():

    def __init__(self) :
        self.banco = Banco();

    def SelectAll(self):    
        return self.banco.ExecutarComando("select * from tb_endereco")
        
    def SelectId(self):
        pass

    def Drop(self):
        pass

    def Update(self):
        pass

    def Insert(self):
        return self.banco.ExecutarComando("insert into tb_endereco (cidade, estado, rua, numero) values (?, ?, ?, ?)", ["lages","SC","Miranda","SN"])