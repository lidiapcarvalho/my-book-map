# Notes

> As notas estão apresentadas por ficheiro

## [`src/main.py`](src/main.py)

DataFrame - estrutura de dados do pandas que organiza informação em forma de tabela, composta por linhas e colunas. No projeot, o DataFrame `books` representa a tabela com os livros lidos, onde cada linhas corresponde a um livro e cada coluna a uma caracterísitca do livro.

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

`books['year_read'] == 2022` - cria a condição True or False

`books[ ... ]` - usa essa condição para selecionar as linhas correspondentes

Juntando:
`books[books['year_read'] == 2022]` - filtra o DataFrame

**Operadores**
==    igual a
!=    diferente de
>     maior que
<     menor que
>=    maior ou igual a
<=    menor ou igual a

`.value_counts()` - conta quantas vezes cada valor aparece, e por defeito, ordena os resultados do maior para o menor número de ocorrências

**Usando o Plotly**
```python
fig = px.bar(
    country_counts,
    x=country_counts.index,
    y=country_counts.values,
    text=country_counts.values
)

fig.show()
```
`fig` - variável onde guardamos o objeto gráfico criado pelo Plotly
`px.bar(...)` - cria o gráfico
`fig.show()` - mostra o gráfico





