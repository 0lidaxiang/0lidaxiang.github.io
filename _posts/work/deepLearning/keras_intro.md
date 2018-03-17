# Keras Introduction
> [荒岛书生](http://www.lidaxiang.cn/)
> StartTime: 2017-11-17,ModifyTime:2017-11-27  

## Keras installion
[Install keras Introduction link](https://keras.io/#installation)  
[Install tensorflow Introduction link](https://www.tensorflow.org/install/)
[Other config, GPU&Theano](https://www.pyimagesearch.com/2016/07/18/installing-keras-for-deep-learning/)
### Requirement already satisfied:
+ tensorflow
+ numpy>=1.9.1
+ six>=1.9.0
+ pyyaml
+ scipy>=0.14
```
pip3 install tensorflow
pip3 install keras
```
### Questions:
1. install succefully and 'import keras' succefully in command line.But faild when using 'python3 XXX.py' command.
SOLUTION:
```
$ python3
>>> import sys
>>> sys.path.insert(0, "/usr/local/lib/python3.5/dist-packages")
```

## Keras Test installion
[Keras Test installion](https://keras-cn.readthedocs.io/en/latest/for_beginners/keras_linux/)
