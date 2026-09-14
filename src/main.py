import pandas as pd
# as  pd - abreviatura convencional para pandas

from map import create_map

# ==================================================
# 1. CARREGAR OS DADOS
# ==================================================

books = pd.read_csv('data/books.csv')
# lê o ficheiro CSV e armazena os dados no DataFrame do pandas

create_map(books)
