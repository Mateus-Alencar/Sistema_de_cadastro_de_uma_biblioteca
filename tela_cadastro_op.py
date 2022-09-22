from f_tela_base import *


def tela_cadastroCliente(self):
    self.window.destroy()
    tela_padrao(self)
    self.img_livros = PhotoImage(file='pilha_de_livros.png')
    frame=Frame(self.window)
    frame.pack()
    self.icon=Label(frame, image=self.img_livros, width=140, height=140, bg='#d9d9d9')
    self.icon.pack()


def tela_cadastroFuncionario(self):
    self.window.destroy()
    tela_padrao(self)
    self.img_livros = PhotoImage(file='pilha_de_livros.png')
    frame=Frame(self.window)
    frame.pack()
    self.icon=Label(frame, image=self.img_livros, width=140, height=140, bg='#d9d9d9')
    self.icon.pack()