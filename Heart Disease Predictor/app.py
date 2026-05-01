"""
Main Streamlit app
"""
import streamlit as st
import pandas as pd
import numpy as np
import shap
import matplotlib.pyplot as plt

from config import (
    APP_TITLE, APP_ICON, LAYOUT, APP_VERSION,
    AGE_RANGE, AGE_DEFAULT, BP_RANGE, BP_DEFAULT,
    CHOLESTEROL_RANGE, CHOLESTEROL_DEFAULT, HEART_RATE_RANGE, HEART_RATE_DEFAULT,
    ST_DEPRESSION_RANGE, ST_DEPRESSION_DEFAULT,
    GENDER_OPTIONS, CHEST_PAIN_OPTIONS, FBS_OPTIONS, ECG_OPTIONS, ANGINA_OPTIONS, SLOPE_OPTIONS
)
from models import load_model_and_explainer, get_risk_prediction, classify_risk_level, get_shap_values
from ui.styles import PREMIUM_CSS
from ui.components import (
    show_header, show_sidebar_info, show_input_card_header, show_results_card_header,
    show_divider, display_risk_distribution_chart, display_risk_status, display_insights, show_ready_state
)
from utils import create_input_dataframe, generate_csv_report


# Page Configuration
st.set_page_config(page_title=APP_TITLE, layout=LAYOUT, page_icon=APP_ICON)
st.markdown(PREMIUM_CSS, unsafe_allow_html=True)

# Load Model
try:
    model, explainer = load_model_and_explainer()
except Exception as e:
    st.error(str(e))
    st.stop()

# Sidebar
show_sidebar_info(APP_VERSION)

# Header
show_header("🏥 Cardiac Risk Assessment Dashboard", "Advanced AI-Powered Diagnostic Support for Heart Health")

# Input & Results Sections
col1, col2 = st.columns([1.2, 1.8], gap="large")

# LEFT COLUMN - INPUT
with col1:
    show_input_card_header()

    age = st.number_input("👤 Age (years)", AGE_RANGE[0], AGE_RANGE[1], AGE_DEFAULT)
    rbp = st.slider("💓 Resting BP (mm Hg)", BP_RANGE[0], BP_RANGE[1], BP_DEFAULT)
    chol = st.slider("🩸 Serum Cholesterol (mg/dl)", CHOLESTEROL_RANGE[0], CHOLESTEROL_RANGE[1], CHOLESTEROL_DEFAULT)
    thalach = st.slider("❤️ Max Heart Rate", HEART_RATE_RANGE[0], HEART_RATE_RANGE[1], HEART_RATE_DEFAULT)
    oldpeak = st.number_input("📊 ST Depression", ST_DEPRESSION_RANGE[0], ST_DEPRESSION_RANGE[1], ST_DEPRESSION_DEFAULT, step=0.1)

    show_divider()

    gender = st.selectbox("⚧️ Gender", GENDER_OPTIONS)
    cp = st.selectbox("🫀 Chest Pain Type", CHEST_PAIN_OPTIONS)
    fbs = st.selectbox("🍬 Fasting Blood Sugar > 120", FBS_OPTIONS)
    restecg = st.selectbox("📈 Resting ECG Results", ECG_OPTIONS)
    exang = st.selectbox("🏃 Exercise Induced Angina", ANGINA_OPTIONS)
    slope = st.selectbox("📉 ST Slope", SLOPE_OPTIONS)

    input_data = create_input_dataframe(age, gender, cp, rbp, chol, fbs, restecg, thalach, exang, oldpeak, slope)

# RIGHT COLUMN - RESULTS
with col2:
    show_results_card_header()

    if st.button("🚀 Generate Diagnostic Report", use_container_width=True):
        try:
            preprocessor = model.named_steps['preprocessor']
            processed_input = preprocessor.transform(input_data)
            prob = get_risk_prediction(model, input_data)

            # Display Risk Distribution Chart
            display_risk_distribution_chart(prob)

            # Display Status
            display_risk_status(prob)

            # AI Insights
            st.markdown("---")
            st.markdown("## 📊 AI-Powered Insights")

            s_val, feature_names, clean_names = get_shap_values(explainer, processed_input, preprocessor)
            feature_impact = pd.Series(s_val, index=clean_names).sort_values(ascending=False)
            top_positive = feature_impact.index[0]
            top_negative = feature_impact.index[-1]

            display_insights(top_positive, top_negative)

            # SHAP Analysis
            with st.expander("🔬 View Advanced SHAP Analysis", expanded=False):
                st.info("📌 SHAP analysis shows how each feature contributes to the prediction.")
                fig, ax = plt.subplots(figsize=(12, 7))
                fig.patch.set_facecolor('#ffffff')
                ax.set_facecolor('#ffffff')

                base_val = float(explainer.expected_value[1]) if hasattr(explainer.expected_value, "__len__") else float(explainer.expected_value)
                shap.plots.waterfall(shap.Explanation(
                    values=s_val,
                    base_values=base_val,
                    data=processed_input[0],
                    feature_names=clean_names
                ), show=False)

                plt.tight_layout()
                st.pyplot(fig, use_container_width=True)

            st.markdown("---")

            # Download Report
            csv_data = generate_csv_report(input_data, prob)
            st.download_button(
                label="📥 Download Diagnostic Report",
                data=csv_data,
                file_name="cardiac_diagnostic_report.csv",
                mime="text/csv",
                use_container_width=True
            )

        except Exception as e:
            st.error(f"Error during analysis: {str(e)}")
    else:
        show_ready_state()
