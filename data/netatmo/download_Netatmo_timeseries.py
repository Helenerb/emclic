# Script for downloading a time series for one weather variable, for one netatmo weather station

import requests as re
from requests.structures import CaseInsensitiveDict

# Get access token from txt file:
with open("netatmo_access_token.txt", "r") as f:
    access_token = f.readlines()

access_token = access_token[0].rstrip("\n")

url = "https://api.netatmo.com/api/getmeasure"

# create a dictionary containing the headers of the request
headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer {}".format(access_token)

# create dictionary containing parameters of the request
params = CaseInsensitiveDict()
params["device_id"] = "70:ee:50:13:3e:c2"  # example id
params["module_id"] = "02:00:00:13:41:6a"  # example
params["scale"] = "30min"  # lowest temporal resolution
params["type"] = "temperature"  #  data type
params["optimize"] = "false"  # usually set this to false, unless worried about band width
params["real_time"] = "false"  # default, a bit unsure about this. Offsets data not at max resolution by scale/2

response = re.get(url, headers=headers, params=params)

print("\n response: \n", response)

with open("test_time_series_download.json", "wb") as f:
    f.write(response.content)

print("\n Content: \n", response.content)
