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

## 16/09/2026

### O que fiz? 🤔

- Atualizei o `notes.md`
- Organizei os livros lidos no primeiro semestre de 2026
- Adicionei os novos livros ao `books.csv`
- Mantive um ficheiro `.txt` provisório com os dados do primeiro semestre, para futuramente organizar o segundo semestre de 2026
- Atualizei o `map.py` com os códigos ISO dos novos países presentes nos dados: Reino Unido, França e Irlanda
- Ao verificar o mapa, percebi que a França não estava a ser apresentada
- Investiguei a origem do problema através do GeoJSON utilizado pelo mapa e confirmei que a França aparece nesse ficheiro com o código `-99`, apesar de o código ISO oficial ser `FRA`
- Deixei a investigação do problema da França para continuar posteriormente

### O que aprendi 🗒️🤓

- Os códigos ISO-3166-1 são utilizados para associar os países aos dados geográficos do mapa
- Um país pode estar corretamente identificado nos nossos dados e, ainda assim, não ser apresentado se a fonte geográfica utilizada tiver uma identificação diferente ou incompleta
- O `.size()` do pandas permite contar o número de elementos de cada grupo criado com `groupby()`
- Nem todos os problemas de um mapa interativo estão necessariamente no código Python; também podem estar relacionados com os dados geográficos utilizados

## 17/09/2026

### O que fiz? 🤔

- Investiguei diferentes identificadores geográficos, incluindo `ADM0_A3` e `ISO_A3_EH`
- Testei uma nova fonte de dados geográficos do Natural Earth
- Confirmei que a França é identificada como `FRA` através de `ADM0_A3`
- Alterei o mapa para utilizar o GeoJSON do Natural Earth e `properties.ADM0_A3`
- Executei novamente o projeto e confirmei que a França passou a aparecer corretamente no mapa
- Fiz um novo commit e `git push` com a correção

### O que aprendi 🗒️🤓

- Nem todos os GeoJSON utilizam os códigos ISO da mesma forma
- É importante verificar a estrutura e as propriedades da fonte de dados geográficos quando um país não aparece no mapa
- O campo `ADM0_A3` do Natural Earth permite uma correspondência correta com os códigos dos países utilizados no projeto

## 19/09/2026

### O que fiz? 🤔

- Atualizei o mapa para apresentar o número total de livros lidos por ano
- Criei uma contagem dos livros por ano através do `value_counts()` do pandas
- Integrei essa informação no título do mapa
- Atualizei os botões do dropdown para que, ao selecionar `All` ou um determinado ano, o título mostrasse também o número de livros correspondente
- Corrigi um erro relacionado com o acesso aos dados, utilizando `books_per_year[year]` em vez de tentar aceder ao DataFrame `books` através do ano
- Ajustei a atualização do título através de `title.text`
- Testei o mapa e confirmei que o título e o número de livros são atualizados corretamente ao utilizar o dropdown

### O que aprendi 🗒️🤓

- `value_counts()` permite contar rapidamente quantos registos existem em cada categoria
- Um botão do Plotly pode atualizar simultaneamente a visibilidade dos elementos e propriedades do layout
- Para atualizar corretamente o texto do título através de um dropdown, pode ser necessário utilizar `title.text`
- É importante distinguir o DataFrame original (`books`) de uma série criada especificamente para contar livros por ano (`books_per_year`)

## 21/09/2026

### O que fiz? 🤔

- Instalei a biblioteca `pycountry` para deixar de manter manualmente os códigos ISO dos países no projeto
- Adicionei `pycountry` ao `requirements.txt`
- Testei a obtenção automática dos códigos ISO para os países já presentes no `books.csv`
- Identifiquei que `South Korea` não era reconhecido diretamente pela biblioteca
- Criei um sistema de aliases para tratar diferenças entre os nomes utilizados no projeto e os nomes reconhecidos pelo `pycountry`
- Criei a função `get_country_code()` para converter automaticamente os nomes dos países nos respetivos códigos ISO de três letras
- Substituí no `map.py` o dicionário manual `country_codes` pela conversão automática através do `pycountry`
- Testei a solução com os países existentes nos dados
- Testei também `Germany`, um país que ainda não está presente no CSV, confirmando que o código `DEU` é obtido automaticamente
- Executei o projeto e confirmei que o mapa continua a funcionar corretamente

