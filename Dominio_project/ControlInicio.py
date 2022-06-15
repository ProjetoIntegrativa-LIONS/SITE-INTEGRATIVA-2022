from bancoDados import Banco

class Inicio():

    def __init__(self,id = 0, titulo = "", descricao = "", segundoTitulo="", imagem=""):
        self.id_inicio = id
        self.titulo_inicio = titulo;
        self.descricao_inicio = descricao;
        self.segundo_titulo = segundoTitulo;
        self.imagem = imagem;

    def ToString(self):
        return f"Id: {self.id_inicio}, titulo: {self.titulo_inicio}";

class ControlInicio():

    def __init__(self):
        self.banco = Banco();
    
    def SelectId(self, id_inicio):
        #dados = self.banco.ExecutarComando("select * from tb_endereco where id_endereco = ?", [id_endereco] )        
        #return Endereco(id_endereco=dados[0][0], cidade=dados[0][1], estado=dados[0][2],rua=dados[0][3],numero=dados[0][4])
        return Inicio(id=1,titulo="PRIMEIRO titulo",descricao="PRIMEIRa descricao",segundoTitulo="SEGUNDO TITULO");

    def Drop(self, id_endereco):
        return self.banco.ExecutarComando("delete from tb_endereco where id_endereco = ?" , [id_endereco])

    def Update(self, endereco):
        return self.banco.ExecutarComando("update tb_endereco set cidade = ?, estado = ?, rua = ?, numero = ? where id_endereco = ?", [endereco.cidade,endereco.estado,endereco.rua,endereco.numero, endereco.id_endereco])

    def LastInsert(self):
        return self.banco.ExecutarComando(sql=" select max( id_endereco ) from tb_endereco", parametros=[])

    def Insert(self, endereco):
        return self.banco.ExecutarComando("insert into tb_endereco (cidade, estado, rua, numero) values (?, ?, ?, ?);", [endereco.cidade,endereco.estado,endereco.rua,endereco.numero])
