import pandas as pd
# as  pd - abreviatura convencional para pandas

from map import create_map
from books import add_book

# ==================================================
# 1. CARREGAR OS DADOS
# ==================================================

books = pd.read_csv('data/books.csv')
# lê o ficheiro CSV e armazena os dados no DataFrame do pandas

answer = input("Queres adicionar um novo livro? (s/n): ")

if answer.lower() == 's':
    add_book()
    books = pd.read_csv('data/books.csv')

create_map(books)
