# Notes

> As notas estão apresentadas por ficheiro

## [`src/main.py`](src/main.py)

`as pd` - abreviatura convencional para pandas

`Index()` - estrutura de pandas para representar uma sequência de nomes

`books.head()` - mostra as primeiras 5 linhas
- Se colocarmos um número dentro dos parênteses, podemos quantas linhas queremos ver

`books.tail()` - mostra as últimas 5 linhas
- Idem

**Escolher colunas específicas**
- Uma coluna
    `books['title']` - mostra a coluna 'title'

- Mais de uma coluna
    `books[['title', 'author']]`

Repitimos duas vezes os parênteses retos ("[]"), pois o segundo é uma lista de nomes.
Ao escolher apenas uma coluna, não é necessário repetir os parênteses retos, pois estamos apenas a fornecer uma string.
