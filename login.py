from tkinter import *
from menu import MainMenu
from tkinter import messagebox


#-------------Função para sair----------------


# -------------Opening Window------------------
window=Tk()
window.title("Lanchonete")
window.configure(bg="#4F4F4F") # grey31 = #4F4F4F	
window.geometry("750x500") # WxH
window.iconbitmap("logo.ico")	

def quit_window():
      if messagebox.askokcancel("Sair","Deseja realmente sair?"):
         window.destroy()

#------------Frames-----------------------
framelogin = Frame(window, background="#C0C0C0", highlightbackground="#ffffff", highlightthickness=3) # C0C0C0 == Silver
framelogin.place(relwidth=0.60,relheight=0.75,relx=0.2,rely=0.15)
# relwidth = largura do lado direito
# relheight = altura de baixo
# relx = largura do lado esquerdo (eixo x)
# rely = altura de cima (eixo y)

#------------ Widgets----------------------
#labels
lblanchonetename = Label(window, text="Sistema Lanchonete", bg="#4F4F4F", fg="#ffffff", bd=0.01, font="Jokerman 35 bold")
lblogin = Label(framelogin, text="Login", font="Britannic 40 bold", bg="#C0C0C0")
lbuser = Label(framelogin, text="Usuário:", font="Britannic 15 bold", bg="#C0C0C0")
lbpassword = Label(framelogin, text="Senha:", font="Britannic 15 bold", bg="#C0C0C0")
#entrys
entryuser = Entry(framelogin, width=32, borderwidth=5)
entrypassword = Entry(framelogin, width=32, borderwidth=5)
#botões
btentrar = Button(framelogin, text="Entrar", padx=60, pady=5, command=MainMenu, borderwidth=5, bg="#C0C0C0", font="Britannic 9 bold")
btexit = Button(framelogin, text="Sair", fg="red", padx=20, pady=5, command=quit_window,borderwidth=5, bg="#C0C0C0", font="Britannic 9 bold")

#---------------Layout widgets------------------------
lblanchonetename.place(x=145,y=0)
lblogin.place(x=180,y=20)
lbuser.place(x=180,y=100)
lbpassword.place(x=180,y=180)
entryuser.place(x=185,y=140)
entrypassword.place(x=185,y=220)
btentrar.place(x=197, y=270)
btexit.place(x=10, y=300)

#-------------Image----------------------------
img = PhotoImage(file="imagens/login4.png")
lbimage = Label(framelogin, image= img, bg="#C0C0C0")
lbimage.place(x=10,y=85)

# -------------Loop End----------------------------
window.mainloop()