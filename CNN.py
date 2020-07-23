# neural network
# 1: CNN-->conventional neural network [1 input,1 hidden layer,1 output layer]
# 2: CNN-->convolutional neural network [1 input,multiple hidden layer,1 output layer]
# model2=Sequential()
# Block 1
# step 1-->convolutional layer  
# step 2-->pooling layer
# step 3-->flatten layer
# step 4-->dense layer
# Block 2
# step 1-->convolutional layer 
# step 2-->pooling layer
# step 3-->flatten layer
# step 4-->dense layer

from tensorflow.keras import layers
from keras.layers.convolutional import Conv2D
model2=Sequential()
model2.add(Conv2D(32,(3,3),input_shape=(64,64)))
