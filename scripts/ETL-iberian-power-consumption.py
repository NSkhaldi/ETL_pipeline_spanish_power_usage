import pandas as pd 
import numpy as np 
import requests
import json
from pandas.io.json import json_normalize
import pymysql
import csv


#EXTRACT

text="Previsión diaria de la demanda eléctrica peninsular"
token="0a3ec68a89579911bd7610e20df0f79c83f79b10275b19025aaf414136c91f9a"
start_date='2017-01-01'
end_date='2018-12-31'
payload = {"Accept": "application/json; application/vnd.esios-api-v1+json", 
          "Content-Type": "application/json",
          "Host": "api.esios.ree.es",
          "Authorization": "Token token=\""+token+"\""}


# Search for the right indicator id

#base_url = "https://api.esios.ree.es/search?query="+text
#r = requests.get(base_url,headers=payload)
#r.json()
# Request the hourly power demand forecast  from 2017-01-01 to 2018-12-31.
base_url_2 = "https://api.esios.ree.es/indicators/460?start_date="+start_date+"T00%3A00%3A00Z&end_date="+end_date+"T07%3A34%3A17Z&time_trunc=hour"
r2 = requests.get(base_url_2,headers=payload)
#r2.json()





#TRANSFORM


df = pd.json_normalize(r2.json()['indicator']['values'])
#Add update timestamp
df['values_updated_at']=r2.json()['indicator']['values_updated_at']
#Add update timestamp
df.rename(columns={'geo_id': 'id', 'geo_name':'name', 'values_updated_at': 'update timestamp', 'value' : 'demand forecast'}, inplace=True)
#Convert to "yyyy-mm-dd HH:MM:SS" format
df['datetime']=pd.to_datetime(df['datetime'], utc=True).astype('datetime64[ns]')
df['update timestamp']=pd.to_datetime(df['update timestamp'], utc=True).astype('datetime64[ns]')
#Drop extra columns
df.drop(['datetime_utc','tz_time'], axis=1, inplace=True)
#Sort columns
df = df.reindex(sorted(df.columns), axis=1)

#CSV file creation
df.to_csv("../output/Anass_etl.csv", index=False)






#LOAD

conn = pymysql.connect(host='localhost',
                       user='user1',
                       password='xxxx',
                       db='mock_db')

cursor=conn.cursor()
# creating column list for insertion
cols = "`,`".join([str(i) for i in df.columns.tolist()])

f = csv.reader(open('../output/Anass_etl.csv'))
sql = "INSERT INTO `mock_db`.`demand_forecast_esios` (`"+cols+"`) VALUES(%s,%s,%s,%s,%s)"
next(f) #skip the header line of csv
for line in f:
    line=[None if cell == '' else cell for cell in line]
    cursor.execute(sql, line)

conn.commit()
cursor.close()

print ("\ndata Imported")


print ("\n ETL PROCESS: success!")