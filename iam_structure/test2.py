import inspect
from magicgui import magic_factory
from napari.types import ImageData

def prepare_functions(func_list):   
    new_list = []
    for f in func_list:                
        if f[0][0] == '_':
            continue
        fullspec = inspect.getfullargspec(f[1])
        print(fullspec.annotations)
        new_func = magic_factory(f[1])
        new_list.append(new_func)
    return new_list

from napari_plugin_engine import napari_hook_implementation
from inspect import getmembers, isfunction
import inspect
#from utils.utils import *
#from iam_structure 
import iam_structure


function_list = getmembers(iam_structure, isfunction)
magic_function_list = prepare_functions(function_list)
