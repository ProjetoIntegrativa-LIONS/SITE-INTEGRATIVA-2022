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
        id = 1
        query="""
            SELECT * FROM `tb_inicio` WHERE id = %(id)s;
        """
        dados = self.banco.ExecutarSelect(query, ({'id':id }));

        for dado in dados:
            inicio = Inicio(imagem1="",imagem3="",id=1,texto1=dado[1],titulo2=dado[2],texto2=dado[3],texto3=dado[4],descricaoImagem1=dado[5],descricaoImagem3=dado[6]);
            localImagem1 =  "assets/images/downloads/";
            localImagem2=  "assets/images/downloads/";
            localImagem1+= inicio.descricaoImagem1;
            localImagem2+= inicio.descricaoImagem3;
            inicio.descricaoImagem1 = localImagem1
            inicio.descricaoImagem3 = localImagem2
        return inicio;        

    def Update(self, inicio):
        query = """
            UPDATE `tb_inicio` 
                SET 
            `texto1`= %(texto1)s ,`titulo_2`= %(titulo_2)s ,`texto_2`= %(texto_2)s ,
            `texto_3`= %(texto_3)s ,`nome_imagem1`= %(nome_imagem1)s ,`nome_imagem2`= %(nome_imagem2)s 
                WHERE %(id)s
        """
        self.banco.ExecutarComando(query,( { 'texto1':inicio.texto1,'titulo_2': inicio.titulo2,'texto_2':inicio.texto2,'texto_3':inicio.texto3,'nome_imagem1':inicio.descricaoImagem1,'nome_imagem2':inicio.descricaoImagem3,'id':inicio.id_inicio } ))
