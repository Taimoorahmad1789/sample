# React Frontend — Cardiac Risk Assessment Dashboard

A React + Vite UI shell that mirrors the dark-themed medical dashboard of the existing Streamlit app.  
Both apps run **side-by-side**; neither replaces the other.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | React 18 |
| Build tool | Vite 5 |
| Charts | Recharts |
| Styling | CSS Modules (custom dark theme) |

---

## Getting Started

### Prerequisites

- **Node.js ≥ 18** (`node --version`)
- **npm ≥ 9** (`npm --version`)
- **Python ≥ 3.9** with the Streamlit app dependencies installed

---

## Running Streamlit and React Side-by-Side

Open **two separate terminal windows/tabs**:

### Terminal 1 — Streamlit (Python backend + UI)

```bash
cd "Heart Disease Predictor"
pip install -r requirements.txt   # first time only
streamlit run app.py
```

Streamlit starts on **http://localhost:8501**

---

### Terminal 2 — React frontend (dev server)

```bash
cd frontend
npm install          # first time only
npm run dev
```

React starts on **http://localhost:3000**

---

## Build for Production

```bash
cd frontend
npm run build        # output goes to frontend/dist/
npm run preview      # serve the production build locally
```

---

## Dev Proxy

`vite.config.js` includes a lightweight proxy so the React app can call the Python backend:

```
React (localhost:3000) → /api/* → Streamlit (localhost:8501)
```

Any `fetch('/api/predict', ...)` call from React is transparently forwarded to Streamlit.  
No CORS configuration is needed during development.

---

## Project Structure

```
frontend/
├── index.html
├── package.json
├── vite.config.js
├── README.md           ← you are here
└── src/
    ├── main.jsx
    ├── App.jsx
    ├── App.module.css
    ├── index.css
    └── components/
        ├── Header.jsx
        ├── Header.module.css
        ├── Sidebar.jsx
        ├── Sidebar.module.css
        ├── InputForm.jsx
        ├── InputForm.module.css
        ├── ResultsPanel.jsx
        └── ResultsPanel.module.css
```

---

## Notes

- The React app is a **UI shell** — it can call the Streamlit backend through the `/api` proxy.
- When the backend is not running, the frontend falls back to **demo/simulated results** so you can still explore the UI.
- The Streamlit app is **not modified** and remains fully functional at `http://localhost:8501`.
