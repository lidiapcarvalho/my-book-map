import plotly.express as px


def show_statistics(books):

    # Quantos livros temos de cada país? - estava no ponto 4. ESTATÍSTICAS
    country_counts = books['country'].value_counts()
    # print(country_counts)

    latest_year = books.groupby('country')['year_read'].max().reset_index()
    # groupby - agrupa os livros por país
    # print(latest_year)

    return country_counts, latest_year


def data_exploration(books):
    # ==================================================
    # 2. EXPLORAÇÃO DOS DADOS
    # ==================================================

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

    return


def filter_data(books):
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

    return


def statistics(books):
    # ==================================================
    # 4. ESTATÍSTICAS
    # ==================================================

    # ver def show_statistics(books)

    # Quantos livros temos de cada país?
    country_counts = books['country'].value_counts()

    # Ordenar os países pelo número de livros
    country_counts_sorted = country_counts.sort_values(ascending=False)

    print(country_counts_sorted)
    print(sorted(books['country'].unique()))

    # ver def show_statistics(books)

    return country_counts_sorted


def charts(books):
    # ==================================================
    # 5. GRÁFICO — LIVROS POR PAÍS
    # ==================================================

    country_counts_sorted = statistics(books)

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

    return
