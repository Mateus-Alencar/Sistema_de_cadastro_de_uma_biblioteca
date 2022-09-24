from f_tela_base import *

def tela_livros(self, frame):
    frame.destroy()
    self.frame = Frame(self.window, width='550', height='400', bg='#d9d9d9')
    self.frame.place(x='0', y='70')