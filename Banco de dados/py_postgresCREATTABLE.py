import psycopg2
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "Dh9o8lu9ii@", host = "127.0.0.1", port = "5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute('''CREATE TABLE AGENDA(ID INT PRIMARY KEY NOT NULL,NOME CHAR(90) NOT NULL,TELEFONE INT NOT NULL);''')
print("Tabela criada com sucesso!")
conn.commit()
conn.close()