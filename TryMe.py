#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import urllib.request
import requests
import urllib
import wget
import zipfile


# # Importing data and preprocesing

# In[55]:


print('Downloading...')
#this link still doesnt work.... 
#will fix when they answer my emails... 
#can be exchanged for any other database system with this kind of shema
#downloaddata = 'https://data.oebb.at/oebb?dataset=uddi:cd36722f-1b9a-11e8-8087-b71b4f81793a&file=uddi:d3e25791-7889-11e8-8fc8-edb0b0e1f0ef/GFTS_Fahrplan_OEBB_20191211.zip'

#urllib.request.urlretrieve(downloaddata, 'data/zip.zip')
#print('...Finished')


# In[23]:


#url = 'https://data.oebb.at/oebb/?dataset=uddi:cd36722f-1b9a-11e8-8087-b71b4f81793a&file=uddi:d3e25791-7889-11e8-8fc8-edb0b0e1f0ef/GFTS_Fahrplan_OEBB_20191211.zip'
#r = requests.get(url)
#with open("data/zip.zip", "wb") as code:
#    code.write(r.content)
#urllib.request.urlretrieve(url, "data/zip.zip")


# In[3]:


with zipfile.ZipFile(r"C:\Users\Sven-PC\Documents\GitHub\Information-Visualisation\data\OBB.zip", 'r') as zip_ref:
    zip_ref.extractall("data")


# In[4]:


data1 = pd.read_csv("data/stop_times.txt")
data2 = pd.read_csv("data/stops.txt")
data3 = pd.read_csv("data/trips.txt")


# In[5]:


data1.head()


# In[6]:


data2.head()


# In[7]:


data3.head()


# In[8]:


data1 = data1.dropna(axis=1)


# In[9]:


data2 = data2.dropna(axis=1)


# In[10]:


data3 = data3.drop(["service_id", "direction_id", "block_id", "shape_id", "trip_type"], axis=1)


# In[11]:


data = pd.merge(data1, data2,  how='left', left_on=['stop_id'], right_on = ['stop_id'])


# In[12]:


data = pd.merge(data, data3,  how='left', left_on=['trip_id'], right_on = ['trip_id'])


# In[24]:


data.head(50) 


# In[25]:


data.route_id.value_counts()


# In[14]:


routes_list = data.route_id.values.tolist()


# In[16]:


routes_list = list(dict.fromkeys(routes_list))


# In[30]:


for routeID in routes_list:
    temp = data[data.route_id == routeID]
    temp_list = temp.stop_name.values.tolist()
    temp_list = list(dict.fromkeys(temp_list))
    print(len(temp_list))
    
    
    
    


# In[27]:


len(temp_list)


# In[ ]:





# In[ ]:


#!/usr/bin/python3

import sys, getopt

#def main(argv):
#   station1 = ''
#   station2 = ''
#   try:
#      opts, args = getopt.getopt(argv,"hs:f:",["sfile=","ffile="])
#   except getopt.GetoptError:
#      print ('test.py -s <station1> -f <station2>')
#      sys.exit(2)
#   for opt, arg in opts:
#      if opt == '-h':
#         print ('test.py -s <station1> -f <station2>')
#         sys.exit()
#      elif opt in ("-s", "--sfile"):
#         station1 = arg
#      elif opt in ("-f", "--ffile"):
#         station2 = arg
#   print ('Station 1 is "', station1)
#   print ('Station 2 is "', station2)
#
#if __name__ == "__main__":
#   main(sys.argv[1:])


# In[35]:


station1 = input(print("Write start station: "))


# In[40]:


station2 = input(print("Write end station: "))


# In[41]:


station2


# In[20]:


name1 = station1
name2 = station2

GW = data[(data.stop_name == name1) | (data.stop_name == name2)]


# In[21]:


GW_duplicate = GW[GW.duplicated(['trip_id'])]


# In[22]:


GW_duplicate.head()


# In[23]:


GW_trip_id_column = GW_duplicate["trip_id"].reset_index(drop=True)


# In[24]:


GW_list = GW_trip_id_column.values.tolist()


# In[25]:


print(len(GW_list))


# In[26]:


data_route = data.loc[data['trip_id'].isin(GW_list)]


# In[27]:


data_route.head(10)


# In[28]:


columns = data_route.columns
data_clean_route = pd.DataFrame(columns=columns)
data_clean_route["start"] = ""
data_clean_route["stop"] = ""
data_clean_route["direction"] = ""

