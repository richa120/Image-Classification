# -*- coding: utf-8 -*-
"""Image classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qKI8qP2cxWqr43Rpor-iXFeZH9bLWs3d
"""

# Commented out IPython magic to ensure Python compatibility.
!pip install ipython-autotime
# %load_ext autotime

# This program classifies images

# Data : Images
# 1. Download manually the images from google
# 2. Download dataset from kaggle.com
# 3. Build a Image Web Crawler
# 4. Use python libraries to scrape the images(Using)

!pip install bing-image-downloader

!mkdir images

from bing_image_downloader import downloader
downloader.download("Rose", limit=30, output_dir='images', adult_filter_off= True)

from bing_image_downloader import downloader
downloader.download("Range Rover", limit=30, output_dir='images', adult_filter_off= True)

from bing_image_downloader import downloader
downloader.download("Orchids", limit=30, output_dir='images', adult_filter_off= True)

import numpy as np

a = np.array([[1,2,3,4,5],
              [4,5,6,7,8]])
a.ndim

#How do i convert matrix to vector?- flatten()

a.flatten()

#Preprocessing
# 1. resize()
# 2. flatten()

import os
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.transform import resize

target = []
images = []
flat_data = []

DATADIR = '/content/images'
CATEGORIES = ['Rose', 'Range Rover', 'Orchids']

for category in CATEGORIES:
  class_num = CATEGORIES.index(category) #Label encoding the values
  path = os.path.join(DATADIR,category) #Create path to use all the images
  for img in os.listdir(path):
    img_array = imread(os.path.join(path,img))
    #print(img_array.shape)
    #plt.imshow(img_array)

    img_resized = resize(img_array,(150,150,5)) #Normalizes the value from 0 to 1
    flat_data.append(img_resized.flatten())
    images.append(img_resized)
    target.append(class_num)

flat_data = np.array(flat_data)
target = np.array(target)
images = np.array(images)

len(flat_data[0])

150*150*3

target

unique,count = np.unique(target,return_counts= True)
plt.bar(CATEGORIES, count)

# Split data into Training & Testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(flat_data, target, test_size= 0.3, random_state= 109)

from sklearn.model_selection import GridSearchCV
from sklearn import svm
param_grid = [{'C':[1,10,100,1000],'kernel':['linear']},
              {'C':[1,10,100,1000],'gamma':[0.001,0.0001],'kernel':['rbf']},
]
svc = svm.SVC(probability=True)
clf = GridSearchCV(svc,param_grid)
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)
y_pred

y_test

from sklearn.metrics import accuracy_score,confusion_matrix

accuracy_score(y_pred,y_test)

confusion_matrix(y_pred,y_test)

