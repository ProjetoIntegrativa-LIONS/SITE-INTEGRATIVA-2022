from bancoDados import Banco

class QuemSomos():

    def __init__(self, id=0, descricao ="", primeiroTitulo ="",segundoTitulo="",imagem =""):
        self.id_quemSomos= id;
        self.descricao = descricao;
        self.primeiroTitulo = primeiroTitulo;
        self.segundoTitulo = segundoTitulo;
        self.imagem = imagem;

    def ToString(self):
        return f"Id: {self.id_quemSomos}, descricao: {self.descricao_quemSomos}";

class ControlQuemSomos():

    def __init__(self,):
        self.banco = Banco();

    def SelectAll(self):    
        pass

    def SelectId(self, id):
        #dados = self.banco.ExecutarComando("select * from tb_endereco where id_endereco = ?", [id_endereco] )        
        #return Endereco(id_endereco=dados[0][0], cidade=dados[0][1], estado=dados[0][2],rua=dados[0][3],numero=dados[0][4])
        return QuemSomos(descricao="Descricao",segundoTitulo="Segundo titulo",primeiroTitulo="Primeiro titulo",id=0);

    def Drop(self):
        pass

    def Update(self):
        pass

    def Insert(self):
        pass
