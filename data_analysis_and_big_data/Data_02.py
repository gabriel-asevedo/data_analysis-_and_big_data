import requests
import sqlite3

def createTable() :
  con.execute('CREATE TABLE IF NOT EXISTS endereco(id integer PRIMARY KEY AUTOINCREMENT, country string, cases float);')
  con.commit()
  print("Table created successfully!")

def insertInTable(country, cases):
  con.execute("INSERT INTO endereco(country, cases) VALUES(?, ?)",(country, cases))
  con.commit()
  print("Data entered successfully!")

def updateTable():
  con.execute(' UPDATE endereco SET country = ? WHERE id = ?', ('PaisQualquer',1))
  con.commit()

def showTable():
  print("")
  query = con.execute('SELECT * FROM endereco;')
  select = query.fetchall()
  print(select)

###

con = sqlite3.connect('covidCases')
print("Open connection!")
createTable()

country = input('Enter a country: ')

url = f"https://disease.sh/v3/covid-19/countries/{country}"
response = requests.get(url)

if response.status_code == 200:
  cases = response.json()['cases']
  cases = f'{cases:_.2f}'
  cases = cases.replace('.' ,  ',').replace('_' ,  '.')
  print(f'Covid cases in {country}: {cases}')
  insertInTable(country, cases)
  showTable()

else:
    print(response.status_code)
    print("Error: query unavailablel")

updateTable()
showTable()
