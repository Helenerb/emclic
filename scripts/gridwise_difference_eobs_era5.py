# Script for formatting and plotting gridwise difference between era-5 and eobs-data

import cartopy.crs as ccrs
import xarray as xr
import matplotlib.pyplot as plt
import cdo
import os

# regrid so that EOBS and ERA-5 are compareable

# Find difference between E-OBS and ERA-5 (subtract one from the other)


# instansiate cdo object
myCdo = cdo.Cdo()

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

print("Begin processing")

#   ----  extract wide area around Madrid for regridding and select apprpriate time frame   ----

# E-OBS

#myCdo.seldate("1990-01-01,2021-06-30", input = eobsPath("tx_ens_mean_0.25deg_reg_v24.0e.nc"), output = eobsPath("temp_eobs1990.nc"))

# select large area
#myCdo.sellonlatbox("-4.90,-2.50,39.25,41.55", input = eobsPath("temp_eobs1990.nc"), output = eobsPath("temp_eobs_largeMadrid.nc"))

#os.system("rm {}".format(eobsPath("temp_eobs1990.nc")))

# ERA-5   --- start with selecting area before selecting time - faster

#myCdo.sellonlatbox("-4.90,-2.50,39.25,41.55", input = era5Path("maxtemp2m_ERA5_1979-2020.nc"), output = era5Path("temp_era5_largeMadrid1979.nc"))

#myCdo.seldate("1990-01-01T11:30:00,2020-05-15T10:30:00", input = era5Path("temp_era5_largeMadrid1979.nc"), output = era5Path("temp_era5_largeMadrid.nc"))

#os.system("rm {}".format(era5Path("temp_era5_largeMadrid1979.nc")))

# change era5 data from Celcius to Kelvin, and change name of variable

#myCdo.setattribute('tx@units="Celcius"', input = '-chname,tasmax,tx -addc,-273.15 {}'.format(era5Path("temp_era5_largeMadrid.nc")), output = era5Path("temp_era5_largeMadridCelsius.nc"))

#os.system("rm {}".format(era5Path("temp_era5_largeMadrid.nc")))

#   ----   Perform regridding  ----

# define new grids:

regrid_eobs = """
gridtype  = lonlat
gridsize  = 323
xsize     = 19
ysize     = 17
xname     = longitude
xlongname = "Longitude values"
xunits    = "degrees_east"
yname     = latitude
ylongname = "Latitude values"
yunits    = "degrees_north"
xfirst    = -4.875
xinc      = 0.125
yfirst    = 39.375
yinc      = 0.125
"""

#with open(eobsPath("regrid_eobs_Madrid.txt"), "wt") as f:
#    f.write(regrid_eobs)

regrid_era5 = """
gridtype  = lonlat
gridsize  = 361
datatype  = float
xsize     = 19
ysize     = 19
xname     = longitude
xlongname = "longitude"
xunits    = "degrees_east"
yname     = latitude
ylongname = "latitude"
yunits    = "degrees_north"
xfirst    = 355.25
xinc      = 0.125
yfirst    = 39.125
yinc      = 0.125
"""
# note: implicitly changes N-S orientation, to S->N

#with open(era5Path("regrid_era5_Madrid.txt"), "wt") as f:
#    f.write(regrid_era5)

#E-OBS
#myCdo.remapbil(eobsPath("regrid_eobs_Madrid.txt"), input = eobsPath("temp_eobs_largeMadrid.nc"), output = eobsPath("temp_regrid_eobs_largeMadrid.nc"))

#myCdo.sellonlatbox("-3.90,-3.50,40.25,40.41", input = eobsPath("temp_regrid_eobs_largeMadrid.nc"), output = eobsPath("regrid_eobs_Madrid.nc"))

#os.system("rm {}".format(eobsPath("temp_regrid_eobs_largeMadrid.nc")))

# ERA-5
#myCdo.remapbil(era5Path("regrid_era5_Madrid.txt"), input = era5Path("temp_era5_largeMadridCelsius.nc"), output = era5Path("temp_regrid_era5_largeMadrid.nc"))

#myCdo.sellonlatbox("-3.90,-3.50,40.25,40.41", input = era5Path("temp_regrid_era5_largeMadrid.nc"), output = era5Path("regrid_era5_Madrid.nc"))

#os.system("rm {}".format(era5Path("temp_regrid_era5_largeMadrid.nc")))

#   ----   Find daily difference   ----

