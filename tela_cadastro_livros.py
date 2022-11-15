from tkinter import filedialog
from turtle import width
from f_tela_base import *
from banco import cadastrar_livro

#Referente a tela de consulta
def tela_cadastrarLivros(self):
    self.frame.destroy()
    self.frame = Frame(self.window, width='550', height='850',bg='#d9d9d9')
    self.frame.place(x='2', y='90')

    label_titulo = Label(self.frame, text='Titulo: ',bg="#a9a9a9",font=('Ivy 15'))
    label_titulo.place(x=35, y=100)
    self.entry_titulo = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    self.entry_titulo.place(x=120,y=100)

    label_autor = Label(self.frame, text='Autor: ',bg="#a9a9a9",font=('Ivy 15'))
    label_autor.place(x=35, y=150)
    self.entry_autor = Entry(self.frame, width=25, justify='left',font='Arial 15 bold', relief='solid')
    self.entry_autor.place(x=120,y=150)

    label_descricao = Label(self.frame, text='Descrição:',bg="#a9a9a9",font=('Ivy 15'))
    label_descricao.place(x=35, y=200)
    self.entry_descricao = Entry(self.frame, width=25,font='Arial 15 bold', relief='solid')
    self.entry_descricao.place(x=140,y=200)

    label_foto = Label(self.frame, text='Imagem:',bg="#a9a9a9",font=('Ivy 15'))
    label_foto.place(x=35, y=250)
    self.entry_foto = Button(self.frame, width=25,text='selecionar imagem', height=2, justify='left', relief='solid', command=lambda:filenames(self))
    self.entry_foto.place(x=140,y=250)


    botao_salvar = Button(self.frame, text='Salvar', bg='red', fg='white',width=18, font='Ivy 18', command=lambda:salvar(self))
    botao_salvar.place(x=120, y=500)
    botao_cancelar = Button(self.frame, text='Cancelar', bg='red', fg='white',width=18, font='Ivy 18', command=lambda:cancelar(self))
    botao_cancelar.place(x=120, y=550)

    def filenames(self):
        #selecionar o caminho para a imagem
        file = filedialog.askopenfilenames(initialdir='C:/')
        self.file = str(file)
        self.entry_foto['text'] = f'{file}'

    def salvar(self):
        cadastrar_livro(self.entry_titulo.get(), self.entry_autor.get(), self.entry_descricao.get(), self.file)

    def cancelar(self):
        #Limpa os campos prenchidos
        self.entry_titulo.delete(0, END)
        self.entry_autor.delete(0, END)
        self.entry_descricao.delete(0, END)
        self.file = ''
        self.entry_foto['text'] = 'selecionar imagem'
        

    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.frame, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_app())
    self.botao_voltar.place(x=10,y=745)