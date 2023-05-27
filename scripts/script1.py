import os

# Para o arquivo dados1.txt
arquivo1 = open("teste.txt")  # Caminho relativo
arquivo2 = open("teste.txt")  # Caminho absoluto

# Para o arquivo dados2.txt
arquivo3 = open("teste.txt")  # Caminho relativo
arquivo4 = open("teste.txt")  # Caminho absoluto

#print(os.path.relpath(arquivo1.name))
#print(os.path.abspath(arquivo1.name))

print(arquivo1)
