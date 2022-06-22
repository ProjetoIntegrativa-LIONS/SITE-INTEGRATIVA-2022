from bancoDados import Banco

class QuemSomos():

    def __init__(self, id=0, titulo1="",texto1="",imagem2="",descricaoImagem2="",texto2="" ):
        self.id_quemSomos= id;
        self.titulo1= titulo1;
        self.texto1=texto1;
        self.imagem2=imagem2
        self.descricaoImagem2 = descricaoImagem2;
        self.texto2=texto2;

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
