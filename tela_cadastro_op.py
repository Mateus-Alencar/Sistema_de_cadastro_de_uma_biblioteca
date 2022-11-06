from f_tela_base import *
from tela_app import *
from banco import *

def icon_comeco(self, usu):
    #Mudanças de campos e elementos, na tela de cadastro, dependendo do tipo de usuário ou serviço
    self.frame.destroy()
    barraAzul = Frame(self.window,borderwidth=0, width=520, height=80, bg='#004aad')
    barraAzul.place(x=0,y=0)
    self.frame = Frame(self.window, width='530', height='810', bg='#d9d9d9')
    self.frame.place(x='0', y='80')
    self.ex()
    self.img_livros = PhotoImage(file='pilha_de_livros.png')
    self.icon=Label(self.frame, image=self.img_livros, width=140, height=140, bg='#d9d9d9')
    self.icon.place(x=180, y= 40)

    self.btm_cadastrar = Button(self.frame, bg='black',borderwidth=4, fg='white',width=15, font='Ivy 16', command=None)
    self.btm_cadastrar.place(x=170, y=510)
    label = Label(self.frame, font='Arial 20 bold', bg='#d9d9d9', fg='black')
    label.place(x=190, y= 190)
    
    if usu == self.funcionario:
        label['text'] = 'Funcionário'
        self.btm_cadastrar['text'] = 'Cadastrar'
    elif usu == self.cliente:
        label['text'] = 'Cliente'
        self.btm_cadastrar['text'] = 'Cadastrar'
    elif usu == self.login:
        label['text'] = 'Login'
        self.btm_cadastrar['text'] = 'Login'
        

    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.frame, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_tela_cadastros())
    self.botao_voltar.place(x=10,y=745)

def tela_cadastroCliente(self, usu):
    #Informações: nome, email e senha.
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
    entry_senha = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid',show='*')
    entry_senha.place(x=130,y=400)
    self.btm_cadastrar['command'] = lambda:cadastrar_cliente(entry_nome.get(), entry_email.get(), entry_senha.get())

def tela_cadastroFuncionario(self, usu):
    #especificações: nome, email, senha e cpf
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
    entry_senha = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid',show='*')
    entry_senha.place(x=130,y=400)

    cpf = Label(self.frame, text='CPF: ',bg="#d9d9d9",font=('Ivy 15'))
    cpf.place(x=35,y=450)
    entry_cpf = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_cpf.place(x=130,y=450)
    
    self.btm_cadastrar['command'] = lambda:cadastrar_funcionario(entry_nome.get(), entry_email.get(), entry_senha.get(), entry_cpf.get())
def tela_login(self, usu):
    #Irá pedir o email e senha para verificar no banco --> banco_biblioteca
    icon_comeco(self, usu)
    label_email = Label(self.frame, text='E-mail: ',bg="#a9a9a9",font=('Ivy 15'))
    label_email.place(x=35, y=300)
    entry_email = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    entry_email.place(x=130,y=300)

    label_senha = Label(self.frame, text='Senha: ',bg="#a9a9a9",font=('Ivy 15'))
    label_senha.place(x=35, y=350)
    entry_senha = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid', show='*')
    entry_senha.place(x=130,y=350)
    self.btm_cadastrar['command']=lambda:login(self, entry_email.get(), entry_senha.get())

