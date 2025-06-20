import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = "browser"

locations = {
    'New York': {'lat': 40.7128, 'lon': -74.0060},
    'London': {'lat': 51.5074, 'lon': -0.1278},
    'Tokyo': {'lat': 35.6895, 'lon': 139.6917},
    'Sydney': {'lat': -33.8688, 'lon': 151.2093},
    'Cairo': {'lat': 30.0444, 'lon': 31.2357}
}

lats = [loc['lat'] for loc in locations.values()]
lons = [loc['lon'] for loc in locations.values()]
names = list(locations.keys())

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    lon=lons,
    lat=lats,
    text=names,
    mode='markers+text',
    marker=dict(size=6, color='red'),
    textposition='top center'
))

fig.update_layout(
    title='Preliminary Interactive Globe',
    geo=dict(
        projection_type='orthographic',  
        showland=True,
        landcolor='rgb(243, 243, 243)',
        showcountries=True,
        showocean=True,
        showrivers=True,
        riverwidth=2,
        showlakes=True,
        oceancolor='lightblue',
        lakecolor="lightblue",
        lataxis=dict(showgrid=True),
        lonaxis=dict(showgrid=True),
    ),
    margin=dict(l=0, r=0, t=50, b=0)
)

fig.show()
