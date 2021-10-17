from skimage.segmentation import watershed,slic
from skimage.feature import peak_local_max
from skimage.filters import threshold_otsu, threshold_local
from scipy import ndimage as ndi
from napari.layers.labels import Labels
import numpy as np
from napari.types import ImageData, LabelsData, VectorsData,LayerDataTuple, PointsData


def iam_threshold(image:ImageData,threshold: float) -> LabelsData:
    result = image > threshold
    return result

def iam_threshold_otsu(image:ImageData,local = False, is_stack = False) -> LabelsData:
    if is_stack:
        return [iam_threshold_otsu(im,local = local, is_stack = False) for im in image]
    
    if local:
        result = image > threshold_local(image)
    else:
        result = image > threshold_otsu(image)
    return result

def iam_slic(image:ImageData,
    mask:LabelsData,
    use_mask = False,
    n_segments=100,
    compactness=10.0,
    max_num_iter=10,
    sigma=0,
    multichannel=False) -> LabelsData:
    if use_mask:
        segments = slic(image, n_segments=n_segments, compactness=compactness,max_num_iter=max_num_iter,sigma=sigma,multichannel=multichannel,mask=mask)
    else:
        segments = slic(image, n_segments=n_segments, compactness=compactness,max_num_iter=max_num_iter,sigma=sigma,multichannel=multichannel)
    return segments

#def iam_watershed(image:ImageData, markers: LabelsData, mask:LabelsData; connectivity: int, watershed_line = False) -> Labels:
      