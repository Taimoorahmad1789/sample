"""
Cardiac Risk Assessment — Streamlit App
----------------------------------------
This app loads a pre-trained scikit-learn pipeline (pipeline.pkl) and uses it
to predict cardiac risk from user-supplied clinical features.

Place `pipeline.pkl` in the same directory as this file before running:

    streamlit run streamlit_app.py
"""

import os

import joblib
import pandas as pd
import streamlit as st

MODEL_PATH = os.path.join(os.path.dirname(__file__), "pipeline.pkl")

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Heart AI Pro — Cardiac Risk Assessment",
    page_icon="🏥",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Load model once (cached so it is not reloaded on every interaction)
# ---------------------------------------------------------------------------
@st.cache_resource
def load_model():
    """Load the pipeline.pkl model.  Returns (model, error_message)."""
    if not os.path.exists(MODEL_PATH):
        return None, (
            f"Model file not found at `{MODEL_PATH}`. "
            "Please place `pipeline.pkl` in the repository root and restart the app."
        )
    try:
        model = joblib.load(MODEL_PATH)
        return model, None
    except Exception as exc:
        return None, f"Failed to load the model: {exc}"


pipeline, load_error = load_model()

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title("🏥 Heart AI Pro — Cardiac Risk Assessment")
st.markdown(
    "Enter the patient's clinical details below and click **Predict** to get a cardiac risk estimate."
)

if load_error:
    st.error(load_error)
    st.info(
        "The app is running in **read-only mode** — predictions are unavailable until "
        "a valid `pipeline.pkl` is placed in the repository root."
    )

st.divider()

# ---------------------------------------------------------------------------
# Input widgets
# ---------------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (years)", min_value=1, max_value=120, value=45, step=1)

    gender = st.selectbox("Sex", options=["Male", "Female"])

    chest_pain = st.selectbox(
        "Chest Pain Type",
        options=["Asymptomatic", "Atypical Angina", "Non-Anginal Pain", "Typical Angina"],
    )

    resting_bp = st.number_input(
        "Resting Blood Pressure (mm Hg)", min_value=50, max_value=300, value=120, step=1
    )

    cholesterol = st.number_input(
        "Serum Cholesterol (mg/dL)", min_value=0, max_value=700, value=200, step=1
    )

    fasting_bs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dL", options=["No", "Yes"]
    )

with col2:
    resting_ecg = st.selectbox(
        "Resting ECG Result",
        options=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"],
    )

    max_hr = st.number_input(
        "Maximum Heart Rate Achieved", min_value=60, max_value=250, value=150, step=1
    )

    exercise_angina = st.selectbox("Exercise-Induced Angina", options=["No", "Yes"])

    st_depression = st.number_input(
        "ST Depression (Oldpeak)", min_value=0.0, max_value=10.0, value=0.0, step=0.1, format="%.1f"
    )

    st_slope = st.selectbox("ST Slope", options=["Flat", "Upsloping", "Downsloping"])

st.divider()

# ---------------------------------------------------------------------------
# Predict button
# ---------------------------------------------------------------------------
predict_clicked = st.button("🔍 Predict Cardiac Risk", disabled=(pipeline is None), use_container_width=True)

if predict_clicked:
    # Map UI values → numeric encodings expected by most standard pipelines
    # trained on the Kaggle Heart Failure Prediction dataset.
    sex_map = {"Male": 1, "Female": 0}
    cp_map = {
        "Asymptomatic": "ASY",
        "Atypical Angina": "ATA",
        "Non-Anginal Pain": "NAP",
        "Typical Angina": "TA",
    }
    ecg_map = {
        "Normal": "Normal",
        "ST-T Wave Abnormality": "ST",
        "Left Ventricular Hypertrophy": "LVH",
    }
    slope_map = {"Flat": "Flat", "Upsloping": "Up", "Downsloping": "Down"}
    angina_map = {"No": "N", "Yes": "Y"}

    features = pd.DataFrame(
        [
            {
                "Age": int(age),
                "Sex": sex_map[gender],
                "ChestPainType": cp_map[chest_pain],
                "RestingBP": int(resting_bp),
                "Cholesterol": int(cholesterol),
                "FastingBS": 1 if fasting_bs == "Yes" else 0,
                "RestingECG": ecg_map[resting_ecg],
                "MaxHR": int(max_hr),
                "ExerciseAngina": angina_map[exercise_angina],
                "Oldpeak": float(st_depression),
                "ST_Slope": slope_map[st_slope],
            }
        ]
    )

    try:
        prediction = pipeline.predict(features)[0]

        # Show probability if the pipeline supports it
        probability = None
        if hasattr(pipeline, "predict_proba"):
            proba = pipeline.predict_proba(features)[0]
            probability = proba[1] if len(proba) > 1 else proba[0]

        if prediction == 1:
            st.error("⚠️ **High Cardiac Risk Detected**")
            risk_label = "High"
        else:
            st.success("✅ **Low Cardiac Risk**")
            risk_label = "Low"

        st.markdown(f"**Risk Level:** {risk_label}")

        if probability is not None:
            st.metric(
                label="Cardiac Risk Probability",
                value=f"{probability * 100:.1f}%",
            )
            st.progress(float(probability))

        with st.expander("📋 Input Summary"):
            st.dataframe(features.T.rename(columns={0: "Value"}))

    except Exception as exc:
        st.error(f"Prediction failed: {exc}")
        st.info(
            "This may happen if the model was trained with different feature names or encodings. "
            "Please verify that `pipeline.pkl` is compatible with the expected input schema."
        )

st.divider()
st.caption(
    "Heart AI Pro · Powered by scikit-learn · "
    "For informational purposes only — not a substitute for medical advice."
)
