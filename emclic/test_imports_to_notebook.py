# We will here test if imports work

import matplotlib.pyplot as plt

print("successfully import matplotlib")

#from ..test_emclic_import import hello_emclic
import test_emclic_import as emc

emc.hello_emclic()

#from ..scripts.test_scripts_import import hello_scripts
import scripts.test_scripts_imports as scr

scr.hello_scripts()
