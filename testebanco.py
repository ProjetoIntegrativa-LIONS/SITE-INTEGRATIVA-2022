from bancoDados import Banco


print("asdasdasd")
banco = Banco()
print("asdasdasd")
valor = 1
dados = banco.ExecutarSelect("SELECT * FROM tb_contato where id= %(valor)s;" , ( {'valor':valor,} ));
query = """
INSERT INTO `tb_contato`
(`nome`,`telefone`,`email`,`motivo`,`descricao`)
VALUES
(%(nome)s, %(telefone)s,%(email)s,%(motivo)s,%(descicao)s )"""

banco.ExecutarComando(query, ( {'nome':"novo nome",'telefone':"47992123123",'email':"leonardo@gmail.com",'motivo':"nada a ver",'descicao':"Descricaonada a ver" } ));

print(dados)