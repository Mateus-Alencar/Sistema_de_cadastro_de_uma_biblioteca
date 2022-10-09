from tkinter import scrolledtext
from f_tela_base import *


def tela_config(self):
    self.frame.destroy()
    self.barraMenu['text']=''
    self.frame = scrolledtext.ScrolledText(self.window, width='530', height='810', bg='#d9d9d9')
    self.frame.place(x='0', y='80')

    config_label = Label(self.frame, bg='black',borderwidth=4, text='Configurações', fg='white', width=15, font='Ivy 16')
    config_label.place(x=100,y=120)
    tema_label = Label(self.frame, bg='black',borderwidth=4, text='Tema de fundo', fg='white', width=15, font='Ivy 16')
    tema_label.place(x=120,y=180)
    temaBranco = Button(self.frame, bg='white',borderwidth=4, fg='white', width=15, font='Ivy 16', height=1)
    temaBranco.place(x=50,y=240)
    temaEscuro = Button(self.frame, bg='black',borderwidth=4, fg='white', width=15, font='Ivy 16', height=1)
    temaEscuro.place(x=200,y=1240)
