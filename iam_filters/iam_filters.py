import sys
sys.path.append('./utils')
from skimage import filters
from scipy import ndimage as ndi
from napari.layers.labels import Labels
import numpy as np
from napari.types import ImageData, LabelsData, VectorsData,LayerDataTuple, PointsData
from utils.utils import *

def iam_gaussian(image:ImageData, sigma = 1.0,proc_all = False) -> ImageData:
    stack = is_stack(image)
    if stack & proc_all:
        result = np.array([filters.gaussian(im,sigma) for im in image])
        return result
    elif stack:
        result = filters.gaussian(image[0],sigma)
    else:
        result = filters.gaussian(image,sigma)
    return result

def iam_gaussian_laplace(image:ImageData, sigma = 1.0,proc_all = False) -> ImageData:
    stack = is_stack(image)
    if stack & proc_all:
        result = np.array([ndi.gaussian_laplace(im,sigma) for im in image])
        return result
    elif stack:
        result = ndi.gaussian_laplace(image[0],sigma)
    else:
        result = ndi.gaussian_laplace(image,sigma)
    return result

def iam_laplace(image:ImageData, sigma = 1.0,proc_all = False) -> ImageData:
    stack = is_stack(image)
    if stack & proc_all:
        result = np.array([filters.laplace(im,sigma) for im in image])
        return result
    elif stack:
        result = filters.laplace(image[0],sigma)
    else:
        result = filters.laplace(image,sigma)
    return result    

def iam_median(image:ImageData, sigma = 1.0,proc_all = False) -> ImageData:
    stack = is_stack(image)
    if stack & proc_all:
        result = [ndi.median_filter(im,sigma) for im in image]
        return result
    elif stack:
        result = ndi.median_filter(image[0],sigma)
    else:
        result = ndi.median_filter(image,sigma)
    return result      