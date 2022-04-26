# Script for cleaning hadISD data

# import cdo library
import cdo

# instantiate cdo object
myCdo = cdo.Cdo()

print("Starting selection process")
myCdo.selyear("1990,2022", input = "madrid_082210.nc", output = "madrid_082210_recent.nc")

print("Selecton process finished")


# Cdo commands:
# cdo -selvar,temperature -ltc, 1.99*10**30 infile maskfile
# cdo ifthen infile maskfile outfile
# delete maskfile
