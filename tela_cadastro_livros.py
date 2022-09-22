from f_tela_base import *

#Referente a tela de consulta
def tela_cadastrarLivros(self):
    self.window.destroy()
    tela_padrao(self)
    frame = Frame(self.window).pack()
    id_livro = Label(frame, text='Id_livro: ',bg="#a9a9a9",font=('Ivy 15'))
    id_livro.place(x=15,y=100)
    entry_id = Entry(frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_id.place(x=100,y=100)

    label_titulo = Label(frame, text='Titulo: ',bg="#a9a9a9",font=('Ivy 15'))
    label_titulo.place(x=15, y=150)
    entry_titulo = Entry(frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_titulo.place(x=90,y=150)