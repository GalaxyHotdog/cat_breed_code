import tensorflow as tf
import os
import matplotlib.pyplot as plt

def set_label():
    #return ['Tabby', 'Bengal', 'Persian', 'Siamese', 'Egyptian Mau']
    lst = os.listdir('/home/jovyan/cat-breed-vol-1/dataset/dataset/images/')
    lst.sort()
    return lst

def set_autotuner():
    return tf.data.experimental.AUTOTUNE

def data_preprocessing():
    labels = set_label()
    counts = []
    for label in labels:
        path = "/home/jovyan/cat-breed-vol-1/dataset/dataset/images/" + label + "/"
        counts.append(len(os.listdir(path)))
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(labels, counts)
    ax.set_ylabel('Counts')
    ax.set_xlabel('Labels')
    plt.xticks(rotation=60)
    plt.show()