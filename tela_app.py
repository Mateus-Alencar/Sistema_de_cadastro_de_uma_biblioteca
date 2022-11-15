from f_tela_base import *
from tela_livros import *
from tela_opcaoDeCadastro import *


def tela_app(self):
    #tela principal
    self.frame.destroy()
    tela_padrao(self)
    self.frame = Frame(self.window, width='530', height='810', bg='#d9d9d9')
    self.frame.place(x='0', y='80')
    
    self.cadastrar = Button(self.frame,text=('Cadastrar'), font='Ivy 17 bold', width=28, height=2, bg='blue', fg='black', command=lambda:self.voltar_tela_cadastros())
    self.cadastrar.place(x=60, y=100)
    self.consultar = Button(self.frame,text=('Consultar'), font='Ivy 17 bold', width=28, height=2, bg='blue', fg='black', command=lambda:self.tela_consult())
    self.consultar.place(x=60, y=200)
    self.emprestimos = Button(self.frame,text=('Empréstimos'), font='Ivy 17 bold', width=28, height=2, bg='blue', fg='black')
    self.emprestimos.place(x=60, y=300)
    self.livros = Button(self.frame,text=('Livros'), font='Ivy 17 bold', width=28, height=2, bg='blue', fg='black', command=lambda:tela_livros(self))
    self.livros.place(x=60, y=400)

    self.img_livros = PhotoImage(file='livrosB.png')
    self.icon=Label(self.frame, image=self.img_livros, width=260, height=260, bg='#d9d9d9')
    self.icon.place(y='500', x= '140')

    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.frame, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_tela_cadastros())
    self.botao_voltar.place(x=10,y=745)