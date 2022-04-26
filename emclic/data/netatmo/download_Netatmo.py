# Script for downloading netatmo weather station data

import requests as re
import os
from requests.structures import CaseInsensitiveDict
import json

# Get access token from txt file:
with open("netatmo_access_token.txt", "r") as f:
    access_token = f.readlines()

access_token = access_token[0].rstrip("\n")

# create a dictionary containing the headers of the request
headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer {}".format(access_token)

print("headers: \n", headers, "\n")

#url = "https://api.netatmo.com/api/getpublicdata?lat_ne=40.6&lon_ne=-3.4&lat_sw=40.1&lon_sw=-4&required_data=temperature&filter=true"
url = "https://api.netatmo.com/api/getpublicdata"

# create a dictionary containing the parameters of the request
params = CaseInsensitiveDict()

#Enter coordinates:
params['lat_ne'] = 40.6
params['lon_ne'] = -3.4
params['lat_sw'] = 40.1
params['lon_sw'] = -4
params['required_data'] = 'temperature'
params['filter'] = 'true'

print("Params: \n", params, "\n")

data = re.get(url, headers=headers, params=params, verify=True)  # Expect to get a json file

print("Response: \n", data, "\n")
print("Headers: \n", data.headers, "\n")

with open("station_data_madrid_netatmo.json", "wb") as f:
    f.write(data.content)

print("Content: \n", data.content, "\n")
