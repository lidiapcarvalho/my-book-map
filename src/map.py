import requests
import pycountry
import plotly.express as px
import unicodedata

# Código dos paíeses
country_aliases = {
    # A-C
    'Afeganistão': 'Afghanistan',
    'África do Sul': 'South Africa',
    'Argélia': 'Algeria',
    'Antígua e Barbuda': 'Antigua and Barbuda',
    'Azerbaijão': 'Azerbaijan',
    'Barém': 'Bahrain',
    'Bélgica': 'Belgium',
    'Bielorrússia': 'Belarus',
    'Bolívia': 'Bolivia, Plurinational State of',
    'Butão': 'Bhutan',
    'Camarões': 'Cameroon',
    'Cazaquistão': 'Kazakhstan',
    'Chéquia': 'Czechia',
    'Croácia': 'Croatia',
    'Coreia do Norte': 'Korea, Democratic People\'s Republic of',
    'Coréia do Norte': 'Korea, Democratic People\'s Republic of',
    'North Korea': "Korea, Democratic People's Republic of",
    'Coreia do Sul': 'Korea, Republic of',
    'Coréia do Sul': 'Korea, Republic of',
    'South Korea': 'Korea, Republic of',
    # D-F
    'Emirados Árabes Unidos': 'United Arab Emirates',
    'Eslováquia': 'Slovakia',
    'Eslovénia': 'Slovenia',
    'Etiópia': 'Ethiopia',
    'Finlândia': 'Finland',
    # G-L
    'Grécia': 'Greece',
    'Guiné': 'Guinea',
    'Guiné-Bissau': 'Guinea-Bissau',
    'Irão': 'Iran, Islamic Republic of',
    'Islândia': 'Iceland',
    'Itália': 'Italy',
    'Jordânia': 'Jordan',
    'Letónia': 'Latvia',
    'Líbano': 'Lebanon',
    'Líbia': 'Libya',
    'Lituânia': 'Lithuania',
    # M-P
    'Macedónia do Norte': 'North Macedonia',
    'Maláui': 'Malawi',
    'Malásia': 'Malaysia',
    'Maurícia': 'Mauritius',
    'Micronésia': 'Micronesia, Federated States of',
    'Moldávia': 'Moldova, Republic of',
    'Países Baixos': 'Netherlands',
    'Paquistão': 'Pakistan',
    'Papua-Nova Guiné': 'Papua New Guinea',
    'Polónia': 'Poland',
    # Q-S
    'Quénia': 'Kenya',
    'Quirguistão': 'Kyrgyzstan',
    'Quiribáti': 'Kiribati',
    'República Centro-Africana': 'Central African Republic',
    'República Dominicana': 'Dominican Republic',
    'Roménia': 'Romania',
    'Rússia': 'Russian Federation',
    'Russia': 'Russian Federation',
    'São Cristóvão e Neves': 'Saint Kitts and Nevis',
    'São Marinho': 'San Marino',
    'São Tomé e Príncipe': 'Sao Tome and Principe',
    'São Vicente e Granadinas': 'Saint Vincent and the Grenadines',
    'Sérvia': 'Serbia',
    'Síria': 'Syrian Arab Republic',
    'Sudão': 'Sudan',
    'Sudão do Sul': 'South Sudan',
    'Suécia': 'Sweden',
    'Suíça': 'Switzerland',
    # T-Z
    'Tailândia': 'Thailand',
    'Tajiquistão': 'Tajikistan',
    'Tanzânia': 'Tanzania, United Republic of',
    'Turquemenistão': 'Turkmenistan',
    'Ucrânia': 'Ukraine',
    'Uzbequistão': 'Uzbekistan',
    'Zimbábue': 'Zimbabwe',
}


def get_country_code(country):
    country_name = country_aliases.get(country, country)
    country_name = remove_accents(country_name)

    country_data = pycountry.countries.get(name=country_name)

    if country_data:
        return country_data.alpha_3

    return None


