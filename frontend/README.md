# React Frontend — Cardiac Risk Assessment Dashboard

A React + Vite dark medical dashboard for cardiac risk assessment. The app runs **fully standalone** — no Python or Streamlit dependency required.

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

---

## Running the React App

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

- The app is **fully standalone** — no backend required.
- Risk predictions are computed locally by a built-in simulation engine using clinical thresholds.
- If a real backend API becomes available at `/api/predict`, the app will use it automatically.
