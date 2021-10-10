try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

import os
from napari_plugin_engine import napari_hook_implementation
from napari.types import ImageData
import numpy as np
from magicgui import magicgui
from skimage import filters
from skimage import exposure
from inspect import getmembers, isfunction
import napari

def noneTypeHandler(func):
    def wrapper(image: ImageData):
        if image not None:
            return func
    return wrapper
    
exposure_function_list = getmembers(exposure, isfunction)
magic_functions = []
for f in exposure_function_list:
    func = f[1]
    func.__annotations__ = {'image': ImageData,'return': ImageData}    
    new_func = magicgui(auto_call=False)(noneTypeHandler(func))
    new_func.__name__ = f[0]
    magic_functions.append(new_func)

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return magic_functions

