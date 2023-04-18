from .extension import ma

class SymptomSchema(ma.Schema):
    class Meta:
        fields = (
            "id", "fullname", "user_id", "gender",
            "age", "hypertension", "heart_desease", 
            "ever_married", "work_type", "resident_type",
            "avg_glucose_level", "bmi", "smoking_status"
        )