### O que aprendi 🗒️🤓

- Bibliotecas externas podem evitar a manutenção manual de informação que já existe numa base de dados standard
- O `pycountry` permite obter automaticamente códigos ISO 3166-1
- Aliases são úteis quando os nomes utilizados nos nossos dados não coincidem com os nomes utilizados pela biblioteca
- Separar a conversão dos nomes dos países numa função torna o código do mapa mais simples e fácil de manter.

## 22/09/2026

### O que fiz? 🤔

- Criado o ficheiro `src/books.py` para permitir adicionar novos livros ao projeto sem editar diretamente o `books.csv`
- Criada a função `add_book()` para recolher os dados de um novo livro através de `input()`
- Adicionados os 9 campos correspondentes às colunas do `books.csv`: título, autor, ano de leitura, país, ano de publicação, século, idioma de leitura, género e rating
- Utilizado `pandas` para criar um `DataFrame` com os dados introduzidos
- Implementada a gravação do novo livro no `data/books.csv` através de `to_csv()`, utilizando `mode='a'` para acrescentar a nova linha sem substituir os dados existentes
- Integrada a função `add_book()` no `src/main.py`
- Adicionada uma pergunta para escolher se pretende adicionar um novo livro ao executar o programa
- Após a adição de um livro, o `books.csv` é novamente carregado antes de criar o mapa, garantindo que os novos dados são utilizados
- Testada a funcionalidade com a opção de não adicionar um livro e com a adição de um livro de teste
- Testado um ano novo (`2027`) para confirmar que o mapa deteta automaticamente o novo ano e apresenta a respetiva cor
- Removidos os dados utilizados apenas para teste

## 23/09/2026

### O que fiz? 🤔

- Tornada dinâmica a atribuição de cores aos anos no mapa, deixando de ser necessário adicionar manualmente cada novo ano ao dicionário `year_colors`
- As cores são agora atribuídas automaticamente aos anos existentes no `books.csv`, permitindo que novos anos sejam reconhecidos sem alterações adicionais no código
- Testada a nova lógica com o ano de 2028 através da funcionalidade de adição de livros
- Confirmado que o ano de 2028 foi reconhecido pelo mapa e recebeu automaticamente uma nova cor
- Removidos os dados utilizados apenas para o teste
- Adicionada validação ao campo `year_read`, garantindo que o valor introduzido é numérico
- Adicionada validação ao campo `rating`, convertendo o valor introduzido para `float` e rejeitando entradas que não sejam numéricas.

## 24/09/2026

### O que fiz? 🤔

- Melhorada a validação do campo `rating` no `books.py`
- Definido que o `rating` deve ser um valor numérico entre 0 e 5
- Mantida a conversão do `rating` para `float`
- Testadas entradas inválidas, incluindo valores não numéricos e valores fora do intervalo permitido
- Confirmado que valores válidos, como `4.5`, são aceites corretamente
- Alterado o campo `year_read` para ser convertido para `int` no momento da introdução
- Testada a introdução do ano de leitura após a alteração

## 25/09/2026

### O que fiz? 🤔

- Adicionada validação ao campo `publication_year`
- Definido que o ano de publicação pode ficar vazio, mas, quando preenchido, deve ser um número inteiro válido
- Adicionada validação ao campo `century`
- Definido que o século pode ficar vavzio, mas, quando preenchido, deve ser um número inteiro válido
- Corrigida a validação do campo `year_read`, garantindo que a conversão para `int` acontece depois da verificação do valor introduzido
- Testada a introdução de valores válidos e campos vazios nos campos opcionais
- Confirmado o funcionamento da recolha dos dados a+ós as alterações

## /09/2026

### O que fiz? 🤔
