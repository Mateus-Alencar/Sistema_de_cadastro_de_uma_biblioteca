from f_tela_base import *

def tela_livros(self, frame):
    frame.destroy()
    self.frame = Frame(self.window, width='550', height='400', bg='#d9d9d9')
    self.frame.place(x='0', y='70')

    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.window, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_app())
    self.botao_voltar.place(x=10,y=845)