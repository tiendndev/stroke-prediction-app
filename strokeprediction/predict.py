from flask import request
from keras.utils import load_img, img_to_array
from keras.models import load_model
import numpy as np
import tensorflow as tf


def prediction_model():
    classes = ['Normal', 'Stroke']
    model_path = "./strokeprediction/h5/model.tflite"
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    img = request.files["file"]
    image_path = "./strokeprediction/static/img/img" + img.filename
    image_path = image_path.replace(" ", "")
    img.save(image_path)
    test_image = load_img(image_path, target_size=(224, 224, 3))
    test_image = img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(input_details[0]['index'], test_image)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])

    print("img_url: ", image_path[26:])

    result = np.argmax(output_data)
    prediction = classes[result]

    return [prediction, image_path[26:]]
