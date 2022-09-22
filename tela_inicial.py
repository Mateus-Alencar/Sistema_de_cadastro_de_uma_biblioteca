from tkinter import *
from turtle import left
from f_tela_base import *
from tela_opcaoDeCadastro import *
from tela_cadastro_livros import *


class app:
    def __init__(self):
        tela_padrao(self)

        #Botões
        cadastar = Button(self.window,text=('Login'), font='Arial 16 bold', width=20, height=15, bg='#00c2cb', fg='black', command=lambda:tela_Op_cadastros(self))
        cadastar.place(x=-5, y= 80)
        consultar = Button(self.window,text=('Consultar'), font='Arial 16 bold', width=20, height=15, bg='#00c2cb', fg='black')
        consultar.place(x=274, y= 80)
        emprestimos = Button(self.window,text=('Emprestimos'), font='Arial 16 bold', width=20, height=15, bg='#00c2cb', fg='black')
        emprestimos.place(x=-5, y= 470)
        livros = Button(self.window,text=('Livros'), font='Arial 16 bold', width=20, height=15, bg='#00c2cb', fg='black')
        livros.place(x=274, y= 470)
        img = PhotoImage(file='livros.png')
        link_cadastrarLivro = Button(self.window,text='Cadastrar livros',width=160, height=29,borderwidth=5, image=img, compound=LEFT, command=lambda:tela_cadastrarLivros(self))
        link_cadastrarLivro.place(x=340, y=855)

        self.window.mainloop()
    

       

app()
