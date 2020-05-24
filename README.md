[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-360/) 

# mnist_GA
 A **mnist handwritten dataset** classifier which uses a **neural network** as its brain. The **CNN** weights act as the genes of each individual who are trained using **genetic algorithm** to produce new individuals. Similarly the training process goes on.
 
 Each individual is trained for 1 epoch and then a new generation is produced. To get better the results, keep changing the hyper parameters using hid and trial.

### Prerequisites

What things you need to install the software and how to install them

```
cv2
numpy 
random
tensorflow==2.2
```

## Getting Started

Download a python interpeter preferable a version beyond 3.0. Install the prerequisute libraries given above,and make sure you have the correct version of **TensorFlow**. Also certain hardware and software requirements like good **Nvidia GPU** and **(CUDA+CUDNN)** respectively are required. Then run genetic.py in your system to train the model and save it. Then run predict.py to see the output in the format given below.

```
$ genetic.py

$ predict.py

```

## Cloning
```bash
$ git clone https://github.com/Shaashwat05/mnist_GA
```

## MNIST Output
The output of the classifier can be seen.

![The input Image to cartoonize.py](https://github.com/Shaashwat05/mnist_GA/blob/master/output.png)


## Built With

* [python3](https://www.python.org/) - The software used

## Author
[![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Profile-teal.svg)](https://www.linkedin.com/in/shaashwat-agrawal-1904a117a/)       [![Github-profile](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/Shaashwat05)

* [**Shaashwat Agrawal**](https://github.com/Shaashwat05) 

# Documentation/ Website

The whole working of the code and explanation of it as well as the concepts can be viewed in this medium website, do visit.
https://medium.com/@shaas2000/mnist-classifier-using-genetic-cnn-e1e860ecc2e9
