#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import urllib.request
import wget


# # Importing data and preprocesing

# In[79]:


print('Downloading...')

calendar = 'https://data.oebb.at/oebb?dataset=uddi:cd36722f-1b9a-11e8-8087-b71b4f81793a&file=uddi:d3e25791-7889-11e8-8fc8-edb0b0e1f0ef/calendar.csv'
calendar_dates = 'https://data.oebb.at/oebb?dataset=uddi:cd36722f-1b9a-11e8-8087-b71b4f81793a&file=uddi:d3e25791-7889-11e8-8fc8-edb0b0e1f0ef/calendar_dates.csv'
agency = 'https://data.oebb.at/oebb?dataset=uddi:cd36722f-1b9a-11e8-8087-b71b4f81793a&file=uddi:d3e25791-7889-11e8-8fc8-edb0b0e1f0ef/agency.csv'
trips = 'https://data.oebb.at/oebb?dataset=uddi:cd36722f-1b9a-11e8-8087-b71b4f81793a&file=uddi:d3e25791-7889-11e8-8fc8-edb0b0e1f0ef/trips.csv'
stops = 'https://data.oebb.at/oebb?dataset=uddi:cd36722f-1b9a-11e8-8087-b71b4f81793a&file=uddi:d3e25791-7889-11e8-8fc8-edb0b0e1f0ef/stops.csv'
routes = 'https://data.oebb.at/oebb?dataset=uddi:cd36722f-1b9a-11e8-8087-b71b4f81793a&file=uddi:d3e25791-7889-11e8-8fc8-edb0b0e1f0ef/routes.csv'
transfers = 'https://data.oebb.at/oebb?dataset=uddi:cd36722f-1b9a-11e8-8087-b71b4f81793a&file=uddi:d3e25791-7889-11e8-8fc8-edb0b0e1f0ef/transfers.csv'
stop_times = 'https://data.oebb.at/oebb?dataset=uddi:cd36722f-1b9a-11e8-8087-b71b4f81793a&file=uddi:d3e25791-7889-11e8-8fc8-edb0b0e1f0ef/stop_times.csv'

#urllib.request.urlretrieve(calendar1, 'data/calendar.csv')
#urllib.request.urlretrieve(calendar_dates, 'data/calendar_dates.csv')
#urllib.request.urlretrieve(agency, 'data/agency.csv')
#urllib.request.urlretrieve(trips, 'data/trips.csv')
#urllib.request.urlretrieve(stops, 'data/stops.csv')
#urllib.request.urlretrieve(routes, 'data/routes.csv')
#urllib.request.urlretrieve(transfers, 'data/transfers.csv')
#urllib.request.urlretrieve(stop_times, 'data/stop_times.csv')
print('...Finished')


# In[4]:


data1 = pd.read_csv("data/stop_times.csv")
data2 = pd.read_csv("data/stops.csv")
data3 = pd.read_csv("data/trips.csv")


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


data3 = data3.dropna(axis=1)


# In[11]:


data = pd.merge(data1, data2,  how='left', left_on=['stop_id'], right_on = ['stop_id'])


# In[12]:


data = pd.merge(data, data3,  how='left', left_on=['trip_id'], right_on = ['trip_id'])


# In[14]:


data.head() 


# In[44]:


name1 = "Graz Hbf"
name2 = "Wien Hbf"

GW = data[(data.stop_name == name1) | (data.stop_name == name2)]


# In[45]:


GW.head()


# In[ ]:


#GW_duplicate = GW[GW.duplicated(['trip_id'], keep=False)]


# In[17]:


GW_duplicate = GW[GW.duplicated(['trip_id'])]


# In[18]:


GW_duplicate.head()


# In[19]:


GW_trip_id_column = GW_duplicate["trip_id"].reset_index(drop=True)


# In[22]:


GW_trip_id_column.head()


# In[23]:


GW_list = GW_trip_id_column.values.tolist()


# In[24]:


print(len(GW_list))


# In[145]:


#GW_list


# In[39]:


data_route = data.loc[data['trip_id'].isin(GW_list)]


# In[43]:


data_route.head(10)


# In[42]:


data_route.to_csv("final_route.csv", encoding='utf-8', index=False)


# In[ ]:




