from f_tela_base import *

def icon_comeco(self, usu):
    self.frame.destroy()
    self.frame = Frame(self.window, width='550', height='400', bg='#d9d9d9')
    self.frame.place(x='190', y='70')
    self.img_livros = PhotoImage(file='pilha_de_livros.png')
    self.icon=Label(self.frame, image=self.img_livros, width=140, height=140, bg='#d9d9d9')
    self.icon.pack()
    if usu == self.funcionario:
        label = Label(self.frame, text='Funcionário', font='Arial 20 bold', bg='#d9d9d9', fg='black')
        label.pack()
    else:
        label = Label(self.frame, text='Cliente', font='Arial 20 bold', bg='#d9d9d9', fg='black')
        label.pack()

    self.frame2 = Frame(self.frame).pack()
    button_cadastar = Button(self.frame2, text=('Cadastrar'), font='Arial 16 bold', width=10, height=2, bg='#00c2cb', fg='black')
    button_cadastar.place(x=195, y= 660)
    button_login = Button(self.frame2, text=('Login'), font='Arial 16 bold', width=10, height=2, bg='#00c2cb', fg='black')
    button_login.place(x=195, y= 740)

    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.window, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_app(self.frame))
    self.botao_voltar.place(x=10,y=845)

def tela_cadastroCliente(self, usu):
    icon_comeco(self, usu)
    nome = Label(self.frame2, text='Nome: ',bg="#d9d9d9",font=('Ivy 15'))
    nome.place(x=35,y=300)
    entry_nome = Entry(self.frame2, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_nome.place(x=130,y=300)

    email = Label(self.frame2, text='E-mail: ',bg="#d9d9d9",font=('Ivy 15'))
    email.place(x=35,y=350)
    entry_email = Entry(self.frame2, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_email.place(x=130,y=350)

    senha = Label(self.frame2, text='Senha: ',bg="#d9d9d9",font=('Ivy 15'))
    senha.place(x=35,y=400)
    entry_senha = Entry(self.frame2, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_senha.place(x=130,y=400)

def tela_cadastroFuncionario(self, usu):
    icon_comeco(self, usu)
    nome = Label(self.frame2, text='Nome: ',bg="#d9d9d9",font=('Ivy 15'))
    nome.place(x=35,y=300)
    entry_nome = Entry(self.frame2, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_nome.place(x=130,y=300)

    email = Label(self.frame2, text='E-mail: ',bg="#d9d9d9",font=('Ivy 15'))
    email.place(x=35,y=350)
    entry_email = Entry(self.frame2, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_email.place(x=130,y=350)
    
    senha = Label(self.frame2, text='Senha: ',bg="#d9d9d9",font=('Ivy 15'))
    senha.place(x=35,y=400)
    entry_senha = Entry(self.frame2, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_senha.place(x=130,y=400)

    cpf = Label(self.frame2, text='CPF: ',bg="#d9d9d9",font=('Ivy 15'))
    cpf.place(x=35,y=450)
    entry_cpf = Entry(self.frame2, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_cpf.place(x=130,y=450)