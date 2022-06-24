import mysql.connector
from mysql.connector import errorcode

class Banco():

    def ConexaoBanco(self):
        con = None
        try:
            con = mysql.connector.connect(host='lionslages.org.br',user='lionsl78_master', port="3306", passwd='.Ce)zTA#9?0_;LLTi^',database='lionsl78_master_db')
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