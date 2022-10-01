from f_tela_base import *
from tela_cadastro_op import *

def tela_Op_cadastros(self, frame):
    frame.destroy()
    tela_padrao(self)
    self.frame = Frame(self.window, width='530', height='810', bg='#d9d9d9')
    self.frame.place(x='0', y='90')

    self.titulo = Label(self.frame, text='CADASTRAR', font='Ivy 34 bold',bg='#d9d9d9')
    self.titulo.place(x=150, y=90)
    self.funcionario = Button(self.frame,text=('Funcionário'), font='Arial 16 bold', width=20, height=2, bg='blue', fg='black', command=lambda:tela_cadastroFuncionario(self,self.funcionario))
    self.funcionario.place(x=130, y=210)
    self.cliente= Button(self.frame,text=('Cliente'), font='Arial 16 bold', width=20, height=2, bg='blue', fg='black', command=lambda:tela_cadastroCliente(self, self.cliente))
    self.cliente.place(x=130, y=300)
    self.login= Button(self.frame,text=('Login'), font='Arial 16 bold', width=20, height=2, bg='blue', fg='black', command=lambda:tela_login(self, self.login))
    self.login.place(x=130, y=390)


