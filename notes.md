# Notes

> As notas estão apresentadas por ficheiro

## [`src/books.py`](src/books.py)

`.isdigit()` - é um método de strings que verifica se todos os caracteres de um string são dígitos, verificando:
- "2026" -> True
- "abc" -> False
- "20a6" -> False
- "" -> False

```python
new_book = pd.DataFrame([{
    'title': title,
    'author': author,
    'year_read': year_read,
    ...
    'rating': rating
}])
```

- Cria um DataFrame com uma linha, correspondente ao livro que acabámos de introduzir

```python
new_book.to_csv(
    'data/books.csv',
    mode='a',
    header=False,
    index=False
)
```
- `mode='a'` - append - acrescentar dadosao final do ficheiro, sem este poderíamos acabar por substituir o conteúdo já existente no CSV

- `header=False` - header corresponde ao nome das colunas. Como não queremos escrevê-los novamente cada vez que adicionamos um livro, usamos `header=False`

- `index=False` - o Pandas normalmente adiciona uma coluna de índice:
0
1
2
3
Porém não queremos que esse índice faça parte dos nossos dados, então configuramos como False esse index, para evitar essa coluna seja gravada no CSV

- Em conjunto, esta parte significa essencialmente: "Pega neste novo livro, acrescenta-o ao final de `books.csv`, sem repetir os nomes das colunas e sem adicionar o índice do Pandas."

## [`src/main.py`](src/main.py)

DataFrame - estrutura de dados do pandas que organiza informação em forma de tabela, composta por linhas e colunas. No projeot, o DataFrame `books` representa a tabela com os livros lidos, onde cada linhas corresponde a um livro e cada coluna a uma caracterísitca do livro.

`as pd` - abreviatura convencional para pandas

`books = pd.read_csv('data/books.csv')` - lê o ficheiro CSV e armazena os dados no DataFrame do pandas

## [`src/map.py`](src/map.py)

`import plotly.express as px` - uma parte da biblioteca Plotly que usamos para criar os gráficos e o mapa

`import unicodedata`

- `unicodedata` - biblioteca que já vem com o Python, não precisamos de a instalar e, por esse motivo não aparece no `requirements.txt`, permitindo-nos trabalhar com as características dos caracteres Unicode - incluindo acentos e outros sinais. No projeto usamos para facilitar a pesquisa do país no `pycountry`.

`.get()` - método de dicionários (`dict`). A ideia é: "Procura esta chave no dicionário. Se existir, devolve o valor. Se não existir, usa este outro valor." Permitindo ter no nosso caso: `country_name = country_aliases.get(country, country)` e dizer:
- se houver um alias -> usa o nome do alias;
- se não houver -> mantém o nome original
É particularmente útil pois não precisasse fazer um `if` para cada país.

```python
return ''.join(
    char
    for char in unicodedata.normalize('NFD', text)
    if unicodedata.category(char) != 'Mn'
)
```

- `unicodedata.normalize('NFD', text)` - o unicode pode representar um carácter acentuado de diferentes formas. Com `NFD`, o Python separa o carácter da sua marca de acento
- `unicodedata.category(char)` - diz-nos a categoria Unicode daquele carácter. Para a marca de acento, a categoria é `Mn`, que significa `Mark, Nonspacing`, uma marca que não ocupa espaço próprio, como muitos acentos
- `''.join(...)` - depois de remover os acentos, temos vários caracteres separados o 
`''.join(...)` junta-os novamente sem colocar nada entre eles

```python
geojson_url = "..."
geojson = requests.get(geojson_url).json()
```
- Obtem um ficheiro GeoJSON através de um URL usando `requests`

```python
country_codes = {
    'Portugal': 'PRT',
    ...
}
```
- Associação de países aos códigos ISO, essencial pois o mapa utiliza os códigos ISO-3 para identificar os países
(Usado no desenvolvimento do projeto)

`books.groupby(['year_read', 'country']).size()`

`.size()` - neste caso serve para contar quantas linhas existem em cada grupo

`.reset_index(name='books')` - aparece normalmente depois de um `groupby()` / `value_counts()`, em suma, transforma o índice numa coluna e dá o nome `books` à coluna das contagens

`.sort_index()` - ordena os dados pelo índice, diferente de `.sort_values()` que ordena pelos valores

```python
year_colors = {
    2022: 'pink',
    2025: 'red',
    ...
}
```
- Atribuição de cores a cada ano

`px.choropleth_map(...)` - criação de mapa coroplético interativo
- Mapa coroplético - mapa temático em que as regiões ou áreas administrativas são pintadas, hachuradas ou coloridas com diferentes tons de cor de acordo com o valor de uma variável estatística

`featureidkey='properties.ADM0_A3',`
- `ADM0_A3` - código de três letras usado pelo Natural Earth para identificar o país

`color_discrete_sequence=[year_colors[year]]`
- `year_colors[year]` vai buscar ao dicionário a cor correspondente ao ano atual

`fig_map.add_traces`
- `trace` simplificando é uma camada de dados/gráfico dentro da figura, é útil pois permite que o mapa tenha vários anos e queremos que cada ano seja tratado como uma camada diferente, que depois pode ser controlada pelo dropdown

`years = sorted(books['year_read'].unique())`
- O código utiliza os anos existentes no CSV, em vez de depender diretamente de uma lista fixa para criar o dropdown

### Dropdown

`buttons = []`
- Controla a visibilidade dos traces através dos botões do Plotly

```python
hover_data={'books': True}
labels={'books': 'Número de livros'}
```
- Mostra informações no hover, como o número de livros se passarmos o rato sobre um país

`fig_map.write_html('mapa.html', auto_open=True)`
- Cria o mapa como HTML

## [`src/stats.py`](src/stats.py)

### Consultar `def show_statistics(books):` e `def statistics(books):`

`groupby` - agrupa os livros por país

`Index()` - estrutura de pandas para representar uma sequência de nomes

**Operadores**
==    igual a
!=    diferente de
>     maior que
<     menor que
>=    maior ou igual a
<=    menor ou igual a

`.value_counts()` - conta quantas vezes cada valor aparece, e por defeito, ordena os resultados do maior para o menor número de ocorrências

### Consultar `def data_exploration(books):`

`books.shape` - (linhas, colunas)

`books.head()` - mostra as primeiras 5 linhas
- Se colocarmos um número dentro dos parênteses, podemos quantas linhas queremos ver

`books.tail()` - mostra as últimas 5 linhas
- Idem

### Consultar `def filter_data(books):`

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

### Consultar `def charts(books):`

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


