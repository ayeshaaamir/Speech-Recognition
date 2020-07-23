import tensorflow as tf
from keras.datasets import fashion_mnist

# access dataset
(x_train,y_train),(x_test,y_test)=fashion_mnist.load_data()
