import pandas as pd
# as  pd - abreviatura convencional para pandas

books = pd.read_csv('data/books.csv')
# lê o ficheiro CSV e armazena os dados no DataFrame do pandas

print(books)

# Quantos livros temos?
print(len(books))  # Neste caso estamos a contar o número de linhas

# Quantas linhas e colunas temos?
print(books.shape)  # (linhas, colunas)

# Quais são os nomes das colunas?
print(books.columns)

# Olhar para os dados em si, mas sem imprimir tudo
print(books.head())  # Mostra as primeiras 5 linhas

print(books.tail())  # Mostra as últimas 5 linhas

# Escolher colunas específicas
# Uma coluna específica
print(books['title'])  # Mostra a coluna 'title'

# Mais de uma coluna específica
print(books[['title', 'author']])  # Mostra as colunas 'title' e 'author'
