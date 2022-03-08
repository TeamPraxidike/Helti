import numpy as np
import tensorflow as tf

def model_prediction(data):

    if isinstance(data, str):
        dataL = [float(i) for i in data.split(",")]

    X = np.array([dataL])

    reloaded = tf.keras.models.load_model('heart_model')

    y = reloaded.predict(X).flatten()

    return y
