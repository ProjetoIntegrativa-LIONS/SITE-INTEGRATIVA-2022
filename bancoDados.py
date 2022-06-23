import mysql.connector
from mysql.connector import errorcode

class Banco():

    def ConexaoBanco(self):
        con = None
        try:
            con = mysql.connector.connect(host='localhost',user='root',password='',database='databaselions')
        except mysql.connector.Error as ex:
            print(ex)
            return ex
        return con

    def ExecutarComando(self, sql, parametros=[]):
        try:
            conexao =self.ConexaoBanco() 
            cursor = conexao.cursor()
            cursor.execute(sql, parametros)
            conexao.commit()            

        except mysql.connector.Error as ex:
            print ("ERRO:   "+ str(ex))

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def ExecutarSelect(self, sql, parametros=[]):
        try:
            conexao =self.ConexaoBanco() 
            cursor = conexao.cursor()
            cursor.execute(sql, parametros)           
            dados = cursor.fetchall()
            return dados

        except mysql.connector.Error as ex:
            print ("ERRO:   "+ str(ex))

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()