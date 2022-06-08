from bancoDados import Banco

class Inicio():

    def __init__(self,id = 0, titulo = "", descricao = ""):
        self.id_inicio = id
        self.titulo_inicio = titulo;
        self.descricao_inicio = descricao;

    def ToString(self):
        return f"Id: {self.id_inicio}, titulo: {self.titulo_inicio}";

class ControlInicio():

    def __init__(self):
        self.banco = Banco();

    def SelectAll(self):    
        return self.banco.ExecutarComando("select * from tb_endereco")

    def SelectId(self, id_endereco):
        dados = self.banco.ExecutarComando("select * from tb_endereco where id_endereco = ?", [id_endereco] )
        pass
        #return Endereco(id_endereco=dados[0][0], cidade=dados[0][1], estado=dados[0][2],rua=dados[0][3],numero=dados[0][4])

    def Drop(self, id_endereco):
        return self.banco.ExecutarComando("delete from tb_endereco where id_endereco = ?" , [id_endereco])

    def Update(self, endereco):
        return self.banco.ExecutarComando("update tb_endereco set cidade = ?, estado = ?, rua = ?, numero = ? where id_endereco = ?", [endereco.cidade,endereco.estado,endereco.rua,endereco.numero, endereco.id_endereco])

    def LastInsert(self):
        return self.banco.ExecutarComando(sql=" select max( id_endereco ) from tb_endereco", parametros=[])

    def Insert(self, endereco):
        return self.banco.ExecutarComando("insert into tb_endereco (cidade, estado, rua, numero) values (?, ?, ?, ?);", [endereco.cidade,endereco.estado,endereco.rua,endereco.numero])
