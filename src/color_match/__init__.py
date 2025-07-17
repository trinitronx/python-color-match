print(f"{__file__} imported")

# This did not run util_pkg/__init__.py
#from util_pkg import length, lower, upper
# This does run the util_pkg/__init__.py
from .util.color import calculate_delta_e

import sys
from pprint import pprint

loaded_modules = dict([(key, value) for key, value in sys.modules.items() ])
pprint(loaded_modules)
