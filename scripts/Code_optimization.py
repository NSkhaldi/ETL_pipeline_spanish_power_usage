import pandas as pd # used version: 1.0.5
import numpy as np # used version: 1.18.5
import time


#Load data and extract only the needed features
spd_opt_data = pd.read_csv('../data/dataset_speed_optimization.csv')
spd_opt_data=spd_opt_data[['latitude','longitude']]



print("\n***********  TIME OPTIMIZATION:*******************\n")

start = time.time()
#Function to apply to all rows in the DataFrame
def functiontoapply_first(lat,lon):
    a=np.sin(lat/2)**2+np.cos(lat)*np.cos(lon)*np.sin(lon/2)**2
    return a
#Add new column to the DataFrame
listresults=[]
for i in range ( 0 ,len(spd_opt_data)):
    r = functiontoapply_first(spd_opt_data.iloc[i]['latitude'],spd_opt_data.iloc[i]['longitude'])
    listresults.append(r)
spd_opt_data['distance']=listresults

end = time.time()
print("\nexecution time before optimization:   "+ str(end - start)+" s")



#Time optimization
start = time.time()
def functiontoapply_third(lat,lon):
    return np.sin(lat/2)**2+np.cos(lat)*np.cos(lon)*np.sin(lon/2)**2
spd_opt_data['distances']= functiontoapply_third(spd_opt_data['latitude'], spd_opt_data['longitude'])

end = time.time()
print("\nexecution time after optimization:   "+ str(end - start)+" s")





print("\n\n\n***********  MEMORY OPTIMIZATION:*******************\n")


print("\n\n\nmemory usage before optimization:\n")
mem_opt_data = pd.read_csv('../data/dataset_memory_optimization.csv')
mem_opt_data.info(memory_usage='deep')


print("\n\nmemory usage after first optimization:\n")
mem_opt_data_opt = pd.read_csv('../data/dataset_memory_optimization.csv', dtype={"ean_hotel_id": "uint32",
                                                                            "name": "string",
                                                                            "address1": "string",
                                                                            "city": "category",  
                                                                            "state_province": "category",
                                                                            "postal_code": "category",
                                                                            "latitude": "float16",
                                                                            "longitude": "float16", 
                                                                            "star_rating": "float16",
                                                                            "high_rate": "float32", 
                                                                            "low_rate": "float32"})

mem_opt_data_opt.info(memory_usage='deep')


print("\n\nmemory usage after second optimization:\n")
mem_opt_data_opt = pd.read_csv('../data/dataset_memory_optimization.csv', dtype={"ean_hotel_id": "category",
                                                                            "name": "category",
                                                                            "address1": "category",
                                                                            "city": "category",  
                                                                            "state_province": "category",
                                                                            "postal_code": "category",
                                                                            "latitude": "category",
                                                                            "longitude": "category", 
                                                                            "star_rating": "category",
                                                                            "high_rate": "category", 
                                                                            "low_rate": "category"})

mem_opt_data_opt.info(memory_usage='deep')