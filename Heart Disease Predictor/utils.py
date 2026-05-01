"""
Utility functions for data processing
"""
import pandas as pd
from models import classify_risk_level


def create_input_dataframe(age, gender, cp, rbp, chol, fbs, restecg, thalach, exang, oldpeak, slope):

    return pd.DataFrame({
        'age': [age],
        'gender': [1 if gender == "Male" else 0],
        'chest_pain_type': [cp],
        'resting_blood_pressure': [rbp],
        'cholesterol': [chol],
        'fasting_blood_sugar': [1 if fbs == "True" else 0],
        'resting_ecg': [restecg],
        'max_heart_rate': [thalach],
        'exercise_induced_angina': [1 if exang == "Yes" else 0],
        'st_depression': [oldpeak],
        'st_slope': [slope],
        'num_major_vessels': [0],
        'thalassemia': ["Normal"]
    })


def generate_csv_report(input_data, probability):
    """Generate CSV report for download."""
    report = input_data.copy()
    report['risk_score'] = int(probability * 100)
    report['risk_level'] = classify_risk_level(probability)
    return report.to_csv(index=False)