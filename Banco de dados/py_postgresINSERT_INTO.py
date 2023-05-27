import psycopg2
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "Dh9o8lu9ii@", host = "127.0.0.1", port = "5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute('''INSERT INTO AGENDA(ID,NOME,TELEFONE) VALUES (1,'DIEGO',999204860);''')
print("Inserção realizada com sucesso!")
conn.commit()
cur.close()
conn.close()