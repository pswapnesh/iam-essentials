from skimage import feature
from scipy import ndimage as ndi
from napari.layers.labels import Labels
import numpy as np
from napari.types import ImageData, LabelsData, VectorsData,LayerDataTuple, PointsData


def iam_shape_index(image:ImageData,sigma: float = 2.0) -> ImageData:
    result = feature.shape_index(image,sigma)
    return result

def hessian_matrix(image:ImageData,sigma: float) -> ImageData:
    result = feature.hessian_matrix(image,sigma, mode = 'reflect')
    return np.array(result)
