import requests
import sqlite3

def criarTabela():
  con.execute('CREATE TABLE IF NOT EXISTS endereco(id integer PRIMARY KEY AUTOINCREMENT, rua string, cep string);')
  con.commit()

  print("Tabela criada com sucesso!");

def inserirNaTabela(dadosLogradouro, cep):
  con.execute("INSERT INTO endereco(rua, cep) VALUES(?, ?)",(dadosLogradouro,cep))
  con.commit()

  print('Dados inseridos com sucesso')

def mostrarTabela():
  print("")
  consulta = con.execute('SELECT * FROM endereco;')
  select = consulta.fetchall()
  print(select)


con = sqlite3.connect('cep')
print("Conexão aberta!");
criarTabela()

cep = input('CEP: ')

url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

if response.status_code == 200:
  dadosLogradouro = response.json()['logradouro']
  inserirNaTabela(dadosLogradouro, cep)
  mostrarTabela()

else:
    print(response.status_code)
    print("Erro: Consulta indisponível")
