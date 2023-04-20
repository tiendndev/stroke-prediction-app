import joblib
import numpy as np


def predict_Stroke(gender, age, hypertension, heart_disease, ever_married, Residence_type, avg_glucose_level, bmi, Private, Govt_job, Self_employed, children, Never_worked):
    loaded_rfc = joblib.load(r"strokeprediction\KnnModel\random_forest.joblib")
    x = np.zeros(13)
    x[0] = gender
    x[1] = age
    x[2] = hypertension
    x[3] = heart_disease
    x[4] = ever_married
    x[5] = Residence_type
    x[6] = avg_glucose_level
    x[7] = bmi
    x[8] = Private
    x[9] = Govt_job
    x[10] = Self_employed
    x[11] = children
    x[12] = Never_worked

    return int(loaded_rfc.predict([x])[0])
