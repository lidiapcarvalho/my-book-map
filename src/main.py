import pandas as pd
# as  pd - abreviatura convencional para pandas
import plotly.express as px

from stats import show_statistics
from map import create_map

# ==================================================
# 1. CARREGAR OS DADOS
# ==================================================

books = pd.read_csv('data/books.csv')
# lê o ficheiro CSV e armazena os dados no DataFrame do pandas

country_counts, latest_year = show_statistics(books)

create_map(books)
