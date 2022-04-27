# emclic
Plotting and dataformatting related to emclic project

## Accessing and running the code from server
Load the following modules and environments:  
- module load Anaconda3/2020.11
- source activate /div/qbo/users/py3Env/venvPy3

### Launch your own Jupyter notebook instance:
(From https://docs.anaconda.com/anaconda/user-guide/tasks/remote-jupyter-notebook/)
- At server, type:  
```
# Replace <PORT> with your selected port number
jupyter notebook --no-browser --port=<PORT>
```
- The proces will output a link with an access token, copy this.   
- Launch local terminal, e.g. windows PowerShell, and type the following  
```
# Replace <PORT> with the port number you selected in the above step
# Replace <REMOTE_USER> with the remote server username
# Replace <REMOTE_HOST> with your remote server address
ssh -L 8080:localhost:<PORT> <REMOTE_USER>@<REMOTE_HOST>
```
- Enter password to server
- Paste the link previously copied into local browser

Other useful commands for handling notebook servers: 

Checking if any notebook servers are already runnning
```
$ jupyter notebook list
```
Killing (shutting down) notebook servers that are no longer needed
```
$ jupyter notebook stop <PORT>
```

## Contents
Most useful code is located in the notebooks, in the `emclic` package.  
The notebooks are:
- *climatologies_eobs_era5.ipynb*: calculates climatologies from already regridded E-OBS and ERA-5 data.
- *gridwise_difference_eobs_ers5.ipynb*: performs regridding of E-OBS and ERA5 data so that they are comparable for Warsaw and Madrid
- *plot_climatologies_eobs_era5.ipynb*: produces plots of climatologies, only does minor data formatting to ready the data for plotting
- *plot_comparison_eobs_era5.ipynb*: plots comparisons of the E-OBS and ERA-5 data, based on the regridded data sets
- *statistics_daily_tmax_era5_eobs.ipynb*: calculates R-squared and RMSE statistics for two data sets (regridded E-OBS and ERA-5 for Warsaw and Madrid)
- *time_series_eobs_era5.ipynb*: simple extraction and plotting of time series data for Warsaw and Madrid, E-OBS and ERA-5 data
- *time_series_hadISD.ipynb*: simple data formatting (using `xarray`, not `cdo`) and plotting of HadIDS weather station data for Warsaw and Madrid. 

The `scripts` package mostly contains the raw files that the notebooks are based on, as well as the file `local_paths.py` which contain some helper files for local paths. 

The `data` package mainly contains formatted and raw data, but also some scripts for downloading, as well as some slight formatting, of the raw data:
- *E-OBS/download_eobs.py*: Simple script for accessing the Copernicus data store API and download data from it
- *HadCRUT5/download_hadCRUT5.py*: Simple script for downloading HadCRUT5 data from an url and writing the content to a file
- *HadISD/download_hadISD.py*: Script for downloading data on station data measurements of meteorological data (temperature, dewpoint, windspeed, wind direction, station and sea level pressure), as well as calculated quantities (vapor pressure, saturation vapor pressure, relative humidity, specific humidity, apparent temperature), for weather stations in Warsaw and Madrid
- *HadISD*: Example file containing simple date range selection of one HadISD station data netcdf file. 
- *netatmo/download_Netatmo.py*: Example script of downloading netatmo station data from Madrid. Note that this script assumes that a netatmo access token has already been obtained. Note that the call in this example only provides the last available measurement point, not the full time series. 
- *netatmo/download_Netatmo_timeseries*: contains the example script for downloading time series data for one specific netatmo station. Note that this requires knowledge on the desired netatmo device and module id. 
-  *netatmo/get_access_token_Netatmo.py*: this script contains so far unsuccessful attempts at fetching the access token from netatmo. I include it here for reference or a starting point only, and recommend following my netatmo-download instruction on how to get the access token using postman. 

