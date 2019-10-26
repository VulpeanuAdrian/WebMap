import folium
import pandas

data = pandas.read_csv("Volcanoes.csv.csv")

lat = list(data["LAT"])
lon = list(data["LON"])
elevantion = list(data["ELEV"])


def color_producer(el):
    if el < 1001:
        return 'green'
    elif el > 1000 and el < 2001:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[45.0798, 24.0835], zoom_start=10, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elevantion):
    fgv.add_child(folium.CircleMarker((lt, ln), popup=str(el),
                                     color=color_producer(el),fill=True,
                                     fill_color=color_producer(el),fill_opacity=0.8))

fgp=folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005']<1500000
                                                      else 'orange' if 1500000<=x['properties']['POP2005']
                                                      <3500000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl( ))
print(map)
map.save("MapValcea.html")
print(lon)

print(data)
print(elevantion)
print(help(folium.CircleMarker))