from flask import request
from keras.utils import load_img, img_to_array
from keras.models import load_model
import numpy as np


def prediction_model():
    classes = ['Normal', 'Stroke']
    model_path = "./strokeprediction/h5/model.h5"
    new_model = load_model(model_path)

    img = request.files["file"]
    image_path = "./strokeprediction/static/img/img" + img.filename
    image_path = image_path.replace(" ", "")
    img.save(image_path)
    test_image = load_img(image_path, target_size=(224, 224, 3))
    test_image = img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    print("img_url: ", image_path[26:])

    result = new_model.predict(test_image)
    result1 = result[0]
    for y in range(2):
        if result1[y] == 1.:
            break
    return [classes[y], image_path[26:]]
