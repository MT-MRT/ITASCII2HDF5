# Sebastian Schramm, FG MRT Universität Kassel
# 03.06.2022

import numpy as np
import os
import math
import matplotlib.pyplot as plt
import h5py

if __name__ == '__main__':
    hdf_file_name = './ImageSeries.hdf5'
    hdf_file_handle = h5py.File(hdf_file_name,'r')
    print(list(hdf_file_handle.keys()))

    for key in hdf_file_handle.keys():
        plt.figure()
        plt.imshow(hdf_file_handle[key])
        title_string = hdf_file_handle[key].attrs['Parameter_RecDate'] + ' ' \
                        + hdf_file_handle[key].attrs['Parameter_RecTime'] + ' ' \
                        + hdf_file_handle[key].attrs['Parameter_ms']
        plt.title(title_string)
        plt.show()

    hdf_file_handle.close()