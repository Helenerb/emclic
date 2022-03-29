# Script for downloading hadCRUT5 data

import requests as re  # library for getting stuff from urls
import os  # operating system through python script

# Download link
url = "https://crudata.uea.ac.uk/cru/data/temperature/HadCRUT.5.0.1.0.analysis.anomalies.ensemble_mean.nc"

data = re.get(url, allow_redirects = True)

with open("HadCrut.5.0.1.0.analysis.anomalies.ensemble_mean.nc", "wb") as f:
    f.write(data.content)

