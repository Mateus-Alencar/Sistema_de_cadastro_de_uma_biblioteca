from f_tela_base import *
from tela_cadastro_op import *

def tela_Op_cadastros(self, frame):
    frame.destroy()
    self.frame = Frame(self.window, width='530', height='500', bg='#d9d9d9')
    self.frame.place(x='1', y='70')
    self.funcionario = Button(self.frame,text=('Funcionário'), font='Arial 16 bold', width=39, height=15, bg='#5cbceb', fg='black', command=lambda:tela_cadastroFuncionario(self,self.funcionario))
    self.funcionario.pack(pady=4)
    self.cliente= Button(self.frame,text=('Cliente'), font='Arial 16 bold', width=39, height=15, bg='#008dd2', fg='black', command=lambda:tela_cadastroCliente(self, self.cliente))
    self.cliente.pack(pady=4)

    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.window, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_app())
    self.botao_voltar.place(x=10,y=845)

