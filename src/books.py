import pandas as pd


def add_book():
    title = input("Título: ")
    author = input("Autor: ")
    year_read = input("Ano de leitura: ")
    country = input("País: ")
    publication_year = input("Ano de publicação: ")
    century = input("Século: ")
    reading_language = input("Idioma de leitura: ")
    genre = input("Género: ")
    rating = input("Rating: ")

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
