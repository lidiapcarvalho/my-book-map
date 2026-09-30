import pandas as pd
from map import get_country_code


def add_book():
    # Title
    while True:
        title = input("Título: ")

        if title.strip():
            break

        print("O título não pode ficar vazio.")

    # Author
    while True:
        author = input("Autor: ")

        if author.strip():
            break

        print("O autor não pode ficar vazio.")

    # Year Read
    while True:
        year_read = input("Ano de leitura: ")

        if year_read.isdigit():
            year_read = int(year_read)
            break

        print("Por favor, introduz um ano válido.")

    # Country
    while True:
        country = input("País: ")

        if get_country_code(country):
            break

        print("País não encontrado. Tenta novamente.")

    # Publication Year
    while True:
        publication_year = input("Ano de publicação: ")

        if publication_year == "":
            break

        if publication_year.isdigit():
            publication_year = int(publication_year)
            break

        print("Por favor, introduz um ano válido.")

    # Century
    while True:
        century = input("Século: ")

        if century == "":
            break

        if century.isdigit():
            century = int(century)
            break

        print("Por favor, introduz um século válido.")

    # Reading Language
    reading_language = input("Idioma de leitura: ")

    # Genre
    genre = input("Género: ")

    # Rating
    while True:
        rating = input("Rating: ")

        try:
            rating = float(rating)

            if 0 <= rating <= 5 and rating * 2 == int(rating * 2):
                break

            print("O rating deve estar entre 0 e 5, em incrementos de 0.5.")

        except ValueError:
            print("Por favor, introduz um rating válido.")

    print(title)
    print(author)
    print(year_read)
    print(country)
    print(publication_year)
    print(century)
    print(reading_language)
    print(genre)
    print(rating)

    new_book = pd.DataFrame([{
        'title': title,
        'author': author,
        'year_read': year_read,
        'country': country,
        'publication_year': publication_year,
        'century': century,
        'reading_language': reading_language,
        'genre': genre,
        'rating': rating
    }])

    new_book.to_csv(
        'data/books.csv',
        mode='a',
        header=False,
        index=False
    )

    print("Livro adicionado ao CSV.")
