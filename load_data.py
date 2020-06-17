import pandas as pd
import numpy as np
import urllib.request
import requests
import urllib
import wget
import zipfile
import os

data = pd.read_csv("all_routes.csv")
def print_stop_list():
    routes_list = data.route_id.values.tolist()
    routes_list = list(dict.fromkeys(routes_list))

    trip_list = data.trip_id.values.tolist()
    trip_list = list(dict.fromkeys(trip_list))


    stop_list = []
    for tripID in trip_list:
        temp_trip = data[data.trip_id == tripID]
        temp_list_trip = temp_trip.stop_name.values.tolist()
        for element in temp_list_trip:
            if not element in stop_list:
                temp_list_trip = list(dict.fromkeys(temp_list_trip))
                stop_list.append(element)

    #np.savetxt("./list_of_stops.csv", stop_list, delimiter=",", fmt='%s')
    #print(stop_list)

def making_data_for_drawing(name1, name2):
    GW = data[(data.stop_name == name1) | (data.stop_name == name2)]
    GW_duplicate = GW[GW.duplicated(['trip_id'])]
    GW_trip_id_column = GW_duplicate["trip_id"].reset_index(drop=True)
    GW_list = GW_trip_id_column.values.tolist()

    data_route = data.loc[data['trip_id'].isin(GW_list)]



#odvojit u funkciju: Brise stanice prije i poslije name1 / 2 
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
            

    #transform = data_clean_route
    stop_list = list(data_clean_route.stop_name.value_counts().index)

    
    
# u svoju funkciju:   poslozi stanice po redu
    final_stop_list = [name1, name2]
    for tripID in GW_list:
        temp = data_clean_route[data_clean_route.trip_id == tripID]
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
            
    
    transform_columns = ["trip_id", "direction", "trip_short_name"]
    transform_columns.extend(final_stop_list)
    
    final_data = pd.DataFrame(columns=transform_columns)
    
    
# fill matrix with times    
    for tripID in GW_list:
        temp = data_clean_route[data_clean_route.trip_id == tripID]
        stopsNumber = temp.stop_sequence.count()
        temp_row = pd.DataFrame(columns=transform_columns)
        temp_row = temp_row.append({"trip_id" : int(tripID)}, ignore_index = True)
        #temp_row["trip_id"] = tripID
        temp_row["direction"] = temp.direction.mean()
        temp_row["trip_short_name"] = temp.trip_short_name.iloc[0]
        for stop in final_stop_list:
            try:
                temp_time = temp.loc[temp["stop_name"] == stop, "departure_time"].iloc[0]
            except IndexError:
                temp_time = "-"
            temp_row[stop] = temp_time
        
        final_data = final_data.append(temp_row)
    
    final_data.trip_id = final_data.trip_id.astype(np.uint8)
    final_data.direction = final_data.direction.astype(np.uint8)
    final_data = final_data.reset_index(drop=True)

    if final_data.empty:
        print("No available routes!")
    else:
        final_data.to_csv((str(name1)+" - "+str(name2)+".csv"), encoding='utf-8', index=False)
        print(final_data)
            
    


station1 = input("Write start station: ")
station2 = input("Write end station: ")
#station1 = "Graz Hbf"
#station2 = "Wien Hbf"

try:
    making_data_for_drawing(station1, station2)
except:
    print("No available routes!")






