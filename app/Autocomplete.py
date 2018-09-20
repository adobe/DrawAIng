from sklearn.neighbors import NearestNeighbors,LSHForest
import numpy as np
import subprocess
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


import os
import simplejson as json
import codecs
import pickle

class Autocomplete:
    feats  = None
    img_list = None
    nbrs = None
    def __init__(self):
        with open('./indexed/imagesfeat.pkl', 'rb') as handle:
            features = pickle.load(handle)  
        self.feats = features.values()
        #print (self.feats) 
        self.img_list = features.keys()
        self.nbrs = NearestNeighbors(n_neighbors=5, algorithm='brute',metric='cosine').fit(self.feats)

    def getImageList(self):
        return self.img_list
    def getFeats(self):
        return str(len(self.feats))
    def getSimilarImages(self,query):
        reshapedData = np.reshape(query , [np.shape(query)[1]])
        reshapedData = reshapedData.reshape(1,-1)
        #print(reshapedData)
        distances, indices = self.nbrs.kneighbors(reshapedData)
        return distances , indices