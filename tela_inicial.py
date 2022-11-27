from tela_opcaoDeCadastro import *
from tela_app import *
from tela_config import *
from tela_livros import *
from tela_consultas import *


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

    def ex(self):
        if __name__ == 'tela_menu' or __name__ == 'tela_padrao':
            self.barraMenu.destroy()
            self.tela_deFundo.destroy()

    #Navegação entre telas.
    def voltar_tela_cadastros(self):
        self.ex()
        tela_Op_cadastros(self)

    def voltar_app(self):
        self.barraMenu['text']=''
        tela_app(self)
        
    def t_app(self):
        tela_app(self)

    def tela_consult(self):
        tela_consultas(self)
        
    def config(self):
        tela_config(self)
    
    def tela_l(self):
        tela_livros(self)

    def emprestimos_consult(self):
        tela_consultas(self)


app()