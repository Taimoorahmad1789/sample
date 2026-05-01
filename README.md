# Cardiac Risk Assessment Dashboard

A modern React + Vite frontend for the Cardiac Risk Assessment Dashboard. The app features a dark medical dashboard UI with interactive inputs, simulated AI risk predictions, and rich insights — all running standalone without any backend dependency.

---

## Quick Start

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

## Repository Structure

```
.
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
| Framework | React 18 |
| Build tool | Vite 5 |
| Charts | Recharts |
| Styling | CSS Modules (custom dark theme) |

## Standalone Mode

The app runs fully standalone. When no backend API is available, it automatically falls back to a built-in simulation engine that computes realistic risk scores from the input values — no server required.
