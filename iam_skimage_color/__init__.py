try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
import sys
sys.path.append('./utils')

import os
from napari_plugin_engine import napari_hook_implementation
from napari.types import ImageData
from magicgui import magicgui, magic_factory
from skimage import color
from inspect import getmembers, isfunction
import napari
import inspect
from utils.utils import *


exposure_function_list = getmembers(color, isfunction)
exposure_function_list = eliminate_functions(exposure_function_list)
# filter only function that return images

magic_exposure_function_list = []
for f in exposure_function_list:
    func = f[1]
    func.__annotations__ = {'image': ImageData,'return': ImageData}    
    func.__name__ = f[0]
    new_func = magic_factory(func)
    magic_exposure_function_list.append(new_func)

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return magic_exposure_function_list

# @napari_hook_implementation
# def napari_experimental_provide_function():
#     # we can return a single function
#     # or a tuple of (function, magicgui_options)
#     # or a list of multiple functions with or without options, as shown here:
#     return magic_exposure_function_list