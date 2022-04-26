# Testing downloading E-OBS (from Copernicus)

import cdsapi

c = cdsapi.Client()

c.retrieve(
    'insitu-gridded-observations-europe',
    {
        'format': 'zip',
        'product_type': 'ensemble_mean',
        'variable': [
            'maximum_temperature', 'mean_temperature', 'minimum_temperature',
            'relative_humidity', 'wind_speed',
        ],
        'grid_resolution': '0.25deg',
        'period': 'full_period',
        'version': '24.0e',
    },
    'test_download.zip')