#myCdo.sub(input = "{} {}".format(eobsPath("regrid_eobs_Madrid.nc"), era5Path("regrid_era5_Madrid.nc")), output = "data/difference_era5_eobs_Madrid.nc")

#   ----   For Warsaw   ----

#   ----  extract wide area around Madrid for regridding and select apprpriate time frame   ----

# E-OBS

#myCdo.seldate("1990-01-01,2021-06-30", input = eobsPath("tx_ens_mean_0.25deg_reg_v24.0e.nc"), output = eobsPath("temp_eobs1990.nc"))

# select large area
#myCdo.sellonlatbox("19.8,22.3,51.05,53.4", input = eobsPath("temp_eobs1990.nc"), output = eobsPath("temp_eobs_largeWarsaw.nc"))

#os.system("rm {}".format(eobsPath("temp_eobs1990.nc")))

# ERA-5   --- start with selecting area before selecting time - faster

#myCdo.sellonlatbox("19.8,22.3,51.05,53.4", input = era5Path("maxtemp2m_ERA5_1979-2020.nc"), output = era5Path("temp_era5_largeWarsaw1979.nc"))

#myCdo.seldate("1990-01-01T11:30:00,2020-05-15T10:30:00", input = era5Path("temp_era5_largeWarsaw1979.nc"), output = era5Path("temp_era5_largeWarsaw.nc"))

#os.system("rm {}".format(era5Path("temp_era5_largeWarsaw1979.nc")))

# change era5 data from Celcius to Kelvin, and change name of variable

#myCdo.setattribute('tx@units="Celcius"', input = '-chname,tasmax,tx -addc,-273.15 {}'.format(era5Path("temp_era5_largeWarsaw.nc")), output = era5Path("temp_era5_largeWarsawCelsius.nc"))

#os.system("rm {}".format(era5Path("temp_era5_largeWarsaw.nc")))

#   ----   Perform regridding  ----

# define new grids:

regrid_eobs_warsaw = """
gridtype  = lonlat
gridsize  = 361
xsize     = 19
ysize     = 19
xname     = longitude
xlongname = "Longitude values"
xunits    = "degrees_east"
yname     = latitude
ylongname = "Latitude values"
yunits    = "degrees_north"
xfirst    = 19.875
xinc      = 0.125
yfirst    = 51.125
yinc      = 0.125
"""

with open(eobsPath("regrid_eobs_Warsaw.txt"), "wt") as f:
    f.write(regrid_eobs_warsaw)

regrid_era5_warsaw = """
gridtype  = lonlat
gridsize  = 323
datatype  = float
xsize     = 19
ysize     = 17
xname     = longitude
xlongname = "longitude"
xunits    = "degrees_east"
yname     = latitude
ylongname = "latitude"
yunits    = "degrees_north"
xfirst    = 20
xinc      = 0.125
yfirst    = 51.125
yinc      = 0.125
"""

# note: implicitly changes N-S orientation, to S->N

with open(era5Path("regrid_era5_Warsaw.txt"), "wt") as f:
    f.write(regrid_era5_warsaw)

#E-OBS
myCdo.remapbil(eobsPath("regrid_eobs_Warsaw.txt"), input = eobsPath("temp_eobs_largeWarsaw.nc"), output = eobsPath("temp_regrid_eobs_largeWarsaw.nc"))

myCdo.sellonlatbox("20.8,21.3,52.05,52.4", input = eobsPath("temp_regrid_eobs_largeWarsaw.nc"), output = eobsPath("regrid_eobs_Warsaw.nc"))

os.system("rm {}".format(eobsPath("temp_regrid_eobs_largeWarsaw.nc")))

# ERA-5
myCdo.remapbil(era5Path("regrid_era5_Warsaw.txt"), input = era5Path("temp_era5_largeWarsawCelsius.nc"), output = era5Path("temp_regrid_era5_largeWarsaw.nc"))

myCdo.sellonlatbox("20.8,21.3,52.05,52.4", input = era5Path("temp_regrid_era5_largeWarsaw.nc"), output = era5Path("regrid_era5_Warsaw.nc"))

os.system("rm {}".format(era5Path("temp_regrid_era5_largeWarsaw.nc")))

#   ----   Find daily difference   ----

myCdo.sub(input = "{} {}".format(eobsPath("regrid_eobs_Warsaw.nc"), era5Path("regrid_era5_Warsaw.nc")), output = "data/difference_era5_eobs_Warsaw.nc")

print("End Processing")

# Next: climatologies!


