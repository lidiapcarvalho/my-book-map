import pandas as pd


def add_book():
    title = input("Título: ")
    author = input("Autor: ")

    # Ano de leitura
    while True:
        year_read = input("Ano de leitura: ")

        if year_read.isdigit():
            year_read = int(year_read)
            break

        print("Por favor, introduz um ano válido.")

    country = input("País: ")

    # Ano de publicação
    while True:
        publication_year = input("Ano de publicação: ")

        if publication_year == "":
            break

        if publication_year.isdigit():
            publication_year = int(publication_year)
            break

        print("Por favor, introduz um ano válido.")

    # Século
    while True:
        century = input("Século: ")

        if century == "":
            break

        if century.isdigit():
            century = int(century)
            break

        print("Por favor, introduz um século válido.")

    reading_language = input("Idioma de leitura: ")
    genre = input("Género: ")

    # Rating
    while True:
        rating = input("Rating: ")

        try:
            rating = float(rating)

            if 0 <= rating <= 5:
                break

            print("O rating deve estar entre 0 e 5.")

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
