# Work Diary

## 02/08/2026

### O que fiz? 🤔

- Criei o projeto `my-book-map`
- Criei o repositório no GitHub
- Instalei as bibliotecas `pandas` e `plotly`
- Criei a estrutura inicial do projeto
- Criei [`book.csv`](book.csv)
- Adicionei os 7 e 12 livros lidos em 2022 e 2025, respetivamente
- Um `DataFrame` do pandas organiza os dados em linhas e colunas.
- `len(books)` mostra o número de linhas
- `books.shape` mostra a dimensão do DataFrame no formato `(linhas, colunas)`.
- `books.columns` mostra os nomes das colunas
- `books.head()` mostra as primeiras 5 linhas por defeito
- `books.tail()` mostra as últimas 5 linhas por defeito
- `books["title"]` permite selecionar uma coluna
- `books[["title", "author"]]` permite selecionar várias colunas através de uma lista de nomes
- Criação de um ficheiro dedicado a notas de conceitos apreendidos, explicados de forma detalhada ([`notes.md`](notes.md))

### Decisões 🧐

- O país corresponde ao país associado ao autor, seguindo a organização do que faço no Maratona App ([Link do meu perfil no Maratona App](https://maratona.social/@lidialecle))
- Os países serão guardados em inglês
- O ano de leitura será separado do ano de publicação
- A coluna `century` será utilizada para livros publicados antes do ano de 2000
- Não será utilizada a quantidade de páginas devido à possível inconsistência das edições

## 03/09/2026

### O que fiz? 🤔

- Continuei a exploração do ficheiro `books.csv` utilizadno pandas
- Criei uma contagem dos livros por país através de `value_counts()`
- Guardei o resultado numa variável: `country_counts = books['country'].value_counts()`
- Comecei a utilizar o Ploty Express para criar visualizações dos dados
- Criei um gráfico de barras com o número de livros lidos por país
- Aprendi a utilizar um objeto `fig` para guardar o gráfico
- Personalizei o gráfico com `fig.update_layout()`, adicionando:
    - título;
    - nome do eixo X;
    - nome do eixo Y.
- Adicionei os valotes numéricos às barras através de `text=country_counts.values`
- Aprendi a controlar a posição desses valores com `textposition`, utilizando `'inside'` e `'outside'`

### O que aprendi 🗒️🤓

Plotly
- `px.bar()` permite criar gráficos de barras
- `fig` é a variável que guarda o gráfico criado
- `fig.show()` apresenta o gráfico no navegador
- `fig.update_layout()` permite alterar elementos do layout do gráfico
- `fig.update_traces()` permite alterar características das próprias barras
- `text` permite apresentar valores associados às barras
- `textposition` permite definir onde esses valores aparecem

Pandas
- `value_counts()` permite contar quantas vezes cada valor aparece numa coluna
- O resultado de `value_counts()` é ordenado, por defeito, do valor mais frequente para o menos frequente
- `ascending=False` indica uma ordenação descendente, ou seja, do maior para o menor



