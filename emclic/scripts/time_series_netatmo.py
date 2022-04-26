# Loads data for Warsaw and Madrid from different sources, plots time series for max temperature and humidity


import cdo as cdo  # cdo for python library
import xarray as xr  # xarray for formatting netcdf files
import os
import matplotlib.pyplot as plt

stations_warsaw = ['121051', '123750']
stations_madrid = ['082210', '082230', '082240', '082270']

madrid_ds = [ xr.open_dataset(os.path.join('data', 'madrid_{}.nc'.format(station))) for station in stations_madrid]

warsaw_ds = [ xr.open_dataset(os.path.join('data', 'warsaw_{}.nc'.format(station))) for station in stations_warsaw]

madrid_hum_ds = [ xr.open_dataset(os.path.join('data', 'madrid_{}_humidity.nc'.format(station))) for station in stations_madrid]

warsaw_hum_ds = [ xr.open_dataset(os.path.join('data', 'warsaw_{}_humidity.nc'.format(station))) for station in stations_warsaw]

# nice color palette:

shades_of_blue = ['teal', 'aqua', 'lightblue', 'deepskyblue', 'steelblue', 'dodgerblue', 'cornflowerblue']

# Temperatures, Warsaw:
warsaw_temps = [ds['temperatures'].where(ds.temperatures != -2e+30) for ds in warsaw_ds ]

fig, ax = plt.subplots(nrows=1, ncols = 1)

for idx, station in enumerate(warsaw_temps):
    station.plot(color = shades_of_blue[idx], linewidth = 0.5, ax = ax, label = stations_warsaw[idx], marker = ".")

plt.legend()
fig.suptitle("Dry bulb air temperature for two weather stations in Warsaw")
plt.show()


# Temperatures, Madrid
madrid_temps = [ds['temperatures'].where(ds.temperatures != -2e+30) for ds in madrid_ds] 

fig, ax = plt.subplots(nrows=1, ncols = 1)

for idx, station in enumerate(madrid_temps):
    station.plot(color = shades_of_blue[idx], linewidth = 0.5, ax = ax, label = stations_madrid[idx], marker = ".")

plt.legend()
fig.suptitle("Dry bulb air temperature for four weather stations in Madrid")
plt.show()

# Humidity, Warsaw:
warsaw_hum = [ds['specific_humidity'].where(ds['specific_humidity'] != -2e+30) for ds in warsaw_hum_ds]

fig, ax = plt.subplots(nrows = 1, ncols = 1)

for idx, station in enumerate(warsaw_hum):
    station.plot(color = shades_of_blue[idx], linewidth = 0.5, ax = ax, label = stations_warsaw[idx], marker = ".")

plt.legend()
fig.suptitle("Specific humidity for two weather stations in Warsaw")
plt.show()

# Humidity, Madrid:
madrid_hum = [ds['specific_humidity'].where(ds['specific_humidity'] != -2e+30) for ds in madrid_hum_ds]

fig, ax = plt.subplots(nrows = 1, ncols = 1)

for idx, station in enumerate(madrid_hum):
    station.plot(color = shades_of_blue[idx], linewidth = 0.5, ax = ax, label = stations_madrid[idx], marker = ".")

plt.legend()
fig.suptitle("Specific humidity for four weather stations in Madrid")
plt.show()






