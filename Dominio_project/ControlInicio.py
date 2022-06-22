from bancoDados import Banco

class Inicio():

    def __init__(self,id = 0, imagem1="",descricaoImagem1="",texto1="",titulo2="",texto2="",texto3="",imagem3="",descricaoImagem3="",):
        self.id_inicio = id;
        self.imagem1= imagem1;
        self.descricaoImagem1=descricaoImagem1;
        self.texto1=texto1;
        self.titulo2 = titulo2;
        self.texto2 = texto2;
        self.texto3 = texto3;
        self.imagem3 = imagem3;
        self.descricaoImagem3 = descricaoImagem3;

class ControlInicio():

    def __init__(self):
        self.banco = Banco();
    
    def SelectInicio(self):
        #dados = self.banco.ExecutarComando("select * from tb_endereco where id_endereco = ?", [id_endereco] )        
        #return Endereco(id_endereco=dados[0][0], cidade=dados[0][1], estado=dados[0][2],rua=dados[0][3],numero=dados[0][4])
        return Inicio(id=1,imagem1="",descricaoImagem1="",texto1="",texto2="",texto3="",descricaoImagem3="",imagem3="",titulo2="");

    def Drop(self, id_endereco):
        return self.banco.ExecutarComando("delete from tb_endereco where id_endereco = ?" , [id_endereco])

    def Update(self, endereco):
        return self.banco.ExecutarComando("update tb_endereco set cidade = ?, estado = ?, rua = ?, numero = ? where id_endereco = ?", [endereco.cidade,endereco.estado,endereco.rua,endereco.numero, endereco.id_endereco])

    def LastInsert(self):
        return self.banco.ExecutarComando(sql=" select max( id_endereco ) from tb_endereco", parametros=[])

    def Insert(self, endereco):
        return self.banco.ExecutarComando("insert into tb_endereco (cidade, estado, rua, numero) values (?, ?, ?, ?);", [endereco.cidade,endereco.estado,endereco.rua,endereco.numero])
