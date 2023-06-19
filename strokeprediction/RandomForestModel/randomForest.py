import joblib
import numpy as np

modelPath = "./strokeprediction/RandomForestModel/RandomForestStrokePredict.joblib"

def predict_Stroke(age, hypertension, heart_disease, ever_married, Residence_type, avg_glucose_level,
                   bmi, gender_Male, gender_Other, work_type_Never_worked, work_type_Private, work_type_Self_employed,
                   work_type_children, smoking_status_formerly_smoked, smoking_status_never_smoked, 
                   smoking_status_smokes, bmi_cat_Ideal, bmi_cat_Overweight, bmi_cat_Obesity, age_cat_Teens,age_cat_Adults,
                   age_cat_Mid_Adults, age_cat_Elderly, glucose_cat_Normal, glucose_cat_High, glucose_cat_Very_High):
    loaded_rfc = joblib.load(modelPath)
    x = np.zeros(26)
    x[0] = age
    x[1] = hypertension
    x[2] = heart_disease
    x[3] = ever_married
    x[4] = Residence_type
    x[5] = avg_glucose_level
    x[6] = bmi
    x[7] = gender_Male
    x[8] = gender_Other
    x[9] = work_type_Never_worked
    x[10] = work_type_Private
    x[11] = work_type_Self_employed
    x[12] = work_type_children
    x[13] = smoking_status_formerly_smoked
    x[14] = smoking_status_never_smoked
    x[15] = smoking_status_smokes
    x[16] = bmi_cat_Ideal
    x[17] = bmi_cat_Overweight
    x[18] = bmi_cat_Obesity
    x[19] = age_cat_Teens
    x[20] = age_cat_Adults
    x[21] = age_cat_Mid_Adults
    x[22] = age_cat_Elderly
    x[23] = glucose_cat_Normal
    x[24] = glucose_cat_High
    x[25] = glucose_cat_Very_High

    percentage = loaded_rfc.predict_proba([x])[:,1]

    return [int(loaded_rfc.predict([x])[0]), float(percentage[0]*100)]
