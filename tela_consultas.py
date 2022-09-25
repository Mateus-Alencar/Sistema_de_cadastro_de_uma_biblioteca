from f_tela_base import *

def tela_consultas(self, frame, consulta):
    frame.destroy()
    if consulta == self.emprestimos:
        pass
    if consulta == self.consultar:
        pass

    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.window, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_app())
    self.botao_voltar.place(x=10,y=845)