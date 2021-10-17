import numpy as np
from napari.types import ImageData, LabelsData, VectorsData,LayerDataTuple
from napari.layers.vectors import Vectors
import scipy.ndimage as ndi
from skimage.feature import structure_tensor
from typing import List

def _image_orthogonal_matrix22_eigvals(M00, M01, M11):
    l1 = (M00 + M11) / 2 + np.sqrt(4 * M01 ** 2 + (M00 - M11) ** 2) / 2
    l2 = (M00 + M11) / 2 - np.sqrt(4 * M01 ** 2 + (M00 - M11) ** 2) / 2
    return l1, l2

def _eigensystem(m00,m01,m11):
    b = np.sqrt(4 * m01 ** 2 + (m00 - m11) ** 2)
    a = (m00 + m11)
    l1 = a / 2 + b / 2
    l2 = a / 2 - b / 2 
    
    v1 = - (-m00+m11 + b)/(2*m01) #[v1,1]
    v2 = - (-m00+m11 - b)/(2*m01) #[v2,1]
    return l1,l2,v1,v2

def iam_orientation(image:ImageData,sigma = 3.0) -> LayerDataTuple:
    '''
    Local orientation of images from structure tensor
    '''
    Srr, Src, Scc = structure_tensor(image, sigma=sigma,order="xy")
    l1,l2,v1,v2 = _eigensystem(Srr, Src, Scc)
    angles = np.arctan2(1,v1)
    anisotropy = (l1-l2)/(l1+l2)
    coherence = anisotropy**2
    power = 0.5 * (Srr + Scc ) + (l1 - l2)/2
    return [(angles, {'name': 'angles'}),(coherence, {'name': 'coherence'}), (power, {'name': 'power'})]

def iam_show_orientation(angles: ImageData,magnitude: ImageData, use_magnitude = False, visual_scale: int = 20)->Vectors:
    '''
    Use angles and magnitude to create a vectors layer
    '''

    xx,yy = np.arange(angles.shape[1]),np.arange(angles.shape[0])
    xx,yy = np.meshgrid(xx,yy)
    xx = xx[::visual_scale,::visual_scale].ravel()
    yy = yy[::visual_scale,::visual_scale].ravel()
    val = angles[::visual_scale,::visual_scale].ravel()
    if (magnitude is not None) & use_magnitude:
        mag = magnitude[::visual_scale,::visual_scale].ravel()    
        vx = mag*np.cos(val)
        vy = mag*np.sin(val)
    else:
        vx = np.cos(val)
        vy = np.sin(val)

    pos = np.zeros((len(xx), 2, 2), dtype=np.float32)
    pos[:, 0, 0] = yy
    pos[:, 0, 1] = xx

    # assign x-y projection
    pos[:, 1, 0] = vy
    pos[:, 1, 1] = vx

    properties = {'angle': val}

    
    return Vectors(pos,properties = properties,edge_width = 2,length = 5,edge_color='angle',edge_colormap='husl' ,name = 'vectors')

