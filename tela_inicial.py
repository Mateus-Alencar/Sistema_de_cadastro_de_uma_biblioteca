from tkinter import *
from turtle import left
from f_tela_base import *
from tela_opcaoDeCadastro import *
from tela_cadastro_livros import *
from tela_consultas import *
from tela_livros import *


class app:
    def __init__(self):
        tela_padrao(self)
        self.com()
        #Botões
    def com(self):
        self.frame = Frame(self.window, width='530', height='770', bg='#d9d9d9')
        self.frame.place(x='2', y='70')
        cadastar = Button(self.frame,text=('Login'), font='Arial 16 bold', width=20, height=15, bg='#00c2cb', fg='black', command=lambda:tela_Op_cadastros(self, self.frame))
        cadastar.place(x=-5, y= 5)
        self.consultar = Button(self.frame,text=('Consultar'), font='Arial 16 bold', width=20, height=15, bg='#00c2cb', fg='black', command=lambda:tela_consultas(self, self.frame, self.consultar))
        self.consultar.place(x=274, y= 5)
        self.emprestimos = Button(self.frame,text=('Emprestimos'), font='Arial 16 bold', width=20, height=15, bg='#00c2cb', fg='black', command=lambda:tela_consultas(self,self.frame, self.emprestimos))
        self.emprestimos.place(x=-5, y= 390)
        livros = Button(self.frame,text=('Livros'), font='Arial 16 bold', width=20, height=15, bg='#00c2cb', fg='black', command=lambda:tela_livros(self, self.frame))
        livros.place(x=274, y= 390)
        img = PhotoImage(file='livros.png')
        link_cadastrarLivro = Button(self.window,text='Cadastrar livros',width=160, height=29,borderwidth=5, image=img, compound=LEFT, command=lambda:tela_cadastrarLivros(self, self.frame))
        link_cadastrarLivro.place(x=340, y=850)

        self.window.mainloop()

    def voltar_app(self, frame):
        frame.destroy()
        self.com()

app()
