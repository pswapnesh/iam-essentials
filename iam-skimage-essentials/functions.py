import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import unsharp_mask
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import gaussian
from skimage.feature import structure_tensor

def _image_orthogonal_matrix22_eigvals(M00, M01, M11):
    l1 = (M00 + M11) / 2 + np.sqrt(4 * M01 ** 2 + (M00 - M11) ** 2) / 2
    l2 = (M00 + M11) / 2 - np.sqrt(4 * M01 ** 2 + (M00 - M11) ** 2) / 2
    return l1, l2

def eigensystem(m00,m01,m11):
    b = np.sqrt(4 * m01 ** 2 + (m00 - m11) ** 2)
    a = (m00 + m11)
    l1 = a / 2 + b / 2
    l2 = a / 2 - b / 2 
    
    v1 = - (-m00+m11 + b)/(2*m01) #[v1,1]
    v2 = - (-m00+m11 - b)/(2*m01) #[v2,1]
    return l1,l2,v1,v2


def orientation_by_structure_tensor(im,s = 3):
    Srr, Src, Scc = structure_tensor(im, sigma=s)
    l1,l2,v1,v2 = eigensystem(Srr, Src, Scc)
    
    #k1 = -(Hrr - eigs[0])/Hrc #[eigvec = [1,k] / sqrt(1+k**2)]
    #k2 = -(Hrr - eigs[1])/Hrc #[eigvec = [1,k] / sqrt(1+k**2)]
    #k2 = -Hrc/(Hcc - eigs[1])
    
    theta = np.arctan2(1,v1)
    anisotropy = (l1-l2)/(l1+l2)
    coherence = anisotropy**2
    power = 0.5 * (Srr + Scc ) + (l1 - l2)/2
    return theta,anisotropy,coherence,power


# def order_parameter_strength(im,cell_sigma=0.5,local_sigma=2):
#     k1,k2 = orientation_by_structure_tensor(im,cell_sigma)
#     cell_orientation = np.arctan(1.0/k1)    
#     theta = cell_orientation- gaussian(cell_orientation,local_sigma)
#     S = (2*np.cos(theta)-1)/2
#     return gaussian(S,local_sigma)

# def nematic_order(im,cell_sigma=0.5,local_sigma=2):
#     ''' legendre poly / cell direction vs local prefered direction  '''
#     k1,k2 = orientation_by_structure_tensor(im,cell_sigma)
#     cell_orientation = np.arctan(1.0/k1)

#     k1,k2 = orientation_by_structure_tensor(im,local_sigma)
#     local_prefered_orientation = np.arctan(1.0/k1)
    
#     theta = cell_orientation-local_prefered_orientation
#     S = (3*np.cos(theta)**2-1)/2
#     return gaussian(S,local_sigma)
