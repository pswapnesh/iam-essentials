from skimage.feature import watershed,slic
from skimage.feature import peak_local_max
from scipy import ndimage as ndi
from napari.layers.labels import Labels
import numpy as np
from napari.types import ImageData, LabelsData, VectorsData,LayerDataTuple, PointsData


def iam_gauss(image:ImageData,threshold: float) -> LabelsData:
    result = image > threshold
    return result
