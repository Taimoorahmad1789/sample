# Cardiac Risk Assessment Dashboard

A modern React + Vite frontend **and** a Streamlit app backed by a trained ML pipeline for the Cardiac Risk Assessment Dashboard.

---

## Quick Start — React App

```bash
cd frontend
npm install          # first time only
npm run dev
# → open http://localhost:3000
```

To build for production:

```bash
cd frontend
npm run build        # output goes to frontend/dist/
npm run preview      # serve the production build locally
```

---

## Quick Start — Streamlit App (with ML model)

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Place the model file

Copy `pipeline.pkl` into the **repository root** (same folder as `streamlit_app.py`):

```
.
├── pipeline.pkl        ← place it here
├── streamlit_app.py
└── requirements.txt
```

> **Note:** If `pipeline.pkl` is missing the app will still start and show a friendly message instead of crashing. Predictions will be unavailable until the file is provided.

### 3. Run the Streamlit app

```bash
streamlit run streamlit_app.py
# → opens http://localhost:8501
```

---

## Repository Structure

```
.
├── streamlit_app.py            # Streamlit ML prediction app
├── requirements.txt            # Python dependencies
├── pipeline.pkl                # Pre-trained sklearn pipeline (add here)
├── README.md
└── frontend/                   # React app (Vite + React 18)
    ├── index.html
    ├── package.json
    ├── vite.config.js
    ├── README.md
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── App.module.css
        ├── index.css
        └── components/
            ├── Header.jsx
            ├── Sidebar.jsx
            ├── InputForm.jsx
            └── ResultsPanel.jsx
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| React framework | React 18 |
| Build tool | Vite 5 |
| Charts | Recharts |
| Styling | CSS Modules (custom dark theme) |
| ML app | Streamlit |
| ML pipeline | scikit-learn + joblib |

## Standalone Mode (React)

The React app runs fully standalone. When no backend API is available, it automatically falls back to a built-in simulation engine that computes realistic risk scores from the input values — no server required.

## Expected Model Input Schema

The Streamlit app feeds the following features to `pipeline.pkl` (aligned with the Kaggle *Heart Failure Prediction* dataset):

| Feature | Type | Values |
|---------|------|--------|
| Age | int | e.g. 45 |
| Sex | int | 0 = Female, 1 = Male |
| ChestPainType | str | ASY, ATA, NAP, TA |
| RestingBP | int | mm Hg |
| Cholesterol | int | mg/dL |
| FastingBS | int | 0 / 1 |
| RestingECG | str | Normal, ST, LVH |
| MaxHR | int | bpm |
| ExerciseAngina | str | N / Y |
| Oldpeak | float | ST depression |
| ST_Slope | str | Flat, Up, Down |
