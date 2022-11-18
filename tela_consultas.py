from tkinter import ttk
from banco import pesquisar_livros
from f_tela_base import *


def tela_consultas(self):
    self.frame.destroy()
    self.frame = Frame(self.window, width='530', height='810', bg='#d9d9d9')
    self.frame.place(x='0', y='90')

    botao_livros = Button(self.frame, text='Livros', bg='#002dd2', fg='white',width=37, font='Ivy 18', command=lambda:consulta_livros(self))
    botao_livros.place(x=0, y=5)
    botao_emprestimos = Button(self.frame, text='Empréstimos', bg='#002dd2', fg='white',width=37, font='Ivy 18')
    botao_emprestimos.place(x=0, y=50)
    botao_historico = Button(self.frame, text='Histórico', bg='#002dd2', fg='white',width=37, font='Ivy 18')
    botao_historico.place(x=0, y=90)

    self.frame_list = Frame(self.frame, width=530, height=600, bg='white')
    self.frame_list.place(x=0,y=140)

    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.frame, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_app())
    self.botao_voltar.place(x=10,y=745)
def consulta_livros(self):
    frame = Frame(self.frame_list, width=530, height=600, bg='white')
    frame.pack()

    treev = ttk.Treeview(frame, selectmode ='browse', height=25) 
    treev.pack(side ='right') 
    verscrlbar = ttk.Scrollbar(frame,  
                            orient ="vertical",  
                            command = treev.yview) 
    verscrlbar.pack(side ='right', fill ='x') 
    treev.configure(xscrollcommand = verscrlbar.set) 
    treev["columns"] = ("1", "2", "3") 
    treev['show'] = 'headings'
    treev.column("1", width = 140, anchor ='c') 
    treev.column("2", width = 120, anchor ='se') 
    treev.column("3", width = 220, anchor ='se') 
    treev.heading("1", text ="titulo") 
    treev.heading("2", text ="autor") 
    treev.heading("3", text ="descrição")

    pesquisar_livros(self)
    linhas = self.linhas

    for linha in linhas:
        treev.insert('', END, values=linha)

def consult_emprestimos():
    pass
def historico():
    pass
