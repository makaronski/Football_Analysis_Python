# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 23:33:39 2018

@author: makar
"""

import http.client
import json
import pandas as pd
from pandas.io.json import json_normalize
import sys
import io

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'b609904fbfc44877b6359d54d7f19ddf' }
connection.request('GET', 'http://api.football-data.org/v2/competitions/2014/matches?season=2017', None, headers )
#response = json.loads(connection.getresponse().read().decode()) #Creates a dictionary object, hard to flatten
response2 = json.dumps(connection.getresponse().read().decode())

dff=json.loads(response2) #Here it is a proper json code ready to export to csv, but is in string
#### NEED TO FIND A WAY TO EXPORT DIRECTLY FROM HERE####
dff2=json.loads(dff) ### Here it is a dictionary
#print(dff2)
print(type(dff))
#response = response.replace("'", '"')
#print (response2)
df = json_normalize(dff2,record_path='matches')
#print(df)
#result = pd.read_json(response)
#dff2.to_csv(path_or_buf='C:\\Users\\makar\\.spyder-py3\\Data_Visualization\\asd.csv')
#data = pd.DataFrame.from_dict(response, orient='index')
#print(data.head())

#with open('C:\\Users\\makar\\.spyder-py3\\Data_Visualization\\CL.txt','a') as createdfile:
 #   createdfile.write(dff)
    
with io.open('C:\\Users\\makar\\.spyder-py3\\Data_Visualization\\Primera_Division_2017-2018.txt', "a", encoding="utf-8") as f:
    f.write(dff)