import tkinter as tk
def mostrar_nomes():
   print("Nome: %s\nSobrenome: %s" % (e1.get(), e2.get()))
   print("Idade: %s\nPeso: %s"% (e3.get(), e4.get()))
janela = tk.Tk()
janela.title("Aplicação GUI com o Widget Entry")
tk.Label(janela,text="Nome").grid(row=0)
tk.Label(janela,text="Sobrenome").grid(row=1)
tk.Label(janela,text="Idade").grid(row=2)
tk.Label(janela,text="Peso").grid(row=3)
e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e3 = tk.Entry(janela)
e4 = tk.Entry(janela)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

tk.Button(janela, text='Sair',command=janela.quit).grid(row=5,column=1,sticky=tk.W,pady=4)
tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=5,column=2,sticky=tk.W,pady=4)
tk.mainloop()