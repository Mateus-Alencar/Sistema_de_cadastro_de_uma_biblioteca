import mysql.connector
from mysql.connector import Error
from f_tela_base import *
from tela_app import *


def consulta_banco():
  mydb = None
  try:
    mydb = mysql.connector.connect(host="localhost", user="root", database = "banco_biblioteca")
    print('conexão realizada com sucesso!!!')
  except Error as err:
    print(f"Error: {err}")
  return mydb


def cadastrar_cliente():
  db = consulta_banco()
  mycursor = (db).cursor()
  sql = "INSERT INTO clientes (nome, email, senha) VALUES ('1','1','1')"
  mycursor.execute(sql)
  mycursor.close()
  db.commit()
  db.close()

def cadastrar_funcionario():
  db = consulta_banco()
  mycursor = db.cursor()
  sql = "INSERT INTO funcionarios (nome, email, senha, cpf) VALUES ('1','1','1','1')"
  mycursor.execute(sql)
  mycursor.close()
  db.commit()
  db.close()

def login(self, email, senha):
  db = consulta_banco()
  mycursor = db.cursor()
  sql = f'''SELECT clientes.email, clientes.senha, funcionarios.email, funcionarios.senha 
            FROM clientes, funcionarios 
            WHERE clientes.email = {email} and clientes.senha = {senha} or funcionarios.email = {email} and funcionarios.senha = {senha}
  '''
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  print(myresult)
  tempo(self)
  if senha and email in myresult[0]:
    mycursor.close()
    db.commit()
    db.close()
    tela_app(self)
  else:
    info = Label(self.frame, font='Arial 12 bold', text='Este usuário não existe', bg='#d9d9d9')
    info.place(x=160,y=480)
  

def cadastrar_livro():
  db = consulta_banco()
  mycursor = db.cursor()
  sql = ""
  mycursor.execute(sql)
  mycursor.close()
  db.commit()
  db.close()

