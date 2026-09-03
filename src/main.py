import pandas as pd
# as  pd - abreviatura convencional para pandas
import plotly.express as px

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

# Quais os livros que li em 2022?
# Condição para filtrar os livros lidos em 2022
# Aqui para cada linha, ele vai responder True or False
print(books['year_read'] == 2022)

# Aqui ele vai mostrar apenas os livros lidos em 2022
print(books[books['year_read'] == 2022])

print(books['year_read'] == 2025)
print(books[books['year_read'] == 2025])

# Filtrar pelo rating
print(books[books['rating'] == 5])  # Mostra os livros com rating igual a 5
# Mostra os livros com rating maior ou igual a 4
print(books[books['rating'] >= 4.5])

# Mais de uma condição
print(books[(books["year_read"] == 2025) & (books["rating"] == 5)])

print(books[(books["year_read"] == 2022) | (books["year_read"] == 2025)])

# Quantos livros temos de cada país?
country_counts = books['country'].value_counts()
print(country_counts)

# Plotly
fig = px.bar(
    country_counts,
    x=country_counts.index,  # x - países
    y=country_counts.values,  # y - número de livros
    text=country_counts.values  # texto a mostrar em cada barra
)

fig.update_layout(
    xaxis_title="País",
    yaxis_title="Número de livros",
)

fig.update_traces(
    textposition='outside'  # Posição do texto fora da barra
)

fig.show()
