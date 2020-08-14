import tkinter as gui
from tkinter import messagebox
from tkinter import *

def MainProdutos():
    # ------------Opening Window----------------------------------
    window = gui.Tk()
    window.title("Lanchonete")
    window.iconbitmap("egg.ico")
    window.geometry("750x500") # WxH
    window.configure(bg="#4F4F4F")

    # ------------Frames----------------------------------
    frame = gui.Frame(window,background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3)
    frame.place(relwidth=0.80,relheight=0.73,relx=0.1,rely=0.15)

    # ------------Widgets----------------------------------
    #labels
    lblanchonetename = Label(window, text="Sistema Lanchonete", bg="#4F4F4F", fg="#ffffff", bd=0.01, font="Jokerman 35")
    lblanchonetename.place(x=150,y=0)
    labelcod = gui.Label(frame,text="Código do produto:", bg="#C0C0C0", font="Britannic 10 bold")
    labelcod.grid(row=0,column=0)
    entrycod = gui.Entry(frame)
    entrycod.grid(row=0, column=1)
    labelnome = gui.Label(frame,text="Nome do produto:", bg="#C0C0C0", font="Britannic 10 bold")
    labelnome.grid(row=0,column=2)
    #entrys
    entrynome = gui.Entry(frame)
    entrynome.grid(row=0, column=3)
    #botões
    btcliente = gui.Button(window,text="Sair", fg="red", bg="#C0C0C0", padx=20, pady=2, borderwidth=5)
    btcliente.place(x=650,y=450)
    btfuncionario = gui.Button(window,text="Salvar", fg="green", bg="#C0C0C0", padx=20, pady=2, borderwidth=5)
    btfuncionario.place(x=550,y=450)

    # ------------Loop End----------------------------------
    window.mainloop()
