import tensorflow as tf
import os

def set_label():
    #return ['Tabby', 'Bengal', 'Persian', 'Siamese', 'Egyptian Mau']
    lst = os.listdir('/home/jovyan/cat-breed-vol-1/dataset/dataset/images/')
    lst.sort()
    print("labels: " + str(lst))
    return lst

def set_autotuner():
    return tf.data.experimental.AUTOTUNE

def data_preprocessing():
    pass