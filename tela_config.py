from tkinter import scrolledtext
from tkinter import *
from winsound import PlaySound
from f_tela_base import *
from playsound import playsound



def tela_config(self):
    self.frame.destroy()
    self.barraMenu['text']=''
    self.frame = Frame(self.window, width='530', height='810', bg='#d9d9d9')
    self.frame.place(x='0', y='80')

    config_label = Label(self.frame, bg='#d9d9d9',borderwidth=4, text='Configurações', fg='black', width=15, font='Ivy 24 bold')
    config_label.place(x=120,y=80)

    tema_label = Label(self.frame,bg='#d9d9d9',borderwidth=4, text='Tema de fundo', fg='black', width=15, font='Ivy 16')
    tema_label.place(x=30,y=180)
    temaBranco = Button(self.frame, bg='white',borderwidth=4, fg='white', width=6, height=1)
    temaBranco.place(x=200,y=180)
    temaEscuro = Button(self.frame, bg='black',borderwidth=4, fg='white', width=6, height=1)
    temaEscuro.place(x=270,y=180)

    som = Button(self.frame,bg='#d9d9d9',borderwidth=4, text='Tema de fundo', fg='black', width=15, font='Ivy 16',command=lambda:play())
    som.place(x=30,y=230)

    def play():
        playsound('btm2.mp3')

