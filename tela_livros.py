from f_tela_base import *
from tela_cadastro_livros import *

def tela_livros(self):
    self.frame.destroy()
    self.frame = Frame(self.window, width='530', height='850', bg='#d9d9d9')
    self.frame.place(x='0', y='90')

    

    linha = Label(self.frame,bg='#d9d9d9', text='______________________________________________________________________________________', font='Ivy 8 bold')
    linha.place(x=0,y=700)
    link_tela_cadastro_livros = Button(self.frame, text='Cadastrar livro', fg='white', font='Ivy 12 bold', borderwidth=0, bg='black', width=16 ,height=2, command=lambda:tela_cadastrarLivros(self))
    link_tela_cadastro_livros.place(x=330,y=740)
    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.frame, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_app())
    self.botao_voltar.place(x=10,y=745)