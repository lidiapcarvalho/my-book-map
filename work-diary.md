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

## 04/09/2026

### O que fiz? 🤔

- Organização do `main.py`, separando a exploração dos dados, filtros, estatísticas, gráfico e mapa
- Resolvi o problema do `fig.show()`, que estava a abrir uma página local com `ERR_CONNECTION_REFUSED`
- Passei a guardar os gráficos como HTML com `fig.write_html(..., auto_open=True)`
- O gráfico de livros lidos por país ficou funcional
- Preparei os dados dos países com códigos ISO-3
- Experimentei um **tile choropleth map** com `px.choropleth_map`
- O mapa aparecia, mas os países não estavam a ser pintados
- Investiguei o GeoJSON e descobri que a propriedade dos códigos ISO-3 se chama `ISO3166-1-Alpha-3`, e não `ISO_A3`
- Corrigi o `featureidkey` para `properties.ISO3166-1-Alpha-3`
- O mapa passou finalmente a apresentar os países com a escala de cores correspondente ao número de linhas

### O que aprendi 🗒️🤓

- Hoje fiquei também com uma melhor compreensão de como os dados do meu CSV são associados às geometrias do mapa através dos códigos ISO

## 07/09/2026

### O que fiz? 🤔

- Restauro dos ficheiros `map.py` e `stats.py` que desapareceram após alterar a designação dos commit's para o padrão que queria.

## 08/09/2026

### O que fiz? 🤔

- Adicionei ao mapa informações adicionais no `hover`, incluindo:
    - número de livros;
    - último ano de leitura;
    - percentagem de livros lidos por país.
- Melhorei a identificação da legenda, passando a indicar "Número de livros"
- Comecei a implementar um dropdown para permitir visualizar os livros por ano
- Criei uma tabela com o número de livros por país e por ano utilizado `groupby()`
- Separei os dados correspondentes a 2022 e criei um mapa específico para esse ano
- Testei o mapa de 2022 e confirmei que apresenta corretamente os três países onde li livros nesse ano: índia, Polónia e Estados Unidos
- O próximo passo será terminar o dropdown, permitindo alternar entre "Todos", 2022 e 2025.

## 10/09/2026

### O que fiz? 🤔

- Continuei a implementação das cores associadas aos diferentes anos de leitura no mapa.
- Definir cores específicas para cada ano:
    - 2022 - rosa
    - 2025 - vermelho
    - 2026 - azul
    - 2027 - verde
- Alterei o mapa de 2022 e de 2025 para utilizarem as suas cores.
- Testei as alterações e confirmei que as cores são apresentadas corretamente nos mapas individuais.
- Adicionei os mapas de 2022 e 2025 ao mapa principal para permitir apresentar as duas cores em simultâneo na opção "All".
- Escondi o mapa anterior que utilizava uma escala de cores contínua.
- Testei o mapa e confirmei que, inicialmente, a opão "All" aparesenta os livros de 2022 a rosa e os de 2025 a vermelho.
- Ficou pendente corrigir o dropdown, uma vez que ao selecionar novamente 2022 ou 2025 ainda é utilizada a configuração anterior com a escala de cores.

## 11/09/2026

### O que fiz? 🤔

- Corrigi o dropdown do mapa para que as opções "All", 2022 e 2025 utilizem corretamente as cores definidas para cada ano.
- Ajustei a visibilidade dos diferentes traces, garantindo que o mapa com a escala de cores anterior não volta a aparecer ao alterar a opção do dropdown.
- Confirmei que a opção "All" apresenta simultaneamente:
    - livros de 2022 a rosa;
    - livros de 2025 a vermelho.
- Identifiquei um aviso de bloqueio dos servidores de tiles do OpenStreetMap ao utilizar open-street-map como mapa de fundo.
- Explorei a utilização de estilos de mapa baseados em MapLibre.
- Testei diferentes estilos predefinidos, incluindo carto-positron, carto-voyager, basic e dark.
- Comparei visualmente os estilos tendo em conta a informação apresentada no mapa, os contornos dos países e o destaque das cores dos anos de leitura.
- Decidi utilizar temporariamente o estilo basic.

### Decisões 🧐

- O estilo basic será utilizado na versão atual do projeto por apresentar um bom equilíbrio entre informação e simplicidade.
- No futuro, poderá ser explorada a possibilidade de criar uma versão com um estilo dark para o mapa.

## 12/09/2026

### O que fiz? 🤔

- Continuei o desenvolvimento do mapa interativo do projeto `my-book-map`
- Corrigi a lógica do dropdown para alternar corretamente entre All, 2022 e 2025
- Adicionei informação ao `hover`, apresentando o número de livros de cada país, com a identificação "Número de livros"
- Criei uma imagem do mapa para apresentar no `README.md`
- Fiz uma revisão na estrutura dos ficheiros
- Removi o ficheiro antigo `mapa_2022.html`
- Confirmei que o `.gitigmore` já inclui `__pycache__/` e os ficheiros `.pyc`
- Limpei o código que já não era utilizado em `map.py` e `main.py`
- Confirmei que o projeto continuava a executar sem erros

### O que aprendi 🗒️🤓

- O dropdown do Plotly pode controlar a visibilidade dos diferentes traces através de `update`
- É possível criar diferentes figuras e combinar os seus traces numa única figura
- `color_discrete_sequence` permite definir uma cor específica para os dados apresentados num mapa
- `hover_data` permite controlar a informação apresentada ao passar o rato sobre um país
- O ficheiro `.gitignore` permite impedir que ficheiros gerados automaticamente pelo Python sejam adicionados ao repositório
- O `README.md` pode incluir imagens armazenadas dentro do próprio repositório através de um caminho relativo

## 14/09/2026

### O que fiz? 🤔

- Continuei a revisão e organização do projeto
- Simplifiquei o `main.py`, removendo imports e código que já não eram utilizados pelo mapa
- Revisei o `map.py` e confirmei que a lógica atual do mapa, das cores por ano, do dropdown e do `hover` estava correta
- Corrigi as funções `statistics()` e `charts()` no `stats.py`, fazendo com que cada função trabalhe com os dados de que necessita
- Atualizei o `requirements.txt`, adicionando `requests`, que é utilizado pelo `map.py`
- Executei novamente o projeto para confirmar que continuava a funcionar sem erros
- Revisei o `README.md` e melhorei a descrição do mapa, incluindo a informação sobre o número de livros por país
- Mantive o `notes.md` para uma revisão posterior

### O que aprendi 🗒️🤓

- Uma função deve receber explicitamente os dados de que necessita, em vez de depender de variáveis criadas noutra função
- O `requirements.txt` deve incluir as bibliotecas que o projeto utiliza diretamente
- É importante rever o código depois de alterações maiores para remover código que deixou de ser necessário
- A documentação deve acompanhar a versão atual do projeto e explicar de forma simples o que o mapa permite visualizar

