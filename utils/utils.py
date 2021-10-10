import inspect
from magicgui import magic_factory
from napari.types import ImageData

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


def prepare_functions(func_list):
    '''

    1. remove functions starting with "_"
    2. remove functions with no arguments named 'image' or 'rgb'
    3. if it's 'image' or 'rgb' then change function annotations accordingly
    4. some arguments take tuple or float. hard code them to float : easy but will lead to errors
    5. should be a better way to do this : check in later
    '''
    image_words = ['image','rgb']
    parameter_words_float = ['sigma','scale']
    new_list = []
    for f in func_list:
        fullspec = inspect.getfullargspec(f[1])
        flag = False
        for s in image_words:
            if s in fullspec.args:
                flag = True        
        if (f[0][0] != "_") & (is_ndarray_output(f)) & (flag):
            annotations = {fullspec.args[0]: ImageData}
            for p in  parameter_words_float:
                if p in fullspec.args:
                    annotations[p] = float
            annotations['return'] = ImageData
            f[1].__annotations__ = annotations   
            f[1].__name__ = f[0]
            new_func = magic_factory(f[1])
            new_list.append(new_func)
    return new_list
