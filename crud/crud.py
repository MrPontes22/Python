import psycopg2

class AppBD:
    def __init__(self):
        print('Método Construtor')
        
    def abrirConexao(self):
        try:
          self.connection = psycopg2.connect(user="postgres",
                                  password="Dh9o8lu9ii@",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="dbestudo")
        except (Exception, psycopg2.Error) as error :
            if(self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)
#-----------------------------------------------------------------------------
#Selecionar todos os Produtos
#-----------------------------------------------------------------------------                 
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
    
            print("Selecionando todos os produtos")
            sql_select_query = """select * from PRODUTO """
                    
            
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()             
            print(registros)
                
    
        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)
    
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
        return registros
#-----------------------------------------------------------------------------
#Inserir Produto
#-----------------------------------------------------------------------------                 
    def inserirDados(self, id, nome, preco):
        try:
          self.abrirConexao()
          cursor = self.connection.cursor()
          postgres_insert_query = """ INSERT INTO PRODUTO
          (id, 'nome', preco) VALUES (%s,%s,%s)"""
          record_to_insert = (id, nome, preco)
          cursor.execute(postgres_insert_query, record_to_insert)
          self.connection.commit()
          count = cursor.rowcount
          print (count, "Registro inserido com successo na tabela PRODUTO")
        except (Exception, psycopg2.Error) as error :
          if(self.connection):
              print("Falha ao inserir registro na tabela PRODUTO", error)
        finally:
            #closing database connection.
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
                
#-----------------------------------------------------------------------------
#Atualizar Produto
#-----------------------------------------------------------------------------                 
    def atualizarDados(self, id, nome, preco):
        try:
            self.abrirConexao()    
            cursor = self.connection.cursor()

            print("Registro Antes da Atualização ")
            sql_select_query = """select * from PRODUTO
            where "id" = %s"""
            cursor.execute(sql_select_query, (id,))
            record = cursor.fetchone()
            print(record)    
            # Atualizar registro
            sql_update_query = """Update PRODUTO set "NOME" = %s, 
            "PRECO" = %s where "id" = %s"""
            cursor.execute(sql_update_query, (nome, preco, id))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso! ")    
            print("Registro Depois da Atualização ")
            sql_select_query = """select * from PRODUTO
            where "id" = %s"""
            cursor.execute(sql_select_query, (id,))
            record = cursor.fetchone()
            print(record)    
        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)    
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

#-----------------------------------------------------------------------------
#Excluir Produto
#-----------------------------------------------------------------------------                 
    def excluirDados(self, id):
        try:
            self.abrirConexao()    
            cursor = self.connection.cursor()    
            # Atualizar registro
            sql_delete_query = """Delete from PRODUTO
            where "id" = %s"""
            cursor.execute(sql_delete_query, (id, ))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso! ")        
        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)    
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
                
#-----------------------------------------------------------------------------
