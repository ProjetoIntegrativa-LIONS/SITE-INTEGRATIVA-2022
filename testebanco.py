from Dominio_project.ControlContatos import Contato
from bancoDados import Banco


print("asdasdasd")
banco = Banco()
print("asdasdasd")
valor = 1

query = """ SELECT * FROM tb_contato where id = %(novoId)s ;"""
dado = banco.ExecutarSelect(query, ( {'novoId': 4} ));

contato = Contato(id=dado[0],nome=dado[1],telefone=dado[2],email=dado[3],motivo=dado[4],descricao=dado[5])




dados = banco.ExecutarSelect("select * from tb_contato");
listaContato = []

for dado in dados:
    contato = Contato(id=dado[0],nome=dado[1],telefone=dado[2],email=dado[3],motivo=dado[4],descricao=dado[5])
    listaContato.append(contato);

print(listaContato)




dados = banco.ExecutarSelect("SELECT * FROM tb_contato where id= %(valor)s;" , ( {'valor':valor,} ));
query = """
INSERT INTO `tb_contato`
(`nome`,`telefone`,`email`,`motivo`,`descricao`)
VALUES
(%(nome)s, %(telefone)s,%(email)s,%(motivo)s,%(descicao)s )"""

banco.ExecutarComando(query, ( {'nome':"novo nome",'telefone':"47992123123",'email':"leonardo@gmail.com",'motivo':"nada a ver",'descicao':"Descricaonada a ver" } ));

print(dados)