from f_tela_base import *

#Referente a tela de consulta
def tela_cadastrarLivros(self, frame):
    frame.destroy()
    self.frame = Frame(self.window, width='550', height='860',bg='#d9d9d9')
    self.frame.place(x='2', y='70')
    id_livro = Label(self.frame, text='Id_livro: ',bg="#a9a9a9",font=('Ivy 15'))
    id_livro.place(x=15,y=100)
    entry_id = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_id.place(x=100,y=100)

    label_titulo = Label(self.frame, text='Titulo: ',bg="#a9a9a9",font=('Ivy 15'))
    label_titulo.place(x=15, y=150)
    entry_titulo = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_titulo.place(x=90,y=150)