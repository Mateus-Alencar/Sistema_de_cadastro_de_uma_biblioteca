from f_tela_base import *

def icon_comeco(self, usu):
    self.window.destroy()
    tela_padrao(self)
    self.frame=Frame(self.window, bg='#D9D9D9')
    self.img_livros = PhotoImage(file='pilha_de_livros.png')
    self.frame.pack()
    self.icon=Label(self.frame, image=self.img_livros, width=140, height=140, bg='#d9d9d9')
    self.icon.pack()
    if usu == self.funcionario:
        label = Label(self.frame, text='Funcionário', font='Arial 20 bold', bg='#d9d9d9', fg='black')
        label.pack()
    else:
        label = Label(self.frame, text='Cliente', font='Arial 20 bold', bg='#d9d9d9', fg='black')
        label.pack()


def tela_cadastroCliente(self, usu):
    icon_comeco(self, usu)


def tela_cadastroFuncionario(self, usu):
    icon_comeco(self, usu)
    