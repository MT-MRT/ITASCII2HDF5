# Sebastian Schramm, FG MRT Universität Kassel
# 03.06.2022

import numpy as np
import os
import math
import matplotlib.pyplot as plt
import h5py

def convert(s): 
    s = s.strip().replace(',', '.')
    try:
        n = float(s)
    except:
        n = math.nan
    return n

if __name__ == '__main__':

    ##############################################################################
    folder_src = './ASCII/' # Hier den Ordner mit den ASCII-Dateien auswählen
    output_file = './ImageSeries.hdf5' # Hier den Dateinamen der HDF5 Datei ändern
    ##############################################################################
    
    file_list = os.listdir(folder_src)
    hdf_file_handle = h5py.File(output_file, "w")

    for file_number, file_name in enumerate(file_list):
        with open(folder_src + file_name, 'r') as f:
            
            dict = {}
            data_bool = False
            parameter_bool = False
            settings_bool = False

            i = 0
            for l in f:
                if l == '\n':
                    data_bool = False
                    parameter_bool = False
                    settings_bool = False

                if data_bool == True:
                    strnumbers = l.split('\t')
                    newImage[i,:] = np.asarray(list(convert(s) for s in strnumbers if s!='' and s!= '\n'))
                    i = i + 1

                if settings_bool == True:
                    split_list = l.split('=')
                    dict['Settings_' + split_list[0]] = split_list[1][:-1]
                
                if parameter_bool == True:
                    split_list = l.split('=')
                    dict['Parameter_' + split_list[0]] = split_list[1][:-1]

                if l == '[Data]\n':
                    newImage = np.zeros((int(dict['Settings_ImageHeight']), int(dict['Settings_ImageWidth'])))
                    data_bool = True

                if l == '[Parameter]\n':
                    parameter_bool = True

                if l == '[Settings]\n':
                    settings_bool = True

            print("image_" + "{:06d}".format(file_number))
            dset = hdf_file_handle.create_dataset("image_" + "{:06d}".format(file_number), 
                                                    (int(dict['Settings_ImageHeight']),int(dict['Settings_ImageWidth'])),
                                                    dtype='float16',
                                                    data=newImage,
                                                    compression="gzip")

            for key in dict:
                dset.attrs[key] = dict[key]

    hdf_file_handle.close()
