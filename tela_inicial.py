from tkinter import *
from f_tela_base import *
from tela_opcaoDeCadastro import *
from tela_app import *

class app:
    def __init__(self):
        self.window = Tk()
        self.window.title('Tela inicial')
        self.window.geometry('520x900')
        self.window.resizable(0,0)
        self.window.config(bg='#d9d9d9')
        
        self.frame = Frame(self.window, width='520', height='900',bg='#004aad')
        self.frame.place(x='0', y='0')
        self.img_livros = PhotoImage(file='livros2.png')
        self.icon=Label(self.frame, image=self.img_livros, width=260, height=260, bg='#d9d9d9')
        self.icon.place(y='100', x= '140')
        texto = Label(self.frame, text='BIBLIOTECA', font='Impact 30 bold', bg='#004aad')
        texto.place(x=160, y=400)
        btm_iniciar = Button(self.frame, text='Iniciar', bg='black',borderwidth=4, fg='white',width=18, font='Ivy 18', command=lambda:tela_Op_cadastros(self))
        btm_iniciar.place(x=130, y=510)
        self.window.mainloop()

    def voltar_in(self):
        tela_Op_cadastros(self)

    def voltar_app(self):
        tela_app(self)

app()
