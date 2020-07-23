import tensorflow as tf
from keras.datasets import fashion_mnist

# access dataset
(x_train,y_train),(x_test,y_test)=fashion_mnist.load_data()

class_name=['T-shirt/top','Trouser','pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
import numpy as np
import matplotlib.pyplot as plt
plt.figure()
plt.imshow(x_train[6])
plt.show()

# model for training
from keras.models import Sequential
from keras.layers import Dense,Activation,Flatten
model=Sequential(
    [
     # stack of layers
     Flatten(input_shape=(28,28)) #single dim
     Dense(128,activation=tf.nn.relu)
     Dense(10,activation=tf.nn.softmax) #multi class classification
    ]
)


