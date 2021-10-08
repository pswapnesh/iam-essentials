from skimage import filters
from skimage import exposure
from inspect import getmembers, isfunction #, getsource,getfullargspec,signature,Parameter
#from magicgui import magic_factory
#from magicgui import magicgui
#import napari
import numpy as np
#from napari.layers import Image
from napari.types import ImageData
from functools import partial
from typing import overload


exposure_function_list = getmembers(exposure, isfunction)
new_functions = []
for f in exposure_function_list:
    f[1].__annotations__ = {'image': ImageData,'return': ImageData}
    new_functions.append(magicgui(f[1]))


viewer = napari.Viewer()
#viewer = napari.view_image(np.random.rand(64, 64), name="My Image")
viewer.window.add_dock_widget(new_functions, area='right')

