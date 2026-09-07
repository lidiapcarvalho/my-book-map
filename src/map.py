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

    # Reseta o índice para que possamos ter uma coluna com os países
    map_data = country_counts.reset_index()
    map_data.columns = ['country', 'books']

    # Junta os dados do último ano lido
    map_data = map_data.merge(latest_year, on='country')

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
        hover_data={'books': True, 'iso_alpha': False},
        color_continuous_scale='Blues',
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

    fig_map.write_html('mapa.html', auto_open=True)
