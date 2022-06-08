from bancoDados import Banco

class QuemSomos():

    def __init__(self, id=0, descricao =""):
        self.id_quemSomos= id;
        self.descricao_quemSomos = descricao;

    def ToString(self):
        return f"Id: {self.id_quemSomos}, descricao: {self.descricao_quemSomos}";

class ControlQuemSomos():

    def __init__(self,):
        self.banco = Banco();

    def SelectAll(self):    
        pass

    def SelectId(self):
        pass

    def Drop(self):
        pass

    def Update(self):
        pass

    def Insert(self):
        pass
