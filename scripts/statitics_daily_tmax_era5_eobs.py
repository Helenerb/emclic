# Script for finding R-squared and R-MDSS of daily maximum temperature data from Era-5 and E-obs

# Note: Here, we use the regridded 0.25 deg data, for values where

import cdo
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import scipy as sc
from sklearn.linear_model import LinearRegression

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

myCdo = cdo.Cdo()

ds_tx_madrid_era5 = xr.open_dataset(era5Path("regrid_era5_Madrid.nc"))
ds_tx_madrid_eobs = xr.open_dataset(eobsPath("regrid_eobs_Madrid.nc"))

# transform so that the two datasets are mergeable
ds_tx_madrid_era5 = ds_tx_madrid_era5.sel(time = slice("1990-01-01", "2020-05-15"))
ds_tx_madrid_era5 = ds_tx_madrid_era5.assign_coords(longitude = (((ds_tx_madrid_era5.longitude + 180) % 360) - 180))

print("\n Before resample", ds_tx_madrid_era5["tx"])

ds_tx_madrid_era5 = ds_tx_madrid_era5.resample(time = "1D").first()
#ds_tx_madrid_era5["time"] = pd.to_datetime(ds_tx_madrid_era5["time"]).date()
ds_tx_madrid_era5 = ds_tx_madrid_era5.rename({"tx" : "tx_era5"})

print("\n after resample: ", ds_tx_madrid_era5["tx_era5"], "\n")

ds_tx_madrid_eobs = ds_tx_madrid_eobs.sel(time = slice("1990-01-01", "2020-05-15"))
ds_tx_madrid_eobs = ds_tx_madrid_eobs.rename({"tx" : "tx_eobs"})

# merge datasets
ds_tx_madrid = xr.merge([ds_tx_madrid_era5, ds_tx_madrid_eobs])

#   ---   Calculate r-squared   ----

# create dataframe for simple data handling
df_tx_madrid = ds_tx_madrid.to_dataframe()

# using numpy corrcoeff
correlation_matrix = np.corrcoef(df_tx_madrid["tx_eobs"], df_tx_madrid["tx_era5"])
r_value= correlation_matrix[0,1]  # understand - why not 0,0??
r_squared = r_value**2

print("\n R-squared using numpy : ", r_squared)

# using arithmetics, finding necessary values
#df_tx_madrid["tx_eobs_2"] = df_tx_madrid["tx_eobs"]**2
#df_tx_madrid["tx_era5_2"] = df_tx_madrid["tx_era5"]**2
#df_tx_madrid["tx_eobs_era5"] = df_tx_madrid["tx_eobs"]*df_tx_madrid["tx_era5"]

#r_arithmetic = (df_tx_madrid["tx_eobs_era5"].mean() - df_tx_madrid["tx_eobs"].mean()*df_tx_madrid["tx_era5"].mean())/(np.sqrt((df_tx_madrid["tx_eobs_2"].mean() - df_tx_madrid["tx_eobs"].mean()**2)*(df_tx_madrid["tx_era5_2"].mean() - df_tx_madrid["tx_era5"].mean()**2)))

#print("Artihmetic r squared: ", r_arithmetic**2)

#   ----   Calculate rmse   ----
r_mse = np.sqrt(((df_tx_madrid["tx_eobs"] - df_tx_madrid["tx_era5"])**2).mean())
print("\n R-MSE: ", r_mse)

#   ----   Linear Regression   ----

# TODO: Try scikitlearn instead!
#regression = sc.stats.linregress(x = df_tx_madrid["tx_eobs"], y = df_tx_madrid["tx_era5"])
model = LinearRegression()

# prepare x-values and y-values for regression
x_reg = df_tx_madrid["tx_eobs"].to_numpy().reshape((-1, 1))  # transform to column vector
y_reg = df_tx_madrid["tx_era5"].to_numpy()

model.fit(x_reg, y_reg)

print("intercept: ", model.intercept_)
print("\n slope: ", model.coef_)

# find r-squared using sklearn:
rsq_sklearn = model.score(x_reg, y_reg)
print("\n R^2 sklearn: ", rsq_sklearn)

fig, ax = plt.subplots(nrows = 1, ncols = 1)

ds_tx_madrid.plot.scatter(x = "tx_eobs", y = "tx_era5", ax = ax, marker = ".", alpha = 0.4, color = "deepskyblue", label = "(E-OBS, ERA-5)")
ax.axline(xy1=[0,0], xy2=[40,40], color = "tomato", alpha = 0.7, linestyle = "dashed", label = "y = x")

# add regression line:
x_vals = np.array(ax.get_xlim())  # axis limits
y_vals = model.intercept_ + model.coef_ * x_vals  # corresponding line
ax.plot(x_vals, y_vals, linestyle = "dashed", color = "gold", label = "Linear regression")  # plot regression line

ax.text(x=34, y=6, s = "R^2: {:.2f}".format(r_squared))
ax.text(x=34, y=3, s = "R-MSE: {:.2f}".format(r_mse))

ax.set_xlabel("EOBS [Degrees Celsius]")
ax.set_ylabel("ERA-5 [Degrees Celsius]")

plt.suptitle("Daily Maximum Temperature, 1990-2020")
plt.legend()

plt.show()
plt.savefig("data/statistics_era5_eobs.png")
plt.close()

# Combine era-5 and e-obs data, for Warsaw and Madrid

# Plot data together with y = x line, to get a visual representation of data fit

# Calculate statistics for fit

