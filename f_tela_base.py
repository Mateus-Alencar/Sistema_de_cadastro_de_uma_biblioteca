import time
from tkinter import *
from tkinter.ttk import Progressbar
from tela_config import *

def tela_padrao(self):
        barraAzul = Frame(self.window,borderwidth=0, width=520, height=80, bg='#004aad')
        barraAzul.pack()
        self.photo = PhotoImage(file='menu.png')
        self.barraMenu = Button(self.window, image=self.photo ,width=140,border=0, height=48,bg='#004aad', command=lambda:tela_menu(self))
        self.barraMenu.place(x=5, y=15)
        

def tela_menu(self):
        self.tela_deFundo = PanedWindow(self.window,borderwidth=0, bg='#a9a9a9',relief='raised',bd=2, orient=VERTICAL)
        self.tela_deFundo.place(x=1,y=90)
        frame_menu = Frame(self.tela_deFundo, width=350, height=550, bg='#B0C4DE')
        frame_menu.pack()
        self.barraMenu.config(text='Menu', compound=LEFT, font='Ivy 23 bold')

        botao_home = Button(frame_menu, bg='#B0C4DE', fg='black',borderwidth=0,font='Arial 18 bold', text='Home', command=lambda:self.voltar_app())
        botao_home.place(x= 8, y= 0)
        linha = Label(frame_menu,bg='#B0C4DE', text='_____________________________________________________________', font='Ivy 8 bold')
        linha.place(x=0,y=40)
        botao_Cadastrar = Button(frame_menu, bg='#B0C4DE', fg='black',borderwidth=0,font='Arial 18 bold', text='Cadastrar', command=lambda:self.voltar_tela_cadastros())
        botao_Cadastrar.place(x= 8, y= 60)
        linha = Label(frame_menu,bg='#B0C4DE', text='_____________________________________________________________', font='Ivy 8 bold')
        linha.place(x=0,y=100)
        botao_Consultar = Button(frame_menu, bg='#B0C4DE', fg='black',borderwidth=0,font='Arial 18 bold', text='Consultar', command=lambda:self.tela_consult())
        botao_Consultar.place(x= 8, y= 120)
        linha = Label(frame_menu,bg='#B0C4DE', text='_____________________________________________________________', font='Ivy 8 bold')
        linha.place(x=0,y=160)
        botao_Emprestimos = Button(frame_menu, bg='#B0C4DE', fg='black',borderwidth=0,font='Arial 18 bold', text='Empréstimos')
        botao_Emprestimos.place(x= 8, y= 180)
        linha = Label(frame_menu,bg='#B0C4DE', text='_____________________________________________________________', font='Ivy 8 bold')
        linha.place(x=0,y=220)
        botao_Livros = Button(frame_menu, bg='#B0C4DE', fg='black',borderwidth=0,font='Arial 18 bold', text='Livros', command=lambda:self.tela_l())
        botao_Livros.place(x= 8, y= 240)
        linha = Label(frame_menu,bg='#B0C4DE', text='_____________________________________________________________', font='Ivy 8 bold')
        linha.place(x=0,y=280)
        botao_config = Button(frame_menu, bg='#B0C4DE', fg='black',borderwidth=0,font='Arial 18 bold', text='Configurações', command=lambda:self.config())
        botao_config.place(x= 8, y= 300)
        linha = Label(frame_menu,bg='#B0C4DE', text='_____________________________________________________________', font='Ivy 8 bold')
        linha.place(x=0,y=340)

        self.img_voltar_c = PhotoImage(file='voltar.png')
        self.botao_voltar_c = Button(self.window, image=self.img_voltar_c,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:voltar(self))
        self.botao_voltar_c.place(x=10,y=825)

def voltar(self):
    self.tela_deFundo.destroy()
    self.botao_voltar_c.destroy()
    self.barraMenu['text']=''

def mudar_cor_fundo(self):
        #Mudar a cor de fundo da aplicação, acessando as propriedades do objeto window
        if self.window['bg'] == '#d9d9d9':
                self.window.config(bg='black')
                self.botao_cor_fundo['text'] = 'Tema claro'
                self.botao_voltar['bg']='black'
        else:
                self.window.config(bg='#d9d9d9')
                self.botao_voltar['bg']='#d9d9d9'
                self.botao_cor_fundo['text'] = 'Tema escuro'


def tempo(self):
    info = Label(font='Arial 10 bold', text='Carregando banco', bg='#d9d9d9')
    info.place(x=190,y=480)
    self.bar = Progressbar(self.window, orient=HORIZONTAL,length=350)
    self.bar.place(x=70,y=500)
    for i in range(10):
        time.sleep(0.2)
        self.bar['value']+=10
        self.bar.update()
        if self.bar['value'] == 60:
                info['text'] =  'Checando informações'
        if self.bar['value'] == 100:
            self.bar.destroy()
            info.destroy()