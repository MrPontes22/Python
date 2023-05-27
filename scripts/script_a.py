def extrair_linha(dados.txt):
    with open(dados.txt) as arquivo:
        linhas = arquivo.read()
        for linha in linhas:
            return linha
print("nome do arquivo:",arquivo.name)