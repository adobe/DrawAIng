#
# ADOBE CONFIDENTIAL
# __________________
#
# Copyright 2017 Adobe Systems Incorporated
# All Rights Reserved.
#
# NOTICE: All information contained herein is, and remains the property of
# Adobe Systems Incorporated and its suppliers, if any. The intellectual
# and technical concepts contained herein are proprietary to Adobe Systems
# Incorporated and its suppliers and may be covered by U.S. and Foreign
# Patents, patents in process, and are protected by trade secret or
# copyright law. Dissemination of this information or reproduction of this
# material is strictly forbidden unless prior written permission is obtained
# from Adobe Systems Incorporated.
#

import caffe
import numpy as np
import PIL
from PIL import Image
import time 
import uuid
import os
from os import listdir
from os.path import isfile, join
import pickle

class ExtractFeatures :
    PRETRAINED_FILE = 'model/caffe_alexnet_train_sketch_57_43_3_iter_10500.caffemodel'
    sketch_model = 'model/train_val_sketch_57_43_3.prototxt'
    output_layer_sketch = 'fc7'
    transformer = None
    basewidth  = 256

    def __init__(self):
        print ("Loading Model .... ")
        self.sketch_net = caffe.Net(self.sketch_model, self.PRETRAINED_FILE, caffe.TEST)
        print ("Model Loaded !")
        self.load_transformer()

    def load_transformer(self):
        print ("Loading TRANSFORMER ... ")
        self.transformer = caffe.io.Transformer({'data': np.shape(self.sketch_net.blobs['data'].data)})
        self.transformer.set_mean('data', np.array([104, 117, 123]))
        self.transformer.set_transpose('data',(2,0,1))
        self.transformer.set_channel_swap('data', (2,1,0))
        self.transformer.set_raw_scale('data', 255.0)
        print ("TRANSFORMER LOADED !")

    def load_sketch_query(self , image):
        image  = image.resize((self.basewidth,self.basewidth ), PIL.Image.ANTIALIAS)
        image_name  = join("temp",'query.png')
        image.save(image_name)
        sketch_in = (self.transformer.preprocess('data', caffe.io.load_image(image_name))) 
        sketch_in = np.reshape([sketch_in],np.shape(self.sketch_net.blobs['data'].data))
        query = self.sketch_net.forward(data=sketch_in)
        query=np.copy(query[self.output_layer_sketch])
        return query.tolist()
    def create_predict_dataset(self , direct):
        path  = direct
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        print(len(onlyfiles))
        feature_map = {}
        for filename in onlyfiles:
            img  = Image.open(join(direct , filename))
            feature_map[filename] = self.load_sketch_query(img)[0]
        print (len(feature_map))
        with open('./indexed/imagesfeat.pkl','wb') as f:
            pickle.dump(feature_map,f,pickle.HIGHEST_PROTOCOL)
        return len(feature_map)


        


    