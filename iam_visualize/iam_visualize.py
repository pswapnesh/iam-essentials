import numpy as np
import napari
from napari.types import ImageData, LabelsData, VectorsData


def show_vectors(angles: ImageData,magnitude: ImageData, visual_scale: int = 20, edge_width:int = 3, length = 5)->VectorsData:
    xx,yy = np.arange(angles.shape[1]),np.arange(angles.shape[0])
    xx,yy = np.meshgrid(xx,yy)
    xx = xx[::visual_scale,::visual_scale].ravel()
    yy = yy[::visual_scale,::visual_scale].ravel()
    val = angles[::visual_scale,::visual_scale].ravel()
    if magnitude is not None:
        mag = magnitude[::visual_scale,::visual_scale].ravel()    
        vx = mag*np.cos(val)
        vy = mag*np.sin(val)
    else:
        vx = np.cos(val)
        vy = np.sin(val)

    pos = np.zeros((len(xx), 2, 2), dtype=np.float32)
    pos[:, 0, 0] = xx
    pos[:, 0, 1] = yy

    # assign x-y projection
    pos[:, 1, 0] = vx
    pos[:, 1, 1] = vy

    return pos

    # # make the angle property, range 0-2pi
    # angle = np.mod(val, 2 * np.pi)

    # # create a property that is true for all angles  > pi
    # pos_angle = angle > np.pi

    # # create the properties dictionary.
    # properties = {
    #     'angle': angle,
    #     'pos_angle': pos_angle,
    # }

    # # add the vectors
    # layer = viewer.add_vectors(
    #     pos,
    #     edge_width=3,
    #     properties=properties,
    #     edge_color='angle',
    #     edge_colormap='husl',
    #     name='vectors'
    # )

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return magic_exposure_function_list