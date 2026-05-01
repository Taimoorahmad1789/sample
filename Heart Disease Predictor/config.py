"""
Configuration and constants for Cardiac Risk Assessment App
"""

# Model Configuration
MODEL_PATH = 'pipeline.pkl'
EXPLAINER_PATH = 'shap_explainer.pkl'

# Risk Thresholds
RISK_HIGH_THRESHOLD = 0.7
RISK_MODERATE_THRESHOLD = 0.3

# Feature Ranges
AGE_RANGE = (1, 120)
AGE_DEFAULT = 45

BP_RANGE = (80, 200)
BP_DEFAULT = 120

CHOLESTEROL_RANGE = (100, 600)
CHOLESTEROL_DEFAULT = 200

HEART_RATE_RANGE = (60, 220)
HEART_RATE_DEFAULT = 150

ST_DEPRESSION_RANGE = (0.0, 10.0)
ST_DEPRESSION_DEFAULT = 0.0

# Feature Labels
GENDER_OPTIONS = ["Male", "Female"]
CHEST_PAIN_OPTIONS = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"]
FBS_OPTIONS = ["False", "True"]
ECG_OPTIONS = ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"]
ANGINA_OPTIONS = ["No", "Yes"]
SLOPE_OPTIONS = ["Upsloping", "Flat", "Downsloping"]

# Default values for fixed features
NUM_MAJOR_VESSELS_DEFAULT = 0
THALASSEMIA_DEFAULT = "Normal"

# App Settings
APP_TITLE = "Heart AI Pro"
APP_ICON = "🏥"
LAYOUT = "wide"

# Version
APP_VERSION = "2.0"