try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

import os
from napari_plugin_engine import napari_hook_implementation
from napari.types import ImageData
import numpy as np
import napari

from magicgui import magicgui
from skimage import filters
from skimage import exposure
from inspect import getmembers, isfunction
import napari
exposure_function_list = getmembers(exposure, isfunction)
magic_functions = []
for f in exposure_function_list:
    f[1].__annotations__ = {'image': ImageData,'return': ImageData}
    magic_functions.append(magicgui(f[1]))

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return magic_functions

