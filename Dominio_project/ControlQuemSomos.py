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

    def SelectId(self):
        id = 1;
        query="""
        select * from tb_quem_somos where id = %(novoId)s;
        """        
        dados = self.banco.ExecutarSelect(query, ({ 'novoId':id }));
        for dado in dados:
            quemsomos = QuemSomos(id=dado[0],titulo1=dado[1],texto1=dado[2],texto2=dado[3],descricaoImagem2=dado[4]);
        
        localImagem =  "assets/images/downloads/";
        localImagem+= quemsomos.descricaoImagem2;
        quemsomos.descricaoImagem2 = localImagem
        
        return quemsomos

    def Update(self, quemSomos):
        query = """
        UPDATE `tb_quem_somos`
        SET
            `titulo_1` = %(titulo)s,
            `texto1` = %(texto1)s,
            `texto_2` = %(texto2)s,
            `nome_imagem` = %(nomeImagem)s
        WHERE `id` = 1;
        """
        self.banco.ExecutarComando(query,( { 'titulo':quemSomos.titulo1, 'texto1':quemSomos.texto1,'texto2':quemSomos.texto2, 'nomeImagem':quemSomos.descricaoImagem2 } ));


    def UpdateSemImagem(self, quemSomos):
        query = """
        UPDATE `tb_quem_somos`
        SET
            `titulo_1` = %(titulo)s,
            `texto1` = %(texto1)s,
            `texto_2` = %(texto2)s
        WHERE `id` = 1;
        """
        self.banco.ExecutarComando(query,( { 'titulo':quemSomos.titulo1, 'texto1':quemSomos.texto1,'texto2':quemSomos.texto2 } ));

