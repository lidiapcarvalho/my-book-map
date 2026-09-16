import requests
import plotly.express as px


def create_map(books):

    geojson_url = "https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson"
    geojson = requests.get(geojson_url).json()

    # ==================================================
    # 6. MAPA
    # ==================================================

    # Código dos paíeses
    country_codes = {
        'Argentina': 'ARG',
        'Brazil': 'BRA',
        'India': 'IND',
        'Japan': 'JPN',
        'Poland': 'POL',
        'Portugal': 'PRT',
        'South Korea': 'KOR',
        'United States': 'USA',
        'United Kingdom': 'GBR',
        'France': 'FRA',
        'Ireland': 'IRL'
    }

    year_colors = {
        2022: 'pink',
        2025: 'red',
        2026: 'blue',
        2027: 'green'
    }

    year_country_counts = (
        books.groupby(['year_read', 'country'])
        .size()
        .reset_index(name='books')
    )

    years = sorted(books['year_read'].unique())

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
            locations=year_data['country'].map(country_codes),
            featureidkey='properties.ISO3166-1-Alpha-3',
            color_discrete_sequence=[year_colors[year]],
            hover_name='country',
            hover_data={
                'books': True
            },
            labels={'books': 'Número de livros'},
            map_style='basic',
            zoom=1,
            center={"lat": 25, "lon": 10},
            title="My Book's World Travel 🌍"
        )

# ___ Mapa "All"_____________________________________________________

    first_year = years[0]

    fig_map = px.choropleth_map(
        map_data_by_year[first_year],
        geojson=geojson,
        locations=map_data_by_year[first_year]['country'].map(country_codes),
        featureidkey='preporties.ISO3166-1-Alpha-3',
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
