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

# Handle none type image later
# def noneTypeHandler(func):
#     def wrapper(image: ImageData):
#         if image is not None:
#             return func        
#         else:
#             return (lambda x: x)
#     #wrapper.__annotations__ = {'image': ImageData,'return': ImageData}
#     return wrapper


exposure_function_list = getmembers(filters, isfunction)
exposure_function_list += getmembers(exposure, isfunction)
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

