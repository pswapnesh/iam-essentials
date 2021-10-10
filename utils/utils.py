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

def contains_image_as_arg(f):    
    fullspec = inspect.getfullargspec(f[1])
    flag = False
    #if fullspec.args[0] == 'image':
    if 'image' in fullspec.args:
        flag = True
    return flag



def eliminate_functions(func_list):
    # remove functions starting with "_"
    new_list = []
    for f in func_list:
        if (f[0][0] != "_") & (is_ndarray_output(f)) & (contains_image_as_arg(f)): #(f[0][0] != "_") & 
            new_list.append(f)
    return new_list
