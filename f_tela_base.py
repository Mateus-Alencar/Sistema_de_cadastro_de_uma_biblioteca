from logging.handlers import TimedRotatingFileHandler
from tkinter import *
from tkinter import colorchooser
from PIL import ImageTk, Image
from tkinter.colorchooser import askcolor

def tela_padrao(self):
        self.window = Tk()
        self.window.title('Tela inicial')
        self.window.geometry('520x900')
        self.window.resizable(0,0)
        self.window.config(bg='#d9d9d9')

        barraAzul = Frame(self.window,borderwidth=0, width=520, height=70, bg='#008dd2')
        barraAzul.pack()
        self.photo = PhotoImage(file='menu.png')
        self.barraMenu = Button(self.window, image=self.photo ,width=48, height=48,bg='#31af91', command=lambda:tela_config(self))
        self.barraMenu.place(x=10, y=10)
        texto = Label(self.window, text='SISTEMA DE CADASTRO', font='Impact 23 bold', bg='#008dd2')
        texto.place(x=120, y=10)
        frameV = Frame(self.window).place(x=0, y=800)

def tela_config(self):
        tela_deFundo = PanedWindow(self.window,borderwidth=0, bg='#a9a9a9',relief='raised',bd=2, orient=VERTICAL)
        tela_deFundo.place(x=10,y=50)
        frame_menu = Frame(tela_deFundo, width=300, height=350)
        frame_menu.pack()
        
        self.img_fundo = PhotoImage(file='tela_config_fundo.png')
        img = Label(tela_deFundo,text='Usuários',image=self.img_fundo, height=150, width=300)
        img.place(x=-1, y= -1)

        botao_cad_log = Button(frame_menu, bg='black', fg='white',font='Arial 15 bold', text='Cadastrar/Login')
        botao_cad_log.place(x= 10, y= 160)
        self.botao_cor_fundo = Button(frame_menu, bg='black', fg='white',font='Arial 15 bold', text='Cor de fundo', command=lambda:mudar_cor_fundo(self))
        self.botao_cor_fundo.place(x= 10, y= 220)
        botao_som = Button(frame_menu, bg='black', fg='white',font='Arial 15 bold', text='Som')
        botao_som.place(x= 10, y= 280)

        self.img_voltar_c = PhotoImage(file='voltar.png')
        self.botao_voltar_c = Button(self.window, image=self.img_voltar_c,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:voltar(self, tela_deFundo))
        self.botao_voltar_c.place(x=10,y=845)

def voltar(self, telaVoltar):
    telaVoltar.destroy()
    self.botao_voltar_c.destroy()

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
