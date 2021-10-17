
import sys
sys.path.append('./utils')

from napari_plugin_engine import napari_hook_implementation
from inspect import getmembers, isfunction
import inspect
from utils.utils import *
from iam_segmentation import iam_segmentation


function_list = getmembers(iam_segmentation, isfunction)
magic_function_list = prepare_functions(function_list)

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return magic_function_list