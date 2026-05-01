# Cardiac Risk Assessment — Full-Stack

This repository contains **two apps** that run side-by-side:

| App | Directory | Port | Purpose |
|-----|-----------|------|---------|
| Streamlit (Python) | `Heart Disease Predictor/` | 8501 | ML model + original UI |
| React (Node/Vite) | `frontend/` | 3000 | Modern React UI shell |

Neither app removes the other. You can use whichever UI you prefer.

---

## Quick Start

### 1. Streamlit app

```bash
cd "Heart Disease Predictor"
pip install -r requirements.txt   # first time only
streamlit run app.py
# → open http://localhost:8501
```

### 2. React app (in a separate terminal)

```bash
cd frontend
npm install          # first time only
npm run dev
# → open http://localhost:3000
```

Both apps can run simultaneously. The React frontend proxies `/api/*` requests to Streamlit's port 8501 automatically.

---

## Repository Structure

```
.
├── Heart Disease Predictor/    # Streamlit ML app (unchanged)
│   ├── app.py
│   ├── requirements.txt
│   ├── config.py
│   ├── models.py
│   ├── utils.py
│   ├── ui/
│   └── assets/
│
└── frontend/                   # React UI shell (new)
    ├── package.json
    ├── vite.config.js
    ├── README.md               ← detailed frontend docs
    └── src/
        ├── App.jsx
        └── components/
```

For full React setup instructions see **[frontend/README.md](frontend/README.md)**.
