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
#step 2-->compile model
model.compile(optimizer='adam',loss='sparse_crossentrophy',matrics=['accuracy'])

#step 3-->fit
model.fit(x_train,y_train,epochs=2)

# step 4-->evaluate model
test_loss,test_acc=model.evaluate(x_test,y_test)
print("test accuracy",test_acc)

#step 5
prediction=model.predict(x_test)
prediction[1]
plt.figure()
plt.imshow(x_test[1])
plt.show()




