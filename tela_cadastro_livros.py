from turtle import width
from f_tela_base import *

#Referente a tela de consulta
def tela_cadastrarLivros(self, frame):
    frame.destroy()
    self.frame = Frame(self.window, width='550', height='700',bg='#d9d9d9')
    self.frame.place(x='2', y='70')
    id_livro = Label(self.frame, text='Id_livro: ',bg="#a9a9a9",font=('Ivy 15'))

    label_titulo = Label(self.frame, text='Titulo: ',bg="#a9a9a9",font=('Ivy 15'))
    label_titulo.place(x=35, y=100)
    entry_titulo = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_titulo.place(x=100,y=100)

    label_autor = Label(self.frame, text='Autor: ',bg="#a9a9a9",font=('Ivy 15'))
    label_autor.place(x=35, y=150)
    entry_autor = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_autor.place(x=100,y=150)

    label_editora = Label(self.frame, text='Editora: ',bg="#a9a9a9",font=('Ivy 15'))
    label_editora.place(x=35, y=200)
    entry_editora = Entry(self.frame, width=22, justify='left',font='Arial 15 bold', relief='solid')
    entry_editora.place(x=130,y=200)

    label_paginas = Label(self.frame, text='N° de páginas: ',bg="#a9a9a9",font=('Ivy 15'))
    label_paginas.place(x=35, y=250)
    entry_paginas = Entry(self.frame, width=8, justify='left',font='Arial 15 bold', relief='solid')
    entry_paginas.place(x=190,y=250)
