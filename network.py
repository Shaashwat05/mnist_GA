import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
import cv2

config=tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth=True
session=tf.compat.v1.InteractiveSession(config=config)


(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

input_shape =(28, 28,1)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train /= 255
X_test /= 255


def init():
    model  =Sequential()
    model.add(Conv2D(28, kernel_size=(3, 3), input_shape = input_shape))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(10, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    return model


def train(models):
    losses = []
    for i in range(len(models)):
        history = models[i].fit(x=X_train,y=y_train, epochs=1, validation_data=(X_test, y_test))
        losses.append(round(history.history['loss'][-1], 4))
    return models, losses










#model.save("cnn.h5", model)