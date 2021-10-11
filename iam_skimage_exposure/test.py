try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
import sys
sys.path.append('./utils')

import os
from napari_plugin_engine import napari_hook_implementation
from napari.types import ImageData
import numpy as np
from magicgui import magicgui, magic_factory
from skimage import filters
from skimage import transform
from inspect import getmembers, isfunction
import napari
import inspect
from utils.utils import *


# def is_ndarray_output(f):
#     search_string = ['ndarray' ,'2-D array']
#     return_string = "Returns"
#     doc = inspect.getdoc(f[1])
#     idx = doc.find(return_string)
#     doc = doc[idx + len(return_string):]
#     idx = doc.find(':')
#     doc = doc[idx + 1 :]
#     idx = doc.find('--')
#     doc = doc[:idx]
#     flag = False
#     for ss in search_string:
#         if ss in doc:
#             flag = True
#     return flag

# def eliminate_functions(func_list):
#     # remove functions starting with "_"
#     new_list = []
#     for f in func_list:
#         if (f[0][0] != '_' ) & (is_ndarray_output(f)):
#             new_list.append(f)
#     return new_list

exposure_function_list = getmembers(transform, isfunction)
#exposure_function_list = eliminate_functions(exposure_function_list)

# remove function whose output is not image    


#print(args,'image' in args)
# filter only function that return images
for f in exposure_function_list:
    #args = inspect.getfullargspec(f[1])
    args = inspect.signature(f[1])
    required_params = []
    sig = str(args)[1:-2]
    sig = sig.split(',')
    for a in sig:
        if "=" in a:
            continue
        else:
            required_params.append(a.replace(' ',''))
    print(f[0]," ",sig,required_params,"\n****\n")
