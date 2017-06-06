# -*- coding: utf-8 -*-
"""
Created on Thu May 18 13:15:38 2017

@author: Shwet
"""

import folium
import pandas as pd
import vincent
sbucks = pd.read_csv('starbucks_india.csv')

map_mumbai = folium.Map(location = [19.0760,72.8777])

for index, row in sbucks.iterrows():
    lis = [row['Mon'],row['Tue'],row['Wed'],row['Thu'],row['Fri'],row['Sat'],row['Sun']]
    x = range(len(lis))
    bar = vincent.Bar(lis,width=440, height=200)
    bar.axis_titles(x='Day of Week - '+row['Name'], y='Foot fall')
    bar.to_json('vega.json')
    popup_ = folium.Popup(max_width=800).add_child(folium.Vega(bar, width=500, height=250))
    if sum(lis) > 2600:
        folium.Marker([row['Latitude'],row['Longitude']], popup=popup_,icon=folium.Icon(color='red',icon='star')).add_to(map_mumbai)
    else:
        folium.Marker([row['Latitude'],row['Longitude']], popup=popup_,icon=folium.Icon(color='green',icon='star-empty')).add_to(map_mumbai)        

map_mumbai.save('starbucks_india.html')

