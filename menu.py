from tkinter import *
from produtos import MainProdutos

def MainMenu():
    # ------------Opening Window----------------------------------
    window = Tk()
    window.title("Lanchonete")
    # window.iconbitmap("egg.ico")
    window.geometry("750x500") # WxH
    window.configure(bg="#4F4F4F")

    # ------------Widgets----------------------------------
    lblanchonetename = Label(window, text="Sistema Lanchonete", bg="#4F4F4F", fg="#ffffff", bd=0.01, font="Jokerman 35 bold")
    lblanchonetename.place(x=145,y=0)
    #botões
    btcliente = Button(window,text="Cadastrar cliente", padx=50, pady=50,font="Britannic 9 bold", borderwidth=5, bg="#C0C0C0")
    btcliente.place(x=60,y=94)
    btfuncionario = Button(window,text="Cadastrar funcionario", padx=35, pady=50, font="Britannic 9 bold", borderwidth=5, bg="#C0C0C0")
    btfuncionario.place(x=275,y=94)
    btprodutos = Button(window,text="Cadastrar produtos", padx=44, pady=50,command=MainProdutos, font="Britannic 9 bold", borderwidth=5, bg="#C0C0C0")
    btprodutos.place(x=60,y=230)
    btrelatorio = Button(window,text="Relatório", padx=70, pady=50, font="Britannic 9 bold", borderwidth=5, bg="#C0C0C0")
    btrelatorio.place(x=275,y=230)
    btpedidos = Button(window,text="Pedidos", padx=75, pady=50, font="Britannic 9 bold", borderwidth=5, bg="#C0C0C0")
    btpedidos.place(x=483,y=230)

    # ------------Loop End----------------------------------
    window.mainloop()
