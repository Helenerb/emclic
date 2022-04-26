# Calculate climatologies for e-obs data for era-5 data, for Warsaw and Madrid

import cdo
import os

# instantiate cdo-object
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

print("Begin formatting")

# climatology, monthly average using monavg:

# Era-5, Madrid
#myCdo.monavg(input = era5Path("regrid_era5_Madrid.nc"), output = era5Path("monavg_regrid_era5_Madrid.nc"))

# Era-5, Warsaw
#myCdo.monavg(input = era5Path("regrid_era5_Warsaw.nc"), output = era5Path("monavg_regrid_era5_Warsaw.nc"))

# E-obs, Madrid
#myCdo.monavg(input = eobsPath("regrid_eobs_Madrid.nc"), output = eobsPath("monavg_regrid_eobs_Madrid.nc"))

# E-obs, Warsaw
#myCdo.monavg(input = eobsPath("regrid_eobs_Warsaw.nc"), output = eobsPath("monavg_regrid_eobs_Warsaw.nc"))

# anomalies from montly averages

# Era-5, Madrid
#myCdo.monsub(input = "{} {}".format(era5Path("regrid_era5_Madrid.nc"), era5Path("monavg_regrid_era5_Madrid.nc")), output = era5Path("anomalies_mon_regrid_era5_Madrid.nc"))

# Era-5, Warsaw
#myCdo.monsub(input = "{} {}".format(era5Path("regrid_era5_Warsaw.nc"), era5Path("monavg_regrid_era5_Warsaw.nc")), output = era5Path("anomalies_mon_regrid_era5_Warsaw.nc"))

# Eobs, Madrid
#myCdo.monsub(input = "{} {}".format(eobsPath("regrid_eobs_Madrid.nc"), eobsPath("monavg_regrid_eobs_Madrid.nc")), output = eobsPath("anomalies_mon_regrid_eobs_Madrid.nc"))

# Eobs, Warsaw
#myCdo.monsub(input = "{} {}".format(eobsPath("regrid_eobs_Warsaw.nc"), eobsPath("monavg_regrid_eobs_Warsaw.nc")), output = eobsPath("anomalies_mon_regrid_eobs_Warsaw.nc"))

# differences in monthly averages

# Madrid
#myCdo.sub(input = "{} {}".format(eobsPath("monavg_regrid_eobs_Madrid.nc"), era5Path("monavg_regrid_era5_Madrid.nc")), output = "data/monavg_difference_eobs_era5_Madrid.nc")

# Warsaw
#myCdo.sub(input = "{} {}".format(eobsPath("monavg_regrid_eobs_Warsaw.nc"), era5Path("monavg_regrid_era5_Warsaw.nc")), output = "data/monavg_difference_eobs_era5_Warsaw.nc")


print("End formatting")

