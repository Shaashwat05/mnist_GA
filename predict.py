from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist
import cv2
import random
import numpy as np


(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)

input_shape =(28, 28,1)

X_train = X_train.astype('float32')

X_train /= 255

model = load_model("cnn.h5")

output = model.predict(X_train[0].reshape(1,28,28,1))

print("Model output :", output)
print("Value with highest probability :", np.argmax(output[0]))
