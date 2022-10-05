from logging.handlers import TimedRotatingFileHandler
from tkinter import *
from tkinter import colorchooser
from PIL import ImageTk, Image
from tkinter.colorchooser import askcolor

def tela_padrao(self):
        barraAzul = Frame(self.window,borderwidth=0, width=520, height=80, bg='#004aad')
        barraAzul.pack()
        self.photo = PhotoImage(file='menu.png')
        self.barraMenu = Button(self.window, image=self.photo ,width=140,border=0, height=48,bg='#004aad', command=lambda:tela_menu(self))
        self.barraMenu.place(x=5, y=15)
        

def tela_menu(self):
        tela_deFundo = PanedWindow(self.window,borderwidth=0, bg='#a9a9a9',relief='raised',bd=2, orient=VERTICAL)
        tela_deFundo.place(x=1,y=80)
        frame_menu = Frame(tela_deFundo, width=350, height=550, bg='#B0C4DE')
        frame_menu.pack()
        self.barraMenu.config(text='Menu', compound=LEFT, font='Ivy 23 bold')

        botao_home = Button(frame_menu, bg='#B0C4DE', fg='black',borderwidth=0,font='Arial 18 bold', text='Home')
        botao_home.place(x= 8, y= 0)
        botao_Cadastrar = Button(frame_menu, bg='#B0C4DE', fg='black',borderwidth=0,font='Arial 18 bold', text='Cadastrar')
        botao_Cadastrar.place(x= 8, y= 60)
        botao_Consultar = Button(frame_menu, bg='#B0C4DE', fg='black',borderwidth=0,font='Arial 18 bold', text='Consultar')
        botao_Consultar.place(x= 8, y= 120)
        botao_Emprestimos = Button(frame_menu, bg='#B0C4DE', fg='black',borderwidth=0,font='Arial 18 bold', text='Empréstimos')
        botao_Emprestimos.place(x= 8, y= 180)
        botao_Livros = Button(frame_menu, bg='#B0C4DE', fg='black',borderwidth=0,font='Arial 18 bold', text='Livros')
        botao_Livros.place(x= 8, y= 240)

        self.img_voltar_c = PhotoImage(file='voltar.png')
        self.botao_voltar_c = Button(self.window, image=self.img_voltar_c,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:voltar(self, tela_deFundo))
        self.botao_voltar_c.place(x=10,y=865)

def voltar(self, telaVoltar):
    telaVoltar.destroy()
    self.botao_voltar_c.destroy()
    self.barraMenu.destroy()
    self.barraMenu = Button(self.window, image=self.photo ,width=140,border=0, height=48,bg='#004aad', command=lambda:tela_menu(self))
    self.barraMenu.place(x=5, y=15)

def mudar_cor_fundo(self):
        #Mudar a cor de fundo da aplicação, acessando as propriedades do objeto window
        cor  = askcolor(title='cores')
        self.window.config(bg=cor[1])
        '''if self.window['bg'] == '#d9d9d9':
                self.window.config(bg='black')
                self.botao_cor_fundo['text'] = 'Tema claro'
                self.botao_voltar['bg']='black'
        else:
                self.window.config(bg='#d9d9d9')
                self.botao_voltar['bg']='#d9d9d9'
                self.botao_cor_fundo['text'] = 'Tema escuro'''
