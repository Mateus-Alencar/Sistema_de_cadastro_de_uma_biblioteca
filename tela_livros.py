from tkinter import ttk
from banco import pesquisar_livros
from f_tela_base import *
from tela_cadastro_livros import *


def tela_livros(self):
    self.frame.destroy()
    self.frame = Frame(self.window, width='530', height='850', bg='#d9d9d9')
    self.frame.place(x='0', y='90')

    selecao_livros(self)

    linha = Label(self.frame,bg='#d9d9d9', text='______________________________________________________________________________________', font='Ivy 8 bold')
    linha.place(x=0,y=700)
    link_tela_cadastro_livros = Button(self.frame, text='Cadastrar livro', fg='white', font='Ivy 12 bold', borderwidth=0, bg='black', width=16 ,height=2, command=lambda:tela_cadastrarLivros(self))
    link_tela_cadastro_livros.place(x=330,y=740)
    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.frame, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_app())
    self.botao_voltar.place(x=10,y=745)

def selecao_livros(self):
    frame = Frame(self.frame, width=530, height=450, bg='white')
    frame.place(x=0,y=0)

    # add some style
    style = ttk.Style()
    # Pick a theme
    style.theme_use('default')
    # Configure our treeview colors
    style.configure('Treeview',
        background='silver', 
        foreground='black', 
        fieldbackground='silver', 
        font='Arial 14 bold')


    treev = ttk.Treeview(frame, selectmode ='browse', height=35, ) 
    treev.pack(side ='right') 
    verscrlbar = ttk.Scrollbar(frame,  
                            orient ="vertical",  
                            command = treev.yview) 
    verscrlbar.pack(side ='left', fill ='x') 
    treev.configure(xscrollcommand = verscrlbar.set) 
    treev["columns"] = ("1", "2", "3") 
    treev['show'] = 'headings'
    treev.column("1", width = 140, anchor ='c') 
    treev.column("2", width = 140, anchor ='c') 
    treev.column("3", width = 220, anchor ='c') 
    treev.heading("1", text ="titulo") 
    treev.heading("2", text ="autor") 
    treev.heading("3", text ="descrição")

    pesquisar_livros(self)
    linhas = self.linhas

    for linha in linhas:
        treev.insert('', END, values=linha)