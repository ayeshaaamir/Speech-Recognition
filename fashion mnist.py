import tensorflow as tf
from keras.datasets import fashion_mnist

# access dataset
(x_train,y_train),(x_test,y_test)=fashion_mnist.load_data()

class_name=['T-shirt/top','Trouser','pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']


