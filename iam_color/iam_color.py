import sys
sys.path.append('./utils')
from skimage import color
from napari.layers.labels import Labels
import numpy as np
from napari.types import ImageData, LabelsData, VectorsData,LayerDataTuple, PointsData

def iam_rgb2gray(image:ImageData) -> ImageData:
    result = color.rgb2gray(image)
    return result