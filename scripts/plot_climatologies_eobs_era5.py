# script for plotting of climatologies, and related data, for era-5 and eobs data of Madrid and Warsaw

import os
import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cartopy.crs as ccrs
import calendar

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


# plot climatologies as time series

# blue colors, global variable
shades_of_blue = ('aquamarine', 'turquoise', 'lightseagreen', 'teal', 'cadetblue', 'powderblue', 'deepskyblue', 'lightskyblue', 'steelblue', 'dodgerblue', 'cornflowerblue', 'royalblue', 'mediumblue', 'mediumslateblue')

def plotMontlyAverage():
    """Plots data of montly average of the daily maximum temperature, for E-OBS and ERA-5 data, for Madrid and Warsaw

    """

    # load data
    ds_monavg_eobs_madrid = xr.open_dataset(eobsPath("monavg_regrid_eobs_Madrid.nc"))
    ds_monavg_era5_madrid = xr.open_dataset(era5Path("monavg_regrid_era5_Madrid.nc"))
    ds_monavg_eobs_warsaw = xr.open_dataset(eobsPath("monavg_regrid_eobs_Warsaw.nc"))
    ds_monavg_era5_warsaw = xr.open_dataset(era5Path("monavg_regrid_era5_Warsaw.nc"))

    fig, (ax_madrid, ax_warsaw) = plt.subplots(nrows = 2, ncols = 1, sharex = True, figsize = (7,5))

    for lon in range(ds_monavg_eobs_madrid.dims.get('longitude')):
        for lat in range(ds_monavg_eobs_madrid.dims.get('latitude')):
            ds_monavg_eobs_madrid.isel(longitude = lon, latitude = lat)["tx"].plot(ax = ax_madrid, color = shades_of_blue[0], alpha = 0.7, label = ("E-OBS" if lon == 0 and lat == 0 else "_nolegend_"))
            ds_monavg_era5_madrid.isel(longitude = lon, latitude = lat)["tx"].plot(ax= ax_madrid, color = shades_of_blue[4], alpha = 0.7, label = ("ERA-5" if lon == 0 and lat == 0 else "_nolegend_"))


    for lon in range(ds_monavg_eobs_warsaw.dims.get('longitude')):
        for lat in range(ds_monavg_eobs_warsaw.dims.get('latitude')):
            ds_monavg_eobs_warsaw.isel(longitude = lon, latitude = lat)["tx"].plot(ax = ax_warsaw, color = shades_of_blue[0], alpha = 0.7, label = ("E-OBS" if lon == 0 and lat == 0 else "_nolegend_"))
            ds_monavg_era5_warsaw.isel(longitude = lon, latitude = lat)["tx"].plot(ax = ax_warsaw, color = shades_of_blue[4], alpha = 0.7, label = ("ERA-5" if lon == 0 and lat == 0 else "_nolegend_"))

    ax_madrid.set_title("Madrid")
    ax_madrid.set_ylabel("")
    ax_madrid.set_xlabel("")
    ax_madrid.legend()

    ax_warsaw.set_title("Warsaw")
    ax_warsaw.set_ylabel("")
    ax_warsaw.legend()

    # add framing axis for common y-label
    fig.add_subplot(111, frame_on = False)
    plt.tick_params(labelcolor="none", bottom = False, left = False)
    plt.ylabel("Degrees Celsius")

    plt.suptitle("Monthly average daily maximal temperature, E-OBS and ERA-5")

    plt.savefig("data/monavg_era5_eobs.png")
    plt.show()
    plt.close()

# Plot daily deviation from monthly average

