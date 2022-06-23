from bancoDados import Banco

class Contato():

    def __init__(self, id=0,nome ="",telefone="", email="", motivo="", descricao=""):
        self.id = id;
        self.nome = nome;
        self.telefone= telefone
        self.email = email;
        self.motivo = motivo;
        self.descricao = descricao;

    def ToString(self):
        return f"Id: {self.id_contato}, Nome: {self.nome_contato}, Telefone: {self.telefone_contato}";
 
class ControlContato():

    def __init__(self):
        self.banco = Banco();

    def SelectAll(self):            
        dados = self.banco.ExecutarSelect("select * from tb_contato;");
        listaContato = []
        for dado in dados:
            contato = Contato(id=dado[0],nome=dado[1],telefone=dado[2],email=dado[3],motivo=dado[4],descricao=dado[5])
            listaContato.append(contato);
        return listaContato;        
    
    def InsertContato(self, contato):
        pass;
        