from tkinter import *
from produtos import MainProdutos
from clientes import MainClientes
from tkinter import messagebox
from PIL import ImageTk, Image


     
    

def MainMenu():

   
    # ------------Opening Window----------------------------------
    window = Tk()
    window.title("Lanchonete")
    # window.iconbitmap("egg.ico")
    window.geometry("750x500") # WxH
    #window.configure(bg="#4F4F4F")
    window.iconbitmap("logo.ico")

    def quit_window():
      if messagebox.askokcancel("Sair","Deseja realmente sair?"):
         window.destroy()

    # ------------Widgets----------------------------------
    lblanchonetename = Label(window, text="Sistema Lanchonete", font="Ariel 35 bold")
    lblanchonetename.place(x=145,y=0)

    framelogin = Frame(window, background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3) # C0C0C0 == Silver
    framelogin.place(relwidth=0.60,relheight=0.75,relx=0.2,rely=0.15)

    img = ImageTk.PhotoImage(Image.open("logo.png"))
    panel = Label(window,image = img)
    panel.grid(row =1,column =0)

   
    
    #botões
   



    menu_bar = Menu(window)
    menu_bar.add_separator()

    file_menu = Menu(menu_bar,tearoff=0)
    file_menu.add_command(label="Clientes",command=MainClientes)
    file_menu.add_separator()
    file_menu.add_command(label="Usuarios")
    file_menu.add_separator()
    file_menu.add_command(label="Produtos",command=MainProdutos)
    file_menu.add_separator()    
    file_menu.add_command(label="Sair",command=quit_window)
    menu_bar.add_cascade(label="Cadastrar",menu=file_menu)

    menu_bar.add_separator()



    relatorio_menu = Menu(menu_bar,tearoff=0)
    relatorio_menu.add_command(label="Clientes")
    relatorio_menu.add_separator()
    relatorio_menu.add_command(label="Usuário")
    relatorio_menu.add_separator()
    relatorio_menu.add_command(label="Produtos")
    menu_bar.add_cascade(label="Relatórios",menu=relatorio_menu)

    menu_bar.add_separator()



    pedidos_menu = Menu(menu_bar,tearoff=0)
    pedidos_menu.add_command(label="Novo")
    pedidos_menu.add_separator()
    menu_bar.add_cascade(label="Pedidos",menu=pedidos_menu)

    window.configure(menu=menu_bar)
    window.mainloop()



    # ------------Loop End----------------------------------
    window.mainloop()