for tripID in GW_list:
    flag = False
    temp = data_route[data_route.trip_id == tripID]
    temp["start"] = ""
    temp["stop"] = ""
    temp["direction"] = ""
    stopsNumber = temp.stop_sequence.count()
    for i in range(stopsNumber):
        stopName = temp.stop_name.values[i]
        if( (stopName == name1 or stopName == name2) and flag == False):
            firstStop = stopName
            if firstStop == name1:
                secondStop = name2
            else:
                secondStop = name1
            flag = True
            temp.loc[temp.stop_sequence == i+1, 'start'] = firstStop
            temp.loc[temp.stop_sequence == i+1, 'stop'] = secondStop
            if(firstStop == name1):
                temp.loc[temp.stop_sequence == i+1, 'direction'] = 0
            else:
                temp.loc[temp.stop_sequence == i+1, 'direction'] = 1
            data_clean_route = data_clean_route.append(temp[temp.stop_sequence == i+1])
        elif(flag and (stopName == name1 or stopName == name2)):
            flag = False
            temp.loc[temp.stop_sequence == i+1, 'start'] = firstStop
            temp.loc[temp.stop_sequence == i+1, 'stop'] = secondStop
            if(firstStop == name1):
                temp.loc[temp.stop_sequence == i+1, 'direction'] = 0
            else:
                temp.loc[temp.stop_sequence == i+1, 'direction'] = 1
            data_clean_route = data_clean_route.append(temp[temp.stop_sequence == i+1])
        elif(flag):
            temp.loc[temp.stop_sequence == i+1, 'start'] = firstStop
            temp.loc[temp.stop_sequence == i+1, 'stop'] = secondStop
            if(firstStop == name1):
                temp.loc[temp.stop_sequence == i+1, 'direction'] = 0
            else:
                temp.loc[temp.stop_sequence == i+1, 'direction'] = 1
            data_clean_route = data_clean_route.append(temp[temp.stop_sequence == i+1])
            


# In[29]:


data_clean_route.head(20)


# ## Saving the data

# In[30]:


data_clean_route.to_csv((name1 + "-" +  name2 +".csv"), encoding='utf-8', index=False)


# ## Transforming the table in prefered format
# 

# In[31]:


transform = pd.read_csv("Graz_Hbf-Wien_Hbf.csv")


# In[32]:


transform.head()


# In[33]:


stop_list = list(data_clean_route.stop_name.value_counts().index)


# In[34]:


stop_list


# In[35]:


final_stop_list = [name1, name2]
for tripID in GW_list:
    temp = transform[transform.trip_id == tripID]
    stopsNumber = temp.stop_sequence.count()
    for i in range(stopsNumber):
        stopName = temp.stop_name.values[i]
        if(stopName in final_stop_list):
            if(i == 0):
                if(stopName == name1):
                    flag = 0
                else:
                    flag = 1
            continue
        elif(i>0):
            previousStop = temp.stop_name.values[i-1]
            index = final_stop_list.index(previousStop)
            if(flag == 0):
                #if previousStop in final_stop_list:
                final_stop_list.insert(index + 1, stopName)
            else:
                final_stop_list.insert(index, stopName)
                
        # ako je prvi kojeg gledas provjeri ako je name 1 ili name 2 i onda okreni provjeravanje na drugu stranu
        
        


# In[36]:


final_stop_list


# In[37]:


transform_columns = ["trip_id", "direction"]


# In[38]:


transform_columns.extend(final_stop_list)


# In[39]:


transform_columns


# In[40]:


data_clean_route = pd.DataFrame(columns=transform_columns)


# In[41]:


data_clean_route


# In[42]:



for tripID in GW_list:
    temp = transform[transform.trip_id == tripID]
    stopsNumber = temp.stop_sequence.count()
    temp_row = pd.DataFrame(columns=transform_columns)
    temp_row = temp_row.append({"trip_id" : int(tripID)}, ignore_index = True)
    #temp_row["trip_id"] = tripID
    temp_row["direction"] = temp.direction.mean()
    for stop in final_stop_list:
        try:
            temp_time = temp.loc[temp["stop_name"] == stop, "departure_time"].iloc[0]
        except IndexError:
            temp_time = "-"
        temp_row[stop] = temp_time
    
    data_clean_route = data_clean_route.append(temp_row)
        


# In[43]:


data_clean_route.trip_id = data_clean_route.trip_id.astype(np.uint8)
data_clean_route.direction = data_clean_route.direction.astype(np.uint8)


# In[46]:


data_clean_route = data_clean_route.reset_index(drop=True)


# In[50]:


data_clean_route.head(15)


# In[47]:


data_clean_route.to_csv(("GW.csv"), encoding='utf-8', index=False)


# In[ ]:




