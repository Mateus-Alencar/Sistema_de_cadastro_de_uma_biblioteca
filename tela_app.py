from f_tela_base import *
from tela_opcaoDeCadastro import *

def tela_app(self):
    self.frame.destroy()
    self.telaIn = True
    tela_padrao(self)
    self.frame = Frame(self.window, width='530', height='810', bg='#d9d9d9')
    self.frame.place(x='0', y='80')
    self.titulo = Label(self.frame, text='CADASTRAR', font='Ivy 34 bold',bg='#d9d9d9')
    self.titulo.place(x=120, y=90)

    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.frame, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_app())
    self.botao_voltar.place(x=10,y=745)