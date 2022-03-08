from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf
import cv2

def model_prediction(imgpath):
    
    class_names = ["Normal", "Pneumonia"]

    model = load_model("./xray_model_cv2")

    img_width = 64
    img_height = 64

    img = cv2.imread(imgpath)
    img = cv2.resize(img, (img_width, img_height), interpolation=cv2.INTER_AREA)

    img = np.array(img)
    img= np.resize(img,(img_height,img_width,3))
    img = img.astype('float32')
    img /= 255

    probability_model = tf.keras.Sequential([model, 
                                             tf.keras.layers.Softmax()])

    img = (np.expand_dims(img,0))
    prediction = probability_model.predict(img)

    return (class_names[np.argmax(prediction[0])], prediction[0][np.argmax(prediction[0])])
