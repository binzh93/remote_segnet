# -*- coding: utf-8 -*- 
import cv2
import gdal
import os
from scipy import misc


# carry geo information
def writeTiff(im_data, im_width, im_height, im_bands, path, im_geotrans=None, im_proj=None):
    if 'int8' in im_data.dtype.name:
        datatype = gdal.GDT_Byte
    elif 'int16' in im_data.dtype.name:
        datatype = gdal.GDT_UInt16
    else:
        datatype = gdal.GDT_Float32
    '''
    if len(im_data.shape) == 3:
        im_bands, im_height, im_width = im_data.shape
    else:
        im_bands, (im_height, im_width) = 1, im_data.shape
    '''
    # 创建文件
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(path, im_width, im_height, im_bands, datatype)
    if (dataset != None) & (im_geotrans != None) & (im_proj != None):
        dataset.SetGeoTransform(im_geotrans)  # 写入仿射变换参数
        dataset.SetProjection(im_proj)  # 写入投影
    if im_bands == 1:
        for i in range(im_bands):
            dataset.GetRasterBand(i + 1).WriteArray(im_data)
    else:
        for i in range(im_bands):
            dataset.GetRasterBand(i + 1).WriteArray(im_data[i])
    del dataset


def opened_operation(tif_file_in, file_out):
    im_arr = gdal.Open(tif_file_in).ReadAsArray()
    misc.imsave('tmp_label.bmp', im_arr)

    img = cv2.imread('tmp_label.bmp', 0)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    # 闭运算
    #closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    im = gdal.Open("train_im15.tif")
    writeTiff(opened, 2240, 4480, 1, file_out, [0, 1, 0, 0, 0, -1], im.GetProjection())


os.chdir('/home/zb/Desktop')
opened_operation("test_res.tif", "result1.tif")







