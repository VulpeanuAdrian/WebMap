import folium
import pandas

data = pandas.read_csv("Volcanoes.csv.csv")  #open csv file with volcanoes data

lat = list(data["LAT"])      #create a lists with volcanoes latitute,longitude,elevantion
lon = list(data["LON"])
elevantion = list(data["ELEV"])


def color_producer(el):
    '''Function created in order to choose different colors based on volcanoes elevation'''
    if el < 1001:
        return 'green'
    elif el > 1000 and el < 2001:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[45.0798, 24.0835], zoom_start=10, tiles="Stamen Terrain") #create a folium map object
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elevantion):
    fgv.add_child(folium.CircleMarker((lt, ln), popup=str(el),
                                     color=color_producer(el),fill=True,
                                     fill_color=color_producer(el),fill_opacity=0.8))  #add circles on eack volcanoe object depending
                                                                                       #of volcanoes elevation         
fgp=folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005']<1500000
                                                      else 'orange' if 1500000<=x['properties']['POP2005']
                                                      <3500000 else 'red'}))  #mark all country with a population under 15m with yellow
                                                      #between 15m-35m orange, over 35m red
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl( )) #add a layer control object in order to un-check the Population marks
print(map)
map.save("MapValcea.html")
