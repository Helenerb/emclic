# Script for plots of comparison between eobs and era5 data

####    ----   Library imports    ----
import cartopy.crs as ccrs
import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


def eobsPath(filename):
    """Returns the filepath to storage for E-OBS data 
    
    Parameters
    ----------
    filename: string
        the name that should be given to the data

    Returns
    -------
    string
        the full file path to the E-OBS data file
    """
    return os.path.join("data/E-OBS", filename)

def era5Path(filename):
    """Returns the filepath to storage for ERA-5 data 
    
    Parameters
    ----------
    filename: string
        the name that should be given to the data

    Returns
    -------
    string
        the full file path to the ERA-5 data file
    """
    return os.path.join("data/ERA-5", filename)


###   ----   Plot plain differences between era-5 and E-obs for Warsaw and Madrid

# Gridplot, Madrid
ds_difference_madrid = xr.open_dataset("data/difference_era5_eobs_Madrid.nc")
ds_difference_warsaw = xr.open_dataset("data/difference_era5_eobs_Warsaw.nc")

# slice for dates where you have observations for both sets of data
ds_difference_warsaw = ds_difference_warsaw.sel(time = slice("1990-01-01", "2020-05-15"))
ds_difference_madrid = ds_difference_madrid.sel(time = slice("1990-01-01", "2020-05-15"))

june15ths = pd.to_datetime(["{}-06-15".format(year) for year in range(1990, 2020)])


ds_difference_june15_madrid = ds_difference_madrid.sel(time=june15ths)
ds_difference_june15_warsaw = ds_difference_warsaw.sel(time=june15ths)


fig, axes = plt.subplots(nrows = 4, ncols = 8, subplot_kw = {"projection" : ccrs.PlateCarree()}, sharey = True, figsize = (33,10))

fig.delaxes(axes[3,7])  # delete last axis, since we want uneven number
fig.delaxes(axes[3,6])

for i, ax in enumerate(axes.flat[:-2]):
    one_plot = ds_difference_june15_madrid.isel(time = i)["tx"].plot(ax = ax, transform = ccrs.PlateCarree(), add_colorbar = False, cmap = "viridis", vmin=-5, vmax=5)
    ax.set_title(pd.to_datetime(ds_difference_june15_madrid["time"][i].values).date())
    if i == 15:
        colorbar_plot = one_plot
    # Possibly add city lines here

fig.colorbar(colorbar_plot, ax = axes[:,:], location = "right", label = "Degrees Celcius")
fig.suptitle("Difference of max value between ERA-5 and E-OBS for Madrid")

fig.tight_layout()
#plt.subplots_adjust(wspace = 0.33)

plt.savefig("data/difference_june15_madrid.png")
plt.show()
plt.close()

# Warsaw

fig, axes = plt.subplots(nrows = 4, ncols = 8, subplot_kw = {"projection" : ccrs.PlateCarree()}, sharey = True, figsize = (33,10))

fig.delaxes(axes[3,7])  # delete last axis, since we want uneven number
fig.delaxes(axes[3,6])

for i, ax in enumerate(axes.flat[:-2]):
    one_plot = ds_difference_june15_warsaw.isel(time = i)["tx"].plot(ax = ax, transform = ccrs.PlateCarree(), add_colorbar = False, cmap = "viridis", vmin=-5, vmax=5)
    ax.set_title(pd.to_datetime(ds_difference_june15_warsaw["time"][i].values).date())
    if i == 15:
        colorbar_plot = one_plot
    # Possibly add city lines here

fig.colorbar(colorbar_plot, ax = axes[:,:], location = "right", label = "Degrees Celcius")
fig.suptitle("Difference of max value between ERA-5 and E-OBS for Warsaw")

fig.tight_layout()
#plt.subplots_adjust(wspace = 0.33)

plt.savefig("data/difference_june15_warsaw.png")
plt.show()
plt.close()

# Plot the same difference data as a time series:

shades_of_blue = ('aquamarine', 'turquoise', 'lightseagreen', 'teal', 'cadetblue', 'powderblue', 'deepskyblue', 'lightskyblue', 'steelblue', 'dodgerblue', 'cornflowerblue', 'royalblue', 'mediumblue', 'mediumslateblue')

fig, (ax_madrid, ax_warsaw) = plt.subplots(nrows = 2, ncols = 1, sharex = True, sharey = True)

counter = 0
for lon in range(ds_difference_warsaw.dims.get('longitude')):
    for lat in range(ds_difference_warsaw.dims.get('latitude')):
        ds_difference_warsaw.isel(longitude = lon, latitude = lat)["tx"].plot(ax = ax_warsaw, color = shades_of_blue[counter], alpha = 0.7)
        counter += 1

counter = 0
for lon in range(ds_difference_madrid.dims.get('longitude')):
    for lat in range(ds_difference_madrid.dims.get('latitude')):
        ds_difference_madrid.isel(longitude = lon, latitude = lat)["tx"].plot(ax = ax_madrid, color = shades_of_blue[counter], alpha = 0.7)
        counter += 1

ax_madrid.set_title("Madrid : E-OBS - ERA-5")
ax_madrid.set_ylabel("")
ax_madrid.set_xlabel("")

ax_warsaw.set_title("Warsaw: E-OBS - ERA-5")
ax_warsaw.set_ylabel("")

# add framing axis for common y-label
fig.add_subplot(111, frame_on = False)
plt.tick_params(labelcolor="none", bottom = False, left = False)
plt.ylabel("Difference [degrees Celsius]")

plt.suptitle("Difference in daily maximum temperature")

plt.tight_layout()

plt.savefig("data/difference_time_series.png")
#plt.show()
plt.close()

