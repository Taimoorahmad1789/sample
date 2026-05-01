"""
Model loading and prediction logic
"""
import streamlit as st
import joblib
import numpy as np
import pandas as pd
from config import MODEL_PATH, EXPLAINER_PATH, RISK_HIGH_THRESHOLD, RISK_MODERATE_THRESHOLD


@st.cache_resource
def load_model_and_explainer():

    try:
        pipeline = joblib.load(MODEL_PATH)
        explainer = joblib.load(EXPLAINER_PATH)
        return pipeline, explainer
    except FileNotFoundError as e:
        raise FileNotFoundError(f"❌ Model files not found: {e}")
    except Exception as e:
        raise Exception(f"❌ Error loading model/explainer: {e}")


def get_risk_prediction(model, input_data):

    try:
        prob = model.predict_proba(input_data)[0][1]
        return prob
    except Exception as e:
        raise ValueError(f"Prediction failed: {e}")


def classify_risk_level(probability):

    if probability > RISK_HIGH_THRESHOLD:
        return 'HIGH'
    elif probability > RISK_MODERATE_THRESHOLD:
        return 'MODERATE'
    else:
        return 'LOW'


def get_shap_values(explainer, processed_input, preprocessor):

    try:
        shap_result = explainer.shap_values(processed_input)
        s_val = shap_result[1][0] if isinstance(shap_result, list) else shap_result[0]

        if len(np.array(s_val).shape) > 1:
            s_val = s_val[:, 1]

        feature_names = preprocessor.get_feature_names_out()
        clean_names = [name.split('__')[-1] for name in feature_names]

        return s_val, feature_names, clean_names
    except Exception as e:
        raise ValueError(f"SHAP calculation failed: {e}")