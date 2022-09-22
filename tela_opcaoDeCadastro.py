from f_tela_base import *
from tela_cadastro_op import *

def tela_Op_cadastros(self):
    self.window.destroy()
    tela_padrao(self)
    funcionario = Button(self.window,text=('Cliente'), font='Arial 16 bold', width=38, height=15, bg='#5cbceb', fg='black', command=lambda:tela_cadastroCliente(self))
    funcionario.pack(pady=5)
    cliente= Button(self.window,text=('Funcionário'), font='Arial 16 bold', width=38, height=15, bg='#008dd2', fg='black', command=lambda:tela_cadastroFuncionario(self))
    cliente.pack(pady=5)

    self.img_voltar = PhotoImage(file='voltar.png')
    botao_voltar = Button(self.window, image=self.img_voltar, width=34,height=34, command=lambda:voltar(self, tela_Op_cadastros))
    botao_voltar.place(x=10,y=850)

