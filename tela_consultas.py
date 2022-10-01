from f_tela_base import *

def tela_consultas(self, frame, consulta):
    frame.destroy()
    self.frame = Frame(self.window, width='530', height='770', bg='#d9d9d9')
    self.frame.place(x='2', y='90')

    botao_livros = Button(self.frame, text='Livros', bg='#002dd2', fg='white',width=36, font='Ivy 18')
    botao_livros.place(x=1, y=0)
    botao_emprestimos = Button(self.frame, text='Empréstimos', bg='#002dd2', fg='white',width=36, font='Ivy 18')
    botao_emprestimos.place(x=1, y=40)
    botao_historico = Button(self.frame, text='Histórico', bg='#002dd2', fg='white',width=36, font='Ivy 18')
    botao_historico.place(x=1, y=80)

    frame_table = Frame(self.frame).place(x=1,y=130)

    self.lista = [(1,'Raj','Mumbai',19), 
       (2,'Aaryan','Pune',18), 
       (3,'Vaishnavi','Mumbai',20), 
       (4,'Rachna','Mumbai',21), 
       (5,'Shubham','Delhi',21)]
    total_rows = len(self.lista) 
    total_columns = len(self.lista[0])
    tabela(self, total_rows, total_columns)
    def tabela(self, r, c):
        #bd
        for i in range(r): 
                for j in range(c): 
                    self.list = Entry(self.frame, width=20, fg='blue', font=('Arial',16,'bold')) 
                    self.list.grid(row=i, column=j)
                    self.list.insert(END, self.lista[i][j])
                   

    if consulta == self.emprestimos:
        pass
    if consulta == self.consultar:
        pass

    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.window, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_app(self.frame))
    self.botao_voltar.place(x=10,y=845)