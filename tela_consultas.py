from f_tela_base import *

def tela_consultas(self):
    self.frame.destroy()
    self.frame = Frame(self.window, width='530', height='810', bg='#d9d9d9')
    self.frame.place(x='0', y='90')

    botao_livros = Button(self.frame, text='Livros', bg='#002dd2', fg='white',width=37, font='Ivy 18')
    botao_livros.place(x=0, y=5)
    botao_emprestimos = Button(self.frame, text='Empréstimos', bg='#002dd2', fg='white',width=37, font='Ivy 18')
    botao_emprestimos.place(x=0, y=50)
    botao_historico = Button(self.frame, text='Histórico', bg='#002dd2', fg='white',width=37, font='Ivy 18')
    botao_historico.place(x=0, y=90)

    self.frame_list_consult = Frame(self.frame)
    self.frame_list_consult.place(x=0,y=140)
    
    def consult_livros():
        pass
    def consult_emprestimos():
        pass
    def historico():
        pass

    self.frame_list = Frame(self.frame, width='530', height='600',bg='white')
    self.frame_list.place(x=0,y=130)

    self.img_voltar = PhotoImage(file='voltar.png')
    self.botao_voltar = Button(self.frame, image=self.img_voltar,borderwidth=0,bg='#d9d9d9', width=48,height=48, command=lambda:self.voltar_app())
    self.botao_voltar.place(x=10,y=745)