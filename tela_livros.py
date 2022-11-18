from banco import pesquisar_livros
from f_tela_base import *
from tela_cadastro_livros import *
from tkinter import ttk

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
    self.frame_l = Frame(self.frame, width=530,height=600, bg='white')
    self.frame_l.place(x=0,y=0)


    #Create a Main Frame
    main_frame = Frame(self.frame_l)
    main_frame.pack(fill=BOTH, expand=1)
    #reate a Canvas
    my_canvas = Canvas(main_frame, height=700, width=500)
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
    print(linhas)
    c=0
    for linha in linhas:
        frame = Frame(second_frame,width=530, height=190, bg='#696969')
        frame.pack()
        #self.path = linha[3]
        #self.img = ImageTk.PhotoImage(Image.open(self.path))
        self.label = Label(frame,text='im',bg="#d9d9d9",font=('Ivy 25'))
        self.label.place(x=10,y=20)
        label = Label(frame, text=str(linha[0]),bg="#d9d9d9",font=('Ivy 15'))
        label.place(x=200,y=10)
        label = Label(frame, text=str(linha[1]),bg="#d9d9d9",font=('Ivy 15'))
        label.place(x=200,y=50)
        emprestimo = Button(frame, text='status',font='Ivy 15', bg='#d9d9d9')
        emprestimo.place(x=430,y=140)
        c = c + 200


        #label = Label(f, text=str(linha[3]),bg="#d9d9d9",font=('Ivy 15'))
        #label.grid(column=4, row=1)


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