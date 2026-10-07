import pandas as pd

from map import create_map
from books import add_book

# ==================================================
# 1. CARREGAR OS DADOS
# ==================================================

books = pd.read_csv('data/books.csv')

while True:
    answer = input("Queres adicionar um novo livro? (s/n): ")

    if answer.lower() != 's':
        break

    add_book()

books = pd.read_csv('data/books.csv')

create_map(books)
