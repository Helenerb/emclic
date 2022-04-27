# Downloading hadISD files
# downloads data from one weather station in Madrid, the 082210 weather station,
# north-east of Madrid city

import requests as re
import os

# The ids for the weathers stations in (a reasonably short distance from) Madrid and Warsaw
madrid_stations = ['082210', '082230', '082240', '082270']
warsaw_stations = ['121051', '123750']
warsaw_outliers = ['123760']

# Downloading the "individual station data"

for station in madrid_stations:
    # measured temperature, dewpoint, wind speed, wind direction, sea level pressure and station level pressure
    url = "https://www.metoffice.gov.uk/hadobs/hadisd/v330_202201p/data/hadisd.3.3.0.202201p_19310101-20220201_{}-99999.nc.gz".format(station)
    data = re.get(url, allow_redirects=True)
    open("madrid_{}.nc.gz".format(station), "wb").write(data.content)

    # calculated vapor pressure, saturation vapor pressure, specific humidity, relative humidity
    url = "https://www.metoffice.gov.uk/hadobs/hadisd/v330_202201p/data/hadisd.3.3.0.202201p_19310101-20220201_{}-99999_humidity.nc.gz".format(station)
    data = re.get(url, allow_redirects=True)
    open("madrid_{}_humidity.nc.gz".format(station), "wb").write(data.content)

    # calculated apparent temperature
    url = "https://www.metoffice.gov.uk/hadobs/hadisd/v330_202201p/data/hadisd.3.3.0.202201p_19310101-20220201_{}-99999_heat_stress.nc.gz".format(station)
    data = re.get(url, allow_redirects=True)
    open("madrid_{}_heat_stress.nc.gz".format(station), "wb").write(data.content)

    
for station in warsaw_stations:
    # measured temperature, dewpoint, wind speed, wind direction, sea level pressure and station level pressure
    url = "https://www.metoffice.gov.uk/hadobs/hadisd/v330_202201p/data/hadisd.3.3.0.202201p_19310101-20220201_{}-99999.nc.gz".format(station)
    data = re.get(url, allow_redirects=True)
    open("warsaw_{}.nc.gz".format(station), "wb").write(data.content)

    # calculated vapor pressure, saturation vapor pressure, specific humidity and relative humidity
    url = "https://www.metoffice.gov.uk/hadobs/hadisd/v330_202201p/data/hadisd.3.3.0.202201p_19310101-20220201_{}-99999_humidity.nc.gz".format(station)
    data = re.get(url, allow_redirects=True)
    open("warsaw_{}_humidity.nc.gz".format(station), "wb").write(data.content)

    # calculated apparent temperature
    url = "https://www.metoffice.gov.uk/hadobs/hadisd/v330_202201p/data/hadisd.3.3.0.202201p_19310101-20220201_{}-99999_heat_stress.nc.gz".format(station)
    data = re.get(url, allow_redirects=True)
    open("warsaw_{}_heat_stress.nc.gz".format(station), "wb").write(data.content)

# Unpack zipped files
os.system("gzip -d *.nc.gz")




