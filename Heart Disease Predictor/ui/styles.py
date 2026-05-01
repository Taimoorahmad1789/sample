"""
CSS styling for Cardiac Risk Assessment App
"""

PREMIUM_CSS = """
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html, body {
    font-family: 'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
    background: #0f172a;
    color: #1e293b;
}

.main {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f1628 100%);
    padding: 0 !important;
}

/* Premium Header */
.premium-header {
    background: linear-gradient(135deg, #0ea5e9 0%, #06b6d4 50%, #0284c7 100%);
    padding: 60px 40px;
    text-align: center;
    margin-bottom: 40px;
    box-shadow: 0 20px 60px rgba(6, 182, 212, 0.3);
    border-bottom: 3px solid rgba(6, 182, 212, 0.5);
}

.premium-header h1 {
    font-size: 3.5em;
    color: white;
    font-weight: 900;
    margin: 0;
    text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    letter-spacing: -1px;
}

.premium-header p {
    font-size: 1.3em;
    color: rgba(255, 255, 255, 0.95);
    margin-top: 15px;
    font-weight: 500;
    letter-spacing: 0.5px;
}

/* Input/Results Card */
.card {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    border-radius: 24px;
    padding: 40px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
    border: 2px solid rgba(6, 182, 212, 0.1);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.card:hover {
    box-shadow: 0 30px 80px rgba(6, 182, 212, 0.2);
    transform: translateY(-5px);
}

.card h2 {
    color: #0284c7;
    font-size: 1.8em;
    font-weight: 800;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.card .subtitle {
    color: #64748b;
    font-size: 0.95em;
    margin-bottom: 30px;
    font-weight: 500;
}

.divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, #0ea5e9, transparent);
    margin: 30px 0;
    border-radius: 10px;
}

/* Risk Badges */
.risk-high {
    background: linear-gradient(135deg, #fca5a5 0%, #f87171 100%);
    color: white;
    padding: 25px;
    border-radius: 16px;
    font-size: 1.4em;
    font-weight: 800;
    text-align: center;
    margin: 20px 0;
    box-shadow: 0 10px 30px rgba(244, 63, 94, 0.3);
    border-left: 6px solid #dc2626;
}

.risk-moderate {
    background: linear-gradient(135deg, #fdba74 0%, #fb923c 100%);
    color: white;
    padding: 25px;
    border-radius: 16px;
    font-size: 1.4em;
    font-weight: 800;
    text-align: center;
    margin: 20px 0;
    box-shadow: 0 10px 30px rgba(249, 115, 22, 0.3);
    border-left: 6px solid #f97316;
}

.risk-low {
    background: linear-gradient(135deg, #86efac 0%, #4ade80 100%);
    color: white;
    padding: 25px;
    border-radius: 16px;
    font-size: 1.4em;
    font-weight: 800;
    text-align: center;
    margin: 20px 0;
    box-shadow: 0 10px 30px rgba(34, 197, 94, 0.3);
    border-left: 6px solid #16a34a;
}

/* Insight Boxes */
.insight-box {
    background: linear-gradient(135deg, #0ea5e9 0%, #06b6d4 100%);
    color: white;
    padding: 30px;
    border-radius: 16px;
    margin: 20px 0;
    box-shadow: 0 15px 40px rgba(6, 182, 212, 0.3);
    border: 2px solid rgba(6, 182, 212, 0.5);
    transition: all 0.3s ease;
}

.insight-box:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 50px rgba(6, 182, 212, 0.4);
}

.insight-box h4 {
    color: white;
    font-size: 1.2em;
    margin-bottom: 12px;
    font-weight: 800;
}

.insight-box p {
    font-size: 1.05em;
    line-height: 1.6;
    margin: 0;
}

.insight-box-green {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
}

/* Button */
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, #0ea5e9 0%, #06b6d4 50%, #0284c7 100%) !important;
    color: white !important;
    font-weight: 800 !important;
    font-size: 1.1em !important;
    height: 60px !important;
    border-radius: 16px !important;
    border: none !important;
    box-shadow: 0 10px 30px rgba(6, 182, 212, 0.4) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 15px 45px rgba(6, 182, 212, 0.6) !important;
}

/* Download Button */
.stDownloadButton > button {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
    color: white !important;
    width: 100% !important;
    border-radius: 16px !important;
    font-weight: 800 !important;
    font-size: 1.05em !important;
    height: 55px !important;
}

/* Alerts */
.stInfo, .stSuccess, .stWarning, .stError {
    border-radius: 12px !important;
    padding: 18px 24px !important;
    font-weight: 600 !important;
}

/* Responsive */
@media (max-width: 768px) {
    .premium-header h1 { font-size: 2.2em; }
    .card { padding: 25px; }
}
</style>
"""