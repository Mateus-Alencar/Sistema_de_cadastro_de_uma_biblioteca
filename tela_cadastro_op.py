from f_tela_base import *

def icon_comeco(self, usu):
    self.frame.destroy()
    self.frame = Frame(self.window, width='530', height='810', bg='#d9d9d9')
    self.frame.place(x='0', y='90')
    self.img_livros = PhotoImage(file='pilha_de_livros.png')
    self.icon=Label(self.frame, image=self.img_livros, width=140, height=140, bg='#d9d9d9')
    self.icon.place(x=200, y= 40)
    
    if usu == self.funcionario:
        label = Label(self.frame, text='Funcionário', font='Arial 20 bold', bg='#d9d9d9', fg='black')
        label.place(x=190, y= 190)
    elif usu == self.cliente:
        label = Label(self.frame, text='Cliente', font='Arial 20 bold', bg='#d9d9d9', fg='black')
        label.place(x=190, y= 190)
    elif usu == self.login:
        label = Label(self.frame, text='Login', font='Arial 20 bold', bg='#d9d9d9', fg='black')
        label.place(x=190, y= 190)
        

    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.window, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_app(self.frame))
    self.botao_voltar.place(x=10,y=845)

def tela_cadastroCliente(self, usu):
    icon_comeco(self, usu)
    nome = Label(self.frame, text='Nome: ',bg="#d9d9d9",font=('Ivy 15'))
    nome.place(x=35,y=300)
    entry_nome = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_nome.place(x=130,y=300)

    email = Label(self.frame, text='E-mail: ',bg="#d9d9d9",font=('Ivy 15'))
    email.place(x=35,y=350)
    entry_email = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_email.place(x=130,y=350)

    senha = Label(self.frame, text='Senha: ',bg="#d9d9d9",font=('Ivy 15'))
    senha.place(x=35,y=400)
    entry_senha = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_senha.place(x=130,y=400)

def tela_cadastroFuncionario(self, usu):
    icon_comeco(self, usu)
    nome = Label(self.frame, text='Nome: ',bg="#d9d9d9",font=('Ivy 15'))
    nome.place(x=35,y=300)
    entry_nome = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_nome.place(x=130,y=300)

    email = Label(self.frame, text='E-mail: ',bg="#d9d9d9",font=('Ivy 15'))
    email.place(x=35,y=350)
    entry_email = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_email.place(x=130,y=350)
    
    senha = Label(self.frame, text='Senha: ',bg="#d9d9d9",font=('Ivy 15'))
    senha.place(x=35,y=400)
    entry_senha = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_senha.place(x=130,y=400)

    cpf = Label(self.frame, text='CPF: ',bg="#d9d9d9",font=('Ivy 15'))
    cpf.place(x=35,y=450)
    entry_cpf = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_cpf.place(x=130,y=450)

def tela_login(self, usu):
    icon_comeco(self, usu)
    label_email = Label(self.frame, text='E-mail: ',bg="#a9a9a9",font=('Ivy 15'))
    label_email.place(x=35, y=300)
    entry_email = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_email.place(x=100,y=300)

    label_senha = Label(self.frame, text='Senha: ',bg="#a9a9a9",font=('Ivy 15'))
    label_senha.place(x=35, y=350)
    entry_senha = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_senha.place(x=100,y=350)
