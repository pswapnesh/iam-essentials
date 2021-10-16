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
from skimage import morphology
from inspect import getmembers, isfunction
import napari
import inspect
from utils.utils import *


function_list = getmembers(morphology, isfunction)
magic_exposure_function_list = prepare_functions(function_list)


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return magic_exposure_function_list

# @napari_hook_implementation
# def napari_experimental_provide_function():
#     # we can return a single function
#     # or a tuple of (function, magicgui_options)
#     # or a list of multiple functions with or without options, as shown here:
#     return magic_exposure_function_list