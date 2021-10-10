try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

import os
from napari_plugin_engine import napari_hook_implementation
from napari.types import ImageData
from magicgui import magicgui, magic_factory
from skimage import exposure
from inspect import getmembers, isfunction
import napari
import inspect

def is_ndarray_output(f):
    '''
    A bad hack to get if the scikit-image function
    returns an image.
    '''
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

# Handle none type image later
# def noneTypeHandler(func):
#     def wrapper(image: ImageData):
#         if image is not None:
#             return func        
#         else:
#             return (lambda x: x)
#     #wrapper.__annotations__ = {'image': ImageData,'return': ImageData}
#     return wrapper


exposure_function_list = getmembers(exposure, isfunction)
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