def remove_accents(text):
    return ''.join(
        char
        for char in unicodedata.normalize('NFD', text)
        if unicodedata.category(char) != 'Mn'
    )


def create_map(books):

    geojson_url = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson"
    geojson = requests.get(geojson_url).json()

    # ==================================================
    # 6. MAPA
    # ==================================================

    # year_colors = {
    # 2022: 'pink',
    # 2025: 'red',
    # 2026: 'blue',
    # 2027: 'green'
    # }

    year_country_counts = (
        books.groupby(['year_read', 'country'])
        .size()
        .reset_index(name='books')
    )

    years = sorted(books['year_read'].unique())

    colors = [
        'pink',
        'red',
        'blue',
        'green',
        'orange',
        'purple',
        'brown',
        'cyan'
    ]

    year_colors = {
        year: colors[i % len(colors)]
        for i, year in enumerate(years)
    }

    books_per_year = books['year_read'].value_counts().sort_index()

    map_data_by_year = {}

    for year in years:
        map_data_by_year[year] = year_country_counts[
            year_country_counts['year_read'] == year
        ]

    # Criar os mapas individuais de cada ano
    year_figures = {}

    for year in years:
        year_data = map_data_by_year[year]

        year_figures[year] = px.choropleth_map(
            year_data,
            geojson=geojson,
            locations=year_data['country'].map(get_country_code),
            featureidkey='properties.ADM0_A3',
            color_discrete_sequence=[year_colors[year]],
            hover_name='country',
            hover_data={
                'books': True
            },
            labels={'books': 'Número de livros'},
            map_style='basic',
            zoom=1,
            center={"lat": 25, "lon": 10},
            title=f"My Book's World Travel 🌍 - {year}: {books_per_year[year]} books"
        )

# ___ Mapa "All"_____________________________________________________

    first_year = years[0]

    fig_map = px.choropleth_map(
        map_data_by_year[first_year],
        geojson=geojson,
        locations=map_data_by_year[first_year]['country'].map(
            get_country_code),
        featureidkey='preporties.ADM0_A3',
        color_discrete_sequence=[year_colors[first_year]],
        hover_name='country',
        map_style='basic',
        zoom=1,
        center={"lat": 25, "lon": 10},
        title="My Book's World Travel 🌍"
    )

    # Remove o primeiro trace, proque vamos adicionar todos os anos
    fig_map.data = ()

    # Adicionar os mapas de todos os anos
    for year in years:
        fig_map.add_traces(year_figures[year].data)

# ___ Dropdown______________________________________________________

    buttons = []

    # Quantos traces pertencem a cada ano?
    year_trace_ranges = {}
    current_position = 0

    for year in years:
        number_of_traces = len(year_figures[year].data)

        year_trace_ranges[year] = range(
            current_position,
            current_position + number_of_traces
        )

        current_position += number_of_traces

    # ALL

    all_visible = [True] * len(fig_map.data)

    buttons.append({
        'label': 'All',
        'method': 'update',
        'args': [
            {
                'visible': all_visible
            },
            {
                'title.text': f"My Book's World Travel 🌍 — All: {len(books)} books"
            }
        ]
    })

    # CADA ANO

    for year in years:

        visible = [False] * len(fig_map.data)

        for trace_index in year_trace_ranges[year]:
            visible[trace_index] = True

        buttons.append({
            'label': str(year),
            'method': 'update',
            'args': [
                {
                    'visible': visible
                },
                {
                    'title.text': f"My Book's World Travel 🌍 — {year}: {books_per_year[year]} books"
                }
            ]
        })

    # Mostra inicialmente todos os anos
    for trace in fig_map.data:
        trace.visible = True

    fig_map.update_layout(
        title="My Book's World Travel 🌍",
        title_x=0.5,
        updatemenus=[
            {
                'buttons': buttons,
                'direction': 'down',
                'showactive': True
            }
        ]
    )

    fig_map.write_html('mapa.html', auto_open=True)
