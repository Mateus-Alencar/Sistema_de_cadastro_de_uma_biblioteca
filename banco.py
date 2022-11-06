import mysql.connector
from mysql.connector import Error
from f_tela_base import *
from tela_app import *


def consulta_banco():
  #Acessar ao banco --> banco_biblioteca
  mydb = None
  try:
    mydb = mysql.connector.connect(host="localhost", user="root", database = "banco_biblioteca")
    print('conexão realizada com sucesso!!!')
  except Error as err:
    print(f"Error: {err}")
  return mydb


def cadastrar_cliente(nome, email, senha):
  db = consulta_banco()
  mycursor = (db).cursor()
  sql1 = ('''
    CREATE TABLE IF NOT EXISTS clientes(
    nome TEXT,
    email TEXT,
    senha TEXT
  )
  ''')
  sql2 = f'INSERT INTO clientes (nome, email, senha) VALUES ("{str(nome)}","{str(email)}","{str(senha)}")'
  mycursor.execute(sql1)
  mycursor.execute(sql2)
  mycursor.close()
  db.commit()
  db.close()

def cadastrar_funcionario(nome, email, senha, cpf):
  db = consulta_banco()
  mycursor = db.cursor()
  sql1 = ('''
    CREATE TABLE IF NOT EXISTS funcionarios(
    nome TEXT,
    email TEXT,
    senha TEXT,
    cpf TEXT
  )
  ''')
  sql2 = f'INSERT INTO funcionarios (nome, email, senha, cpf) VALUES ("{str(nome)}","{str(email)}","{str(senha)}","{str(cpf)}")'
  mycursor.execute(sql1)
  mycursor.execute(sql2)
  mycursor.close()
  db.commit()
  db.close()

def login(self, email, senha):
  db = consulta_banco()
  mycursor = db.cursor()
  sql = f'''SELECT clientes.email, clientes.senha, funcionarios.email, funcionarios.senha 
            FROM clientes, funcionarios 
            WHERE clientes.email = "{str(email)}" and clientes.senha = "{str(senha)}" or funcionarios.email = "{str(email)}" and funcionarios.senha = "{str(senha)}"
  '''
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  print(myresult)
  tempo(self)
  if senha and email in myresult[0]:
    mycursor.close()
    db.commit()
    db.close()
    self.t_app()
  else:
    info = Label(self.frame, font='Arial 12 bold', text='Este usuário não existe', bg='#d9d9d9')
    info.place(x=160,y=480)
  

def cadastrar_livro(titulo, autor, descricao, imagem):
  db = consulta_banco()
  mycursor = db.cursor()
  sql1 = ('''
    CREATE TABLE IF NOT EXISTS livros(
    titulo TEXT,
    autor TEXT,
    descricao TEXT,
    imagem TEXT
  )
  ''')
  sql2 = f'INSERT INTO livros (titulo, autor, descricao, imagem) VALUES ("{titulo}","{autor}","{descricao}","{imagem}")'
  mycursor.execute(sql1)
  mycursor.execute(sql2)
  mycursor.close()
  db.commit()
  db.close()

