from f_tela_base import *

def icon_comeco(self, usu):
    self.window.destroy()
    tela_padrao(self)
    self.frame=Frame(self.window, bg='#D9D9D9')
    self.img_livros = PhotoImage(file='pilha_de_livros.png')
    self.frame.pack()
    self.icon=Label(self.frame, image=self.img_livros, width=140, height=140, bg='#d9d9d9')
    self.icon.pack()
    if usu == self.funcionario:
        label = Label(self.frame, text='Funcionário', font='Arial 20 bold', bg='#d9d9d9', fg='black')
        label.pack()
    else:
        label = Label(self.frame, text='Cliente', font='Arial 20 bold', bg='#d9d9d9', fg='black')
        label.pack()

    self.frame2 = Frame(self.window).pack()
    button_cadastar = Button(self.frame2, text=('Cadastrar'), font='Arial 16 bold', width=10, height=2, bg='#00c2cb', fg='black')
    button_cadastar.place(x=180, y= 660)
    button_login = Button(self.frame2, text=('Login'), font='Arial 16 bold', width=10, height=2, bg='#00c2cb', fg='black')
    button_login.place(x=180, y= 740)

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
    