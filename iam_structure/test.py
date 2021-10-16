import numpy as np
import napari
from skimage.io import imread
from iam_structure import *

fname = 'D:\Swapnesh\Work\Projects-Colaboration\Tam\Alignment\inputs\Rippling-DIA.tif'
im = imread(fname)[0]

viewer = napari.Viewer()

layer = viewer.add_image(im, name='original')
d1 = viewer.window.add_dock_widget(show_vectors, area='right')
#d2 = viewer.window.add_dock_widget(orientation_by_structure_tensor, area='right')

visual_scale = 20
angles,anisotropy,coherence,power = orientation_by_structure_tensor(im,sigma=3)
xx,yy = np.arange(angles.shape[1]),np.arange(angles.shape[0])
xx,yy = np.meshgrid(xx,yy)
xx = xx[::visual_scale,::visual_scale].ravel()
yy = yy[::visual_scale,::visual_scale].ravel()
val = angles[::visual_scale,::visual_scale].ravel()
vx = np.cos(val)
vy = np.sin(val)

pos = np.zeros((len(xx), 2, 2), dtype=np.float32)
pos[:, 0, 0] = xx
pos[:, 0, 1] = yy

# assign x-y projection
pos[:, 1, 0] = vx
pos[:, 1, 1] = vy

# make the angle property, range 0-2pi
angle = np.mod(val, 2 * np.pi)

# create a property that is true for all angles  > pi
pos_angle = angle > np.pi

# create the properties dictionary.
properties = {
    'angle': angle,
    'pos_angle': pos_angle,
}

# add the vectors
layer = viewer.add_vectors(
    pos,
    edge_width=3,
    properties=properties,
    edge_color='angle',
    edge_colormap='husl',
    name='vectors'
)

# set the edge color mode to colormap
layer.edge_color_mode = 'colormap'

napari.run()