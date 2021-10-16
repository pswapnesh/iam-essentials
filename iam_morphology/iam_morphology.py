import  skimage.morphology as morph
import numpy as np
from napari.types import ImageData, LabelsData
import scipy.ndimage as ndi
'''
dilation erosion etc.
dilation without touching 
remove smalle holes 
remove small objects
remove objects with contraints

'''


def binary_dilation(binary: LabelsData, disk_size :int = 1) -> LabelsData:
    return morph.binary_dilation(binary,morph.disk(disk_size))

def binary_erosion(binary: LabelsData, disk_size: int = 1)-> LabelsData:
    return morph.binary_erosion(binary,morph.disk(disk_size))    

def binary_closing(binary: LabelsData, disk_size: int = 1)-> LabelsData:
    return morph.binary_closing(binary,morph.disk(disk_size))    

def binary_opening(binary: LabelsData, disk_size:int = 1)-> LabelsData:
    return morph.binary_opening(binary,morph.disk(disk_size))    

def distance_transform(binary: LabelsData)-> LabelsData:
    return ndi.distance_transform_edt(binary)

