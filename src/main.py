import pandas as pd
# as  pd - abreviatura convencional para pandas
import plotly.express as px

# Teste
import requests

geojson_url = "https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson"

geojson = requests.get(geojson_url).json()

print(geojson["features"][0]["properties"])


# ==================================================
# 1. CARREGAR OS DADOS
# ==================================================

books = pd.read_csv('data/books.csv')
# lê o ficheiro CSV e armazena os dados no DataFrame do pandas

print(books)

# ==================================================
# 2. EXPLORAÇÃO DOS DADOS
# ==================================================

# Quantos livros temos?
print(len(books))  # Neste caso estamos a contar o número de linhas

# Quantas linhas e colunas temos?
print(books.shape)  # (linhas, colunas)

# Quais são os nomes das colunas?
print(books.columns)

# Olhar para os dados em si, mas sem imprimir tudo
print(books.head())  # Mostra as primeiras 5 linhas

print(books.tail())  # Mostra as últimas 5 linhas

# ==================================================
# 3. FILTROS
# ==================================================

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

# ==================================================
# 4. ESTATÍSTICAS
# ==================================================

# Quantos livros temos de cada país?
country_counts = books['country'].value_counts()
print(country_counts)

# Ordenar os países pelo número de livros
country_counts_sorted = country_counts.sort_values(ascending=False)

print(sorted(books['country'].unique()))

# ==================================================
# 5. GRÁFICO — LIVROS POR PAÍS
# ==================================================

# Plotly
fig = px.bar(
    country_counts_sorted,
    x=country_counts_sorted.index,  # x - países
    y=country_counts_sorted.values,  # y - número de livros
    text=country_counts_sorted.values  # texto a mostrar em cada barra
)

fig.update_layout(
    xaxis_title="País",
    yaxis_title="Número de livros",
)

fig.update_traces(
    textposition='outside'  # Posição do texto fora da barra
)

# Salva o gráfico como um ficheiro HTML
fig.write_html('grafico.html', auto_open=True)

# ==================================================
# 6. MAPA
# ==================================================

# Código dos paíeses
country_codes = {
    'Argentina': 'ARG',
    'Brazil': 'BRA',
    'India': 'IND',
    'Japan': 'JPN',
    'Poland': 'POL',
    'Portugal': 'PRT',
    'South Korea': 'KOR',
    'United States': 'USA',
}

# Reseta o índice para que possamos ter uma coluna com os países
map_data = country_counts.reset_index()
map_data.columns = ['country', 'books']
map_data['iso_alpha'] = map_data['country'].map(
    country_codes)  # Mapeia os países para os seus códigos ISO
print(map_data)

# Mapa
fig_map = px.choropleth_map(
    map_data,
    geojson=geojson,
    locations='iso_alpha',
    featureidkey='properties.ISO3166-1-Alpha-3',
    color='books',
    hover_name='country',
    hover_data={'books': True, 'iso_alpha': False},
    color_continuous_scale='Blues',
    map_style='carto-positron',
    zoom=1,
    center={"lat": 0, "lon": 0},
    title='Livros lidos por país'
)

fig_map.update_geos(
    projection_type='natural earth',
)

fig_map.update_layout(
    title='Livros lidos por país',
    title_x=0.5,
)

fig_map.write_html('mapa.html', auto_open=True)
