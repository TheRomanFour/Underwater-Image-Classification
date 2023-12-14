import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf




def load_data():
    
    data = tf.keras.utils.image_dataset_from_directory('data')

    data_iterator = data.as_numpy_iterator()

    batch = data_iterator.next()
    data = data.map(lambda x,y: (x/255, y))
    data.as_numpy_iterator().next()

    train_size = int(len(data)*.7)
    val_size = int(len(data)*.2)
    test_size = int(len(data)*.1)


    train = data.take(train_size)
    val = data.skip(train_size).take(val_size)
    test = data.skip(train_size+val_size).take(test_size)

    return train, val, test,