def plotDailyAnomalies():
    """Plots daily anomalies from montly average of maximum daily temperature, for E-OBS and ERA-5 data, for Warsaw and Madrid

    """
    # load data
    ds_anomalies_eobs_madrid = xr.open_dataset(eobsPath("anomalies_mon_regrid_eobs_Madrid.nc"))
    ds_anomalies_era5_madrid = xr.open_dataset(era5Path("anomalies_mon_regrid_era5_Madrid.nc"))
    ds_anomalies_eobs_warsaw = xr.open_dataset(eobsPath("anomalies_mon_regrid_eobs_Warsaw.nc"))
    ds_anomalies_era5_warsaw = xr.open_dataset(era5Path("anomalies_mon_regrid_era5_Warsaw.nc"))

    fig, (ax_madrid, ax_warsaw) = plt.subplots(nrows = 2, ncols = 1, sharex = True, figsize = (7,5))

    for lon in range(ds_anomalies_eobs_madrid.dims.get('longitude')):
        for lat in range(ds_anomalies_eobs_madrid.dims.get('latitude')):
            ds_anomalies_eobs_madrid.isel(longitude = lon, latitude = lat)["tx"].plot(ax = ax_madrid, color = shades_of_blue[0], alpha = 0.7, label = ("E-OBS" if lon == 0 and lat == 0 else "_nolegend_"))
            ds_anomalies_era5_madrid.isel(longitude = lon, latitude = lat)["tx"].plot(ax= ax_madrid, color = shades_of_blue[4], alpha = 0.7, label = ("ERA-5" if lon == 0 and lat == 0 else "_nolegend_"))

    for lon in range(ds_anomalies_eobs_warsaw.dims.get('longitude')):
        for lat in range(ds_anomalies_eobs_warsaw.dims.get('latitude')):
            ds_anomalies_eobs_warsaw.isel(longitude = lon, latitude = lat)["tx"].plot(ax = ax_warsaw, color = shades_of_blue[0], alpha = 0.7, label = ("E-OBS" if lon == 0 and lat == 0 else "_nolegend_"))
            ds_anomalies_era5_warsaw.isel(longitude = lon, latitude = lat)["tx"].plot(ax = ax_warsaw, color = shades_of_blue[4], alpha = 0.7, label = ("ERA-5" if lon == 0 and lat == 0 else "_nolegend_"))

    ax_madrid.set_title("Madrid")
    ax_madrid.set_ylabel("")
    ax_madrid.set_xlabel("")
    ax_madrid.legend()

    ax_warsaw.set_title("Warsaw")
    ax_warsaw.set_ylabel("")
    ax_warsaw.legend()

    # add framing axis for common y-label
    fig.add_subplot(111, frame_on = False)
    plt.tick_params(labelcolor="none", bottom = False, left = False)
    plt.ylabel("Degrees Celsius")

    plt.suptitle("Daily anomalies from montly average of maximum temperature, E-OBS and ERA-5")

    plt.savefig("data/anomalies_era5_eobs.png")
    plt.show()
    plt.close()

def plotMonavgDifference():
    """Plots the difference in monthly averages between E-OBS and Era-5 data, for Warsaw and Madrid

    """
    # load data
    ds_monavg_difference_madrid = xr.open_dataset("data/monavg_difference_eobs_era5_Madrid.nc")
    ds_monavg_difference_warsaw = xr.open_dataset("data/monavg_difference_eobs_era5_Warsaw.nc")

    # slice for dates where you have observations for both sets of data
    ds_monavg_difference_madrid = ds_monavg_difference_madrid.sel(time = slice("1990-01-01", "2020-05-15"))
    ds_monavg_difference_warsaw = ds_monavg_difference_warsaw.sel(time = slice("1990-01-01", "2020-05-15"))

    
    fig, (ax_madrid, ax_warsaw) = plt.subplots(nrows = 2, ncols = 1, sharex = True, figsize = (7,5))

    for lon in range(ds_monavg_difference_madrid.dims.get('longitude')):
        for lat in range(ds_monavg_difference_madrid.dims.get('latitude')):
            ds_monavg_difference_madrid.isel(longitude = lon, latitude = lat)["tx"].plot(ax = ax_madrid, color = shades_of_blue[4], alpha = 0.7)

    for lon in range(ds_monavg_difference_warsaw.dims.get('longitude')):
        for lat in range(ds_monavg_difference_warsaw.dims.get('latitude')):
            ds_monavg_difference_warsaw.isel(longitude = lon, latitude = lat)["tx"].plot(ax = ax_warsaw, color = shades_of_blue[4], alpha = 0.7)

    # add horizontal line at zero difference:
    ax_madrid.axhline(y=0.0, color = "tomato", alpha = 0.7)
    ax_warsaw.axhline(y=0.0, color = "tomato", alpha = 0.7)

    ax_madrid.set_title("Madrid")
    ax_madrid.set_ylabel("")
    ax_madrid.set_xlabel("")

    ax_warsaw.set_title("Warsaw")
    ax_warsaw.set_ylabel("")

    # add framing axis for common y-label
    fig.add_subplot(111, frame_on = False)
    plt.tick_params(labelcolor="none", bottom = False, left = False)
    plt.ylabel("Degrees Celsius")

    plt.suptitle("Difference montly average of daily maximal temperature, E-OBS and ERA-5")

    plt.savefig("data/difference_monavg_eobs_era5.png")
    plt.show()
    plt.close()

