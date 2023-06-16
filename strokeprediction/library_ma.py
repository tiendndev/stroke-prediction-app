from .extension import ma


class SymptomSchema(ma.Schema):
    class Meta:
        fields = (
            "id", "fullname", "user_id", "gender",
            "age", "hypertension", "heart_disease",
            "ever_married", "work_type", "residence_type",
            "avg_glucose_level", "bmi", "smoking_status", "stroke", "percentageStroke"
        )

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "email", "password", "user_name")