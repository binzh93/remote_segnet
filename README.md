# Remote_SegNet 

# Introduction
This is a method using segnet to train and predict architectural change in image change detection.Here architectural change is only newly added buildings in two images. What I did was combine the two images and predict the result directly.Here images are all high-resolution images which are photographed in 2015 and 2017.All images have 4 channels.Combine the two years' images and train the merged image by the hand label to predict the test images in architectural changes.

# Requirements
python 2.7 <br/>
tensorflow 1.2 - GPU <br/>
gdal <br/>

# datamake.py
This file makes train file and test file,here is the step:
1.split a big image save in a path
2.

# model.py 
This file trains network and prediction the result





