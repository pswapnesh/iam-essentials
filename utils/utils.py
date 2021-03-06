import inspect
from magicgui import magic_factory
from napari.types import ImageData

def prepare_functions(func_list):   
    new_list = []
    for f in func_list:                
        if f[0][0] == '_':
            continue
        if f[0][:4] != 'iam_':
            continue
        fullspec = inspect.getfullargspec(f[1])
        f[1].__name__ = f[0][4:]
        new_func = magic_factory(f[1])
        new_list.append(new_func)
    return new_list

def is_stack(image):
    if len(image.shape) > 2:
        return True
    elif len(image.shape) == 2:
        return  False
    return 0