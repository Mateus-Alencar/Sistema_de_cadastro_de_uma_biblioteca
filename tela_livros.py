from banco import pesquisar_livros, status_livro, add_emprestimo, excluir_livro, excluir_emprestimo
from f_tela_base import *
from tela_cadastro_livros import *
from tkinter import ttk
from PIL import ImageTk, Image

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
    barra_pesquisa = Entry(self.frame,width=25, justify='left',font='Arial 16 bold', relief='solid')
    barra_pesquisa.place(x=80,y=10)
    label = Label(self.frame, text='Livro: ',bg='#d9d9d9', font='Arial 15 bold')
    label.place(x=10,y=10)
    label = Button(self.frame, text='Pesquisar',bd=5,relief='solid', font='Arial 15 bold', command=lambda:frame_livro(self, barra_pesquisa.get()))
    label.place(x=385,y=4)

    self.frame_l = Frame(self.frame, width=530,height=600, bg='white')
    self.frame_l.place(x=0,y=70)


    #Create a Main Frame
    main_frame = Frame(self.frame_l)
    main_frame.pack(fill=BOTH, expand=1)
    #reate a Canvas
    my_canvas = Canvas(main_frame, height=620, width=500)
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    # Add a scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    #Configure the Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox('all')))
    #Create another frame inside the canvas
    second_frame = Frame(my_canvas)
    #Add that new frame to a window in the canvas
    my_canvas.create_window((0,0), window=second_frame, anchor='nw')
    pesquisar_livros(self)
    linhas = self.linhas

    #for linha in linhas:
    ##    self.imagens = PhotoImage(file=f'capa_livros/{linha[0]}.png')
    #cont = 0
    for linha in linhas:
        frame = Frame(second_frame,width=530, height=190, bg='#696969')
        frame.pack()

        imagem = Image.open(f'capa_livros/{linha[0]}.png')
        self.imagemL = ImageTk.PhotoImage(imagem)
        label = Button(frame,bg='black',image=self.imagemL, height=150, width=120)
        label.image = self.imagemL
        label.place(x=10,y=20)

        label_titulo = Label(frame, text=str(linha[0]),bg="#d9d9d9",font=('Ivy 15'))
        label_titulo.place(x=180,y=20)
        label_autor = Label(frame, text=str(linha[1]),bg="#d9d9d9",font=('Ivy 15'))
        label_autor.place(x=180,y=60)
        status_livro(self)
        self.status = 'Disponível'
        for livro in self.emprestimos_banco:
            print(livro)
            if linha[0] == livro[0]:
                if livro[3] == None:
                    self.status = 'Emprestado'
        self.emprestimo_status = Label(frame, text=self.status,font='Ivy 15', bg='#d9d9d9')
        self.emprestimo_status.place(x=390,y=130)


def frame_livro(self, titulo):
    #Cria um frame em cima do Self.frame para mostrar os dados do livro
    for l in self.linhas:
        if l[0] == titulo:
            linha = l
    frame_esp = Frame(self.frame, width=450,height=550,bd=3,relief='groove', bg='white')
    frame_esp.place(x=20, y= 100)

    self.imagem_qrcode = PhotoImage(file='qrcode.png')
    label = Label(frame_esp,bg="#d9d9d9", image=self.imagem_qrcode, width=150, height=150)
    label.place(x=160,y=10)

    label = Label(frame_esp, text='Título:',bg="white",font=('Ivy 15'))
    label.place(x=20,y=160)
    label = Label(frame_esp, text=str(linha[0]),bg="white",font=('Ivy 15'))
    label.place(x=100,y=160)
    label = Label(frame_esp, text='Autor:',bg="white",font=('Ivy 15'))
    label.place(x=20,y=200)
    label = Label(frame_esp, text=str(linha[1]),bg="white",font=('Ivy 15'))
    label.place(x=100,y=200)

    label_text = Label(frame_esp,bg="#d9d9d9",wraplength=180,text=linha[2],font=('Ivy 12'), width=45, height=13)
    label_text.place(x=10,y=250)

    self.emprestimo = Button(frame_esp, text=self.status,font='Ivy 15', bg='#d9d9d9', command=lambda:trocar_status(self, linha))
    self.emprestimo.place(x=180,y=500)

    botao_excluir_livro = Button(frame_esp, text='Excluir', font='Ivy 14', relief='solid', bg='red', fg='black', command=lambda:excluir_livro(linha[0]))
    botao_excluir_livro.place(x=20, y=500)

    sair = Button(frame_esp, text='SAIR',font='Ivy 8', bg='#d9d9d9', command=lambda:sair(frame_esp))
    sair.place(x=400,y=520)

    def sair(frame):
        frame.destroy()

    def trocar_status(self, linha):
        frame_status = Frame(self.frame, width=450,height=550,bd=3,relief='groove', bg='white')
        frame_status.place(x=20, y=100)

        self.label_n_l = Label(frame_status, font='Ivy 18',bg='white', text=linha[0])
        self.label_n_l.place(x=40,y=30 )
        linha_ = Label(frame_status,bg='white', text='______________________________________________________________________________________', font='Ivy 8 bold')
        linha_.place(x=0,y=60)

        label = Label(frame_status,bg='white', font='Arial 15', text='Nome cliente:')
        label.place(x=20,y=120)
        self.entry_cliente = Entry(frame_status,bd=3,relief='solid', font='Arial 13')
        self.entry_cliente.place(x=160,y=120)

        label = Label(frame_status,bg='white', font='Arial 15', text='Data emprestimo:')
        label.place(x=20 ,y= 160)
        self.entry_data_emprestimo = Entry(frame_status,bd=3,relief='solid', font='Arial 13')
        self.entry_data_emprestimo.place(x=180 ,y=160 )

        label = Label(frame_status,bg='white', font='Arial 15', text='Data devolução:')
        label.place(x=20 ,y=200)
        self.entry_data_devolucao = Entry(frame_status,bd=3,relief='solid', font='Arial 13')
        self.entry_data_devolucao.place(x=180 ,y=200 )

        label = Label(frame_status,bg='white', font='Ivy 12', text='Data --> "aaaa-mm-dd"')
        label.place(x=20 ,y=230)

        botao = Button(frame_status, text='OK', font='Arial 15', bd=5,relief='groove', command=lambda:adicionar_emprestimo(self, linha[0]))
        botao.place(x=190,y=250)

        sair2 = Button(frame_status, text='SAIR',font='Ivy 8', bg='#d9d9d9', command=lambda:sair(frame_status))
        sair2.place(x=400,y=520)
        
        def adicionar_emprestimo(self, titulo):
            if self.status == 'Disponível':
                excluir_emprestimo(titulo)
                add_emprestimo(self)
                self.status = 'Emprestado'
            if self.status == 'Emprestado':
                excluir_emprestimo(titulo)
                add_emprestimo(self)
                self.status = 'Disponível'



'''
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
'''