def plotMonavgDifferenceGridwise():
    """Plots the difference in montly averaged daily maximum temperature between E-OBS and ERA-5 data

    Produces one figure for each year, which contains gridwise plots of the difference each month of that year
    """

     # load data
    ds_monavg_difference_madrid = xr.open_dataset("data/monavg_difference_eobs_era5_Madrid.nc")
    ds_monavg_difference_warsaw = xr.open_dataset("data/monavg_difference_eobs_era5_Warsaw.nc")

    # slice for dates where you have observations for both sets of data
    ds_monavg_difference_madrid = ds_monavg_difference_madrid.sel(time = slice("1990-01-01", "2020-05-15"))
    ds_monavg_difference_warsaw = ds_monavg_difference_warsaw.sel(time = slice("1990-01-01", "2020-05-15"))

    years = [str(year) for year in range(1990,2020)]
    #years = ['1990']

    for year in years:
        # Madrid
        fig, axes = plt.subplots(nrows=3, ncols = 4, subplot_kw = {"projection" : ccrs.PlateCarree()}, figsize = (12,6))
        ds_one_year_madrid = ds_monavg_difference_madrid.sel(time = year)

        for i, ax in enumerate(axes.flat):
            one_month = ds_one_year_madrid.isel(time = i)["tx"].plot(ax = ax, transform = ccrs.PlateCarree(), add_colorbar = False, cmap = "BrBG", vmin = -1, vmax = 2)
            ax.set_title(calendar.month_name[i+1])
            

        fig.colorbar(one_month, ax = axes[:,:], location = "right", label = "Degrees Celsius")
        fig.suptitle("Madrid {} - Difference in montly average daily Tmax, E-OBS and ERA-5 data".format(year))

        plt.savefig("data/monavg_difference_gridwise/{}_madrid.png".format(year))
        #plt.show()
        plt.close()

        # Warsaw
        fig, axes = plt.subplots(nrows=3, ncols = 4, subplot_kw = {"projection" : ccrs.PlateCarree()}, figsize = (12,7.5))
        ds_one_year_warsaw = ds_monavg_difference_warsaw.sel(time = year)

        for i, ax in enumerate(axes.flat):
            one_month = ds_one_year_warsaw.isel(time = i)["tx"].plot(ax = ax, transform = ccrs.PlateCarree(), add_colorbar = False, cmap = "BrBG", vmin = -1, vmax = 2)
            ax.set_title(calendar.month_name[i+1])
            

        fig.colorbar(one_month, ax = axes[:,:], location = "right", label = "Degrees Celsius")
        fig.suptitle(" Warsaw {} - Difference in montly average daily Tmax, E-OBS and ERA-5 data".format(year))

        plt.savefig("data/monavg_difference_gridwise/{}_warsaw.png".format(year))
        #plt.show()
        plt.close()
       


if __name__=="__main__":
    #plotMontlyAverage()
    #plotDailyAnomalies()
    #plotMonavgDifference()
    plotMonavgDifferenceGridwise()
