try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

import os
from napari_plugin_engine import napari_hook_implementation
from napari.types import ImageData
import numpy as np
from magicgui import magicgui, magic_factory
from skimage import filters
from skimage import exposure
from inspect import getmembers, isfunction
import napari
import inspect

def is_ndarray_output(f):
    search_string = ['ndarray' ,'2-D array']
    return_string = "Returns"
    doc = inspect.getdoc(f[1])
    idx = doc.find(return_string)
    doc = doc[idx + len(return_string):]
    idx = doc.find(':')
    doc = doc[idx + 1 :]
    idx = doc.find('--')
    doc = doc[:idx]
    flag = False
    for ss in search_string:
        if ss in doc:
            flag = True
    return flag

def eliminate_functions(func_list):
    # remove functions starting with "_"
    new_list = []
    for f in func_list:
        if (f[0][0] != '_' ) & (is_ndarray_output(f)):
            new_list.append(f)
    return new_list

exposure_function_list = getmembers(filters, isfunction)
exposure_function_list = eliminate_functions(exposure_function_list)

# remove function whose output is not image    

# filter only function that return images
for f in exposure_function_list:
    print(f[0],is_ndarray_output(f))
