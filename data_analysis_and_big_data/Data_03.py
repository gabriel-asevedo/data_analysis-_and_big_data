#1
import pandas as pd

#2
df_players = pd.read_excel('/content/jogadores.xlsx')

#3
df_players

"""# Nova seção"""

#4
df_players.dropna(inplace = True)
df_players

#5
df_players['salario_anual'] = df_players['salario'] * 12
df_players

#6
df_players['Nome'] = df_players.Nome.str.upper()
df_players

#7
pd.set_option('display.precision', 2)
df_players.describe()

# Count = indica que foram lidos 4 valores de salário não nulos
# Mean  = indica que a média dos salários foi de $312500,00
# Std   = indica que houve uma dispersão de dados, sendo que o valor do desvio padrão foi relativamente alto em comparação com a média, uma vez que temos
#         o jogador Everson recebendo $850.000 e todos os outros jogadores recebendo abaixo de $200.000, evidenciando uma grande variação.
# Min   = indica o menor valor entre os salários, sendo o do jogador Fábio com $100.000
# Max   = indica o maior valor entre os salários, sendo o do jogador Everson com $850.000

# 25%(Q1, Primeiro Quartil) = indica que 25% dos jogadores possuem o salário menor que $137.500
# 50%(Q2, Mediana)          = indica que 50 % dos jogadores possuem o salario menor que $150.000 e os outros 50% possuem o salário maior que esse valor.
# 75%(Q3, terceiro Quartil) = indica que 75% dos jogadores possuem o salário menor que $325.000

#8
# a)
df_players[(df_players['salario'] > 200000)][['Nome', 'Time']]

# a) (query)
##df_players.query('salario > 200000')[['Nome', 'Time']]

# b)
df_players[df_players['Nome'].str.contains('u', case=False)][['Nome', 'Time']]

# b) (query)
df_players.query("Nome.str.contains('u', case=False)")[['Nome', 'Time']]

# c)
df_players.sort_values(by = 'salario', ascending = False)[['Nome', 'salario', 'Time']]

# d)
df_players.sort_values(by = ['Time', 'salario'], ascending = [True, False])[['Nome', 'salario', 'Time']]

# e)
df_players.groupby(['Time'])['Nome'].count()

# f)
df_players.groupby('Time')['salario'].mean()
