import requests
import plotly.express as px


def create_map(books, country_counts, latest_year):

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
    }

    year_colors = {
        2022: 'pink',
        2025: 'red',
        2026: 'blue',
        2027: 'green'
    }

    # Reseta o índice para que possamos ter uma coluna com os países
    map_data = country_counts.reset_index()
    map_data.columns = ['country', 'books']

    # Junta os dados do último ano lido
    map_data = map_data.merge(latest_year, on='country')

    year_country_counts = (
        books.groupby(['year_read', 'country'])
        .size()
        .reset_index(name='books')
    )

    years = sorted(books['year_read'].unique())

    dropdown_options = ['Todos'] + years

    map_data_by_year = {}

    for year in years:
        map_data_by_year[year] = year_country_counts[
            year_country_counts['year_read'] == year
        ]

    map_2022 = map_data_by_year[2022]
    map_2025 = map_data_by_year[2025]

    fig_2022 = px.choropleth_map(
        map_2022,
        geojson=geojson,
        locations=map_2022['country'].map(country_codes),
        featureidkey='properties.ISO3166-1-Alpha-3',
        color_discrete_sequence=[year_colors[2022]],
        hover_name='country',
        map_style='open-street-map',
        zoom=1,
        center={"lat": 25, "lon": 10},
        title="My Book's World Travel 🌍"
    )

    fig_2025 = px.choropleth_map(
        map_2025,
        geojson=geojson,
        locations=map_2025['country'].map(country_codes),
        featureidkey='properties.ISO3166-1-Alpha-3',
        color_discrete_sequence=[year_colors[2025]],
        hover_name='country',
        map_style='open-street-map',
        zoom=1,
        center={"lat": 25, "lon": 10},
        title="My Book's World Travel 🌍"
    )

    map_data['percentage'] = (map_data['books'] / len(books)) * 100

    map_data['iso_alpha'] = map_data['country'].map(
        country_codes)  # Mapeia os países para os seus códigos ISO

    # Mapa
    fig_map = px.choropleth_map(
        map_data,
        geojson=geojson,
        locations='iso_alpha',
        featureidkey='properties.ISO3166-1-Alpha-3',
        color='books',
        hover_name='country',
        hover_data={
            'books': True,
            'year_read': True,
            'percentage': ':.1f',
            'iso_alpha': False
        },
        color_continuous_scale='Sunset',
        labels={'books': 'Número de livros'},
        map_style='open-street-map',
        zoom=1,
        center={"lat": 25, "lon": 10},
        title="My Book's World Travel 🌍"
    )

    fig_map.update_geos(
        projection_type='natural earth',
    )

    fig_map.update_layout(
        title="My Book's World Travel 🌍",
        title_x=0.5,
    )

    fig_map.data[0].visible = False

    # Adiciona os mapas de 2022 e 2025 à figura principal
    fig_map.add_traces(fig_2022.data)
    fig_map.add_traces(fig_2025.data)

    # Mostra apenas o mapa "Todos" inicialmente
    # for trace in fig_map.data[1:]:
    # trace.visible = False

    fig_map.update_layout(
        updatemenus=[
            {
                'buttons': [
                    {
                        'label': 'All',
                        'method': 'update',
                        'args': [
                            {'visible': [True, False, False]}
                        ]
                    },
                    {
                        'label': '2022',
                        'method': 'update',
                        'args': [
                            {'visible': [False, True, False]}
                        ]
                    },
                    {
                        'label': '2025',
                        'method': 'update',
                        'args': [
                            {'visible': [False, False, True]}
                        ]
                    }
                ],
                'direction': 'down',
                'showactive': True
            }
        ]
    )

    fig_map.write_html('mapa.html', auto_open=True)
