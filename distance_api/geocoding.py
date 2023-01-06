import googlemaps
from constants import api_key
from bokeh.io import show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap



gmaps = googlemaps.Client(key=api_key)

bokeh_width = 1200
bokeh_height = 1050

def get_geocode(location):
    geocode_result = gmaps.geocode(location)
    lat_lng = geocode_result[0]["geometry"]["location"]
    return [lat_lng["lat"],lat_lng["lng"]]


def map_points(lat:list, lng:list ):
    average_lat = sum(lat)/len(lat)
    average_lng = sum(lng)/len(lng)

    bokeh_width = 1050
    bokeh_height = 1050
    map_options = GMapOptions(lat=average_lat, lng=average_lng, map_type="roadmap",zoom =7)
    p = gmap(api_key, map_options,  width=bokeh_width, height=bokeh_height)
    source = ColumnDataSource(
        data=dict(lat=lat,
                lon=lng)
    )
    p.circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, source=source)
    return(p)

def visualize_map(locations:list):
    lat = []
    lng = []
    for loc in locations:
        results = get_geocode(loc)
        print(results)
        lat.append(results[0])
        lng.append(results[1])
        p = map_points(lat,lng)
    show(p)
    return(p)