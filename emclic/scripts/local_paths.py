# Local paths, used mainly in retrieving and storing data

import os

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

def hadisd_path(filename):
    """Returns the filepath to storage for HadISD weather station data 
    
    Parameters
    ----------
    filename: string
        the name that should be given to the data

    Returns
    -------
    string
        the full file path to the HasISD data file
    """
    return os.path.join("data/HadISD", filename)
