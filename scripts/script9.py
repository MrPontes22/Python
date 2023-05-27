arquivo_escrita = open("dados_write2.txt", "w")
arquivo_escrita.write("Diego Pontes.")
arquivo_escrita.write("\nMatricula:.")
arquivo_escrita.write("\nDisciplina:.")
arquivo_escrita.close()

arquivo = open("dados_write2.txt", "r")

print("Iterando sobre o arquivo")
for linha in arquivo:
    print(repr(linha))

arquivo.close()
