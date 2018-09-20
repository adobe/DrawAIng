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

import time
from flask import Flask, request
from ExtractFeatures import ExtractFeatures
from Autocomplete import Autocomplete
from PIL import Image
import json

app = Flask(__name__)
extract = ExtractFeatures()
auto = Autocomplete()

@app.route('/createdataset')
def createdataset():
    result = extract.create_predict_dataset('dataset')
    return "Successfully loaded : " + str(result)

@app.route('/predict' , methods=["POST"])
def predict():
    print (request.files)
    if request.method == 'POST' and request.files['image']:
        img_list = auto.getImageList()
        img = request.files['image']
        img.save('./temp/test.png')
        img = Image.open('./temp/test.png')
        query_feature  = extract.load_sketch_query(img)
        distance  , index = auto.getSimilarImages(query_feature)
        result = []
        for i in range(1,5,1):
            result.append(str(img_list[index[0][i-1]]))
        return json.dumps(result)
    return "Image not found"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)