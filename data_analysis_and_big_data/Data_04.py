import pandas as pd

products = pd.read_excel('/content/Produtos.xlsx')

experimental_data = pd.read_csv('/content/dados_experimentos.csv')

products

products.describe()

products['Moeda'].value_counts()

products[(products.Moeda == 'Dólar')]

products.sort_values(by='Preço de Compra', ascending = True)

experimental_data.describe()

experimental_data.sort_values('tratamento')

experimental_data.sort_values(by='dose')

experimental_data['tratamento'].value_counts()

experimental_data['droga'].value_counts()

# products
#O documento examinado contém dados sobre produtos importados, incluindo informações como nome, preço e a moeda de compra.
#Ele realiza cálculos para determinar o gasto em moeda local (real) e, em seguida, multiplica esse valor pela "Margem" para estabelecer o preço de venda, levando em consideração o lucro incorporado na margem.
#Parece ser uma tabela relacionada a uma loja que se dedica à importação e venda de itens, pois exibe valores originais em sua moeda nativa e a margem de lucro ao converter para a moeda local (real) para a venda.

# experimental_data
#Os registros experimentais fornecem informações sobre os procedimentos realizados em um contexto médico, possivelmente relacionados a uma condição específica.
#A tabela apresenta dados sobre a dose administrada (seja primeira, segunda, etc.) e um identificador que provavelmente referencia o nome da droga em outra tabela.
#Esse arquivo parece trazer informações sobre experimentos relacionados a uma possível doença, incluindo identificação, tratamento, tempo de tratamento, doses necessárias e identificação da droga utilizada.
