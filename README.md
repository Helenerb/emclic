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
Most useful code is located in the notebooks, in the `emclic` package. The `scripts` package mostly contains the raw files that the notebooks are based on. 
The notebooks are:
- *climatologies_eobs_era5.ipynb*: calculates climatologies from already regridded E-OBS and ERA-5 data.
- *gridwise_difference_eobs_ers5.ipynb*: performs regridding of E-OBS and ERA5 data so that they are comparable for Warsaw and Madrid
- *plot_climatologies_eobs_era5.ipynb*: produces plots of climatologies, only does minor data formatting to ready the data for plotting
- *plot_comparison_eobs_era5.ipynb*: plots comparisons of the E-OBS and ERA-5 data, based on the regridded data sets
- *statistics_daily_tmax_era5_eobs.ipynb*: calculates R-squared and RMSE statistics for two data sets (regridded E-OBS and ERA-5 for Warsaw and Madrid)
- *time_series_eobs_era5.ipynb*: simple extraction and plotting of time series data for Warsaw and Madrid, E-OBS and ERA-5 data
- *time_series_hadISD.ipynb*: simple data formatting (using `xarray`, not `cdo`) and plotting of HadIDS weather station data for Warsaw and Madrid. 



