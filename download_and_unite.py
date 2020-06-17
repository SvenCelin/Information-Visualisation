import pandas as pd
import numpy as np
import urllib.request
import requests
import urllib
import wget
import zipfile
import os


#print('Downloading...')
#this link still doesnt work.... 
#will fix when they answer my emails... 
#can be exchanged for any other database system with this kind of shema
#downloaddata = 'https://data.oebb.at/oebb?dataset=uddi:cd36722f-1b9a-11e8-8087-b71b4f81793a&file=uddi:d3e25791-7889-11e8-8fc8-edb0b0e1f0ef/GFTS_Fahrplan_OEBB_20191211.zip'

#urllib.request.urlretrieve(downloaddata, 'data/zip.zip')
#print('...Finished')


with zipfile.ZipFile("./data/OBB.zip", 'r') as zip_ref:
    zip_ref.extractall("data")

data1 = pd.read_csv("./data/stop_times.txt")
data2 = pd.read_csv("./data/stops.txt")
data3 = pd.read_csv("./data/trips.txt")



data1.head()
data2.head()
data3.head()

data1 = data1.dropna(axis=1)
data2 = data2.dropna(axis=1)
data3 = data3.drop(["service_id", "direction_id", "block_id", "shape_id", "trip_type"], axis=1)
data = pd.merge(data1, data2,  how='left', left_on=['stop_id'], right_on = ['stop_id'])
data = pd.merge(data, data3,  how='left', left_on=['trip_id'], right_on = ['trip_id'])

data.head(10) 
data.to_csv(("./all_routes.csv"), encoding='utf-8', index=False)
