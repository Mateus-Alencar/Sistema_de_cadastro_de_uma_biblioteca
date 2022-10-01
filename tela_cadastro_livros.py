from turtle import width
from f_tela_base import *

#Referente a tela de consulta
def tela_cadastrarLivros(self, frame):
    frame.destroy()
    self.frame = Frame(self.window, width='550', height='750',bg='#d9d9d9')
    self.frame.place(x='2', y='90')
    id_livro = Label(self.frame, text='Id_livro: ',bg="#a9a9a9",font=('Ivy 15'))

    label_titulo = Label(self.frame, text='Titulo: ',bg="#a9a9a9",font=('Ivy 15'))
    label_titulo.place(x=35, y=100)
    entry_titulo = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_titulo.place(x=100,y=100)

    label_autor = Label(self.frame, text='Autor: ',bg="#a9a9a9",font=('Ivy 15'))
    label_autor.place(x=35, y=150)
    entry_autor = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_autor.place(x=100,y=150)

    label_descricao = Label(self.frame, text='Descrição: ',bg="#a9a9a9",font=('Ivy 15'))
    label_descricao.place(x=35, y=200)
    entry_descricao = Entry(self.frame, width=22, justify='left',font='Arial 15 bold', relief='solid')
    entry_descricao.place(x=100,y=200)


    botao_salvar = Button(self.frame, text='Salvar', bg='red', fg='white',width=18, font='Ivy 18', command=lambda:salvar())
    botao_salvar.place(x=120, y=500)
    botao_cancelar = Button(self.frame, text='Cancelar', bg='red', fg='white',width=18, font='Ivy 18', command=lambda:cancelar(self))
    botao_cancelar.place(x=120, y=550)

    def salvar():
        pass
    def cancelar(self):
        pass

    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.window, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_app(self.frame))
    self.botao_voltar.place(x=10,y=845)