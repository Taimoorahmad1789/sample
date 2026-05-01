"""
CSS styling for Cardiac Risk Assessment App
"""
import base64
import os


def _get_bg_data_uri() -> str:
    """Load the cardiac background SVG and return a base64 data URI."""
    svg_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "assets", "static", "cardiac_bg.svg",
    )
    try:
        with open(svg_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
        return f"data:image/svg+xml;base64,{encoded}"
    except FileNotFoundError:
        return ""


_BG_URI = _get_bg_data_uri()

# CSS snippet for the cardiac background image (injected only when the file loads)
_BG_IMAGE_CSS = f"""
/* ── Cardiac background image with dark overlay for readability ── */
[data-testid="stAppViewContainer"], [data-testid="stApp"] {{
    background-image:
        linear-gradient(rgba(6, 13, 31, 0.82), rgba(6, 13, 31, 0.82)),
        url("{_BG_URI}") !important;
    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
    background-repeat: no-repeat !important;
}}
""" if _BG_URI else ""

PREMIUM_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

/* ── Base dark background (fallback) ── */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {{
    font-family: 'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
    background: #060d1f !important;
    color: #e2e8f0 !important;
}}

{_BG_IMAGE_CSS}

/* Main content area – transparent so the background image shows through */
[data-testid="stAppViewContainer"] > .main,
.main, section.main {{
    background: transparent !important;
    padding: 0 !important;
}}

/* Block container */
[data-testid="block-container"] {{
    background: transparent !important;
    padding-top: 0 !important;
}}

/* ── Sidebar ── */
[data-testid="stSidebar"], [data-testid="stSidebar"] > div {{
    background: linear-gradient(180deg, #0d1b3e 0%, #112240 60%, #0a1628 100%) !important;
    border-right: 1px solid rgba(0, 212, 255, 0.18) !important;
    box-shadow: 4px 0 24px rgba(0, 212, 255, 0.08) !important;
}}

[data-testid="stSidebar"] * {{
    color: #cbd5e1 !important;
}}

[data-testid="stSidebar"] .stInfo,
[data-testid="stSidebar"] .stSuccess {{
    background: rgba(0, 212, 255, 0.08) !important;
    border: 1px solid rgba(0, 212, 255, 0.25) !important;
    color: #94d8fb !important;
    border-radius: 10px !important;
}}

/* ── Premium Header ── */
.premium-header {{
    background: linear-gradient(135deg, #0d1b3e 0%, #112240 40%, #0a2444 100%);
    padding: 60px 40px;
    text-align: center;
    margin-bottom: 40px;
    border-bottom: 2px solid rgba(0, 212, 255, 0.35);
    box-shadow: 0 8px 40px rgba(0, 212, 255, 0.18), 0 2px 0 rgba(0, 212, 255, 0.4);
    position: relative;
}}

.premium-header::after {{
    content: '';
    position: absolute;
    bottom: -2px;
    left: 10%;
    width: 80%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #00d4ff, #3b82f6, #00d4ff, transparent);
    filter: blur(1px);
}}

.premium-header h1 {{
    font-size: 3.5em;
    color: #ffffff;
    font-weight: 900;
    margin: 0;
    text-shadow: 0 0 30px rgba(0, 212, 255, 0.6), 0 4px 20px rgba(0, 0, 0, 0.5);
    letter-spacing: -1px;
    background: linear-gradient(135deg, #ffffff 0%, #00d4ff 60%, #3b82f6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}}

.premium-header p {{
    font-size: 1.3em;
    color: rgba(180, 220, 255, 0.9);
    margin-top: 15px;
    font-weight: 500;
    letter-spacing: 0.5px;
}}

/* ── Cards ── */
.card {{
    background: linear-gradient(145deg, #0d1b3e 0%, #112240 60%, #0a2444 100%);
    border-radius: 24px;
    padding: 40px;
    border: 1px solid rgba(0, 212, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}}

.card:hover {{
    transform: translateY(-5px);
    border-color: rgba(0, 212, 255, 0.45);
    box-shadow: 0 16px 60px rgba(0, 0, 0, 0.5);
}}

.card h2 {{
    color: #00d4ff;
    font-size: 1.8em;
    font-weight: 800;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 12px;
}}

.card .subtitle {{
    color: #7fa8c9;
    font-size: 0.95em;
    margin-bottom: 30px;
    font-weight: 500;
}}

/* ── Divider ── */
.divider {{
    height: 2px;
    background: linear-gradient(90deg, transparent, #00d4ff, #3b82f6, transparent);
    margin: 30px 0;
    border-radius: 10px;
    box-shadow: 0 0 8px rgba(0, 212, 255, 0.4);
}}

/* ── Risk Badges ── */
.risk-high {{
    background: linear-gradient(135deg, #1e0a0a 0%, #3b0f0f 100%);
    color: #fca5a5;
    padding: 25px;
    border-radius: 16px;
    font-size: 1.4em;
    font-weight: 800;
    text-align: center;
    margin: 20px 0;
    border: 1px solid rgba(239, 68, 68, 0.5);
    box-shadow: 0 8px 32px rgba(239, 68, 68, 0.25), 0 0 24px rgba(239, 68, 68, 0.15);
}}

.risk-moderate {{
    background: linear-gradient(135deg, #1f1200 0%, #3b1f00 100%);
    color: #fdba74;
    padding: 25px;
    border-radius: 16px;
    font-size: 1.4em;
    font-weight: 800;
    text-align: center;
    margin: 20px 0;
    border: 1px solid rgba(249, 115, 22, 0.5);
    box-shadow: 0 8px 32px rgba(249, 115, 22, 0.25), 0 0 24px rgba(249, 115, 22, 0.15);
}}

.risk-low {{
    background: linear-gradient(135deg, #031a0e 0%, #062d18 100%);
    color: #86efac;
    padding: 25px;
    border-radius: 16px;
    font-size: 1.4em;
    font-weight: 800;
    text-align: center;
    margin: 20px 0;
    border: 1px solid rgba(34, 197, 94, 0.5);
    box-shadow: 0 8px 32px rgba(34, 197, 94, 0.2), 0 0 24px rgba(34, 197, 94, 0.12);
}}

/* ── Insight Boxes ── */
.insight-box {{
    background: linear-gradient(145deg, #0a1e3d 0%, #0f2a50 100%);
    color: #e2e8f0;
    padding: 30px;
    border-radius: 16px;
    margin: 20px 0;
    border: 1px solid rgba(0, 212, 255, 0.3);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4),
                0 0 30px rgba(0, 212, 255, 0.12);
    transition: all 0.3s ease;
}}

.insight-box:hover {{
    transform: translateY(-5px);
    border-color: rgba(0, 212, 255, 0.55);
    box-shadow: 0 16px 48px rgba(0, 0, 0, 0.5),
                0 0 48px rgba(0, 212, 255, 0.22);
}}

.insight-box h4 {{
    color: #00d4ff;
    font-size: 1.2em;
    margin-bottom: 12px;
    font-weight: 800;
    text-shadow: 0 0 12px rgba(0, 212, 255, 0.5);
}}

.insight-box p {{
    font-size: 1.05em;
    line-height: 1.6;
    margin: 0;
    color: #cbd5e1;
}}

.insight-box-green {{
    border-color: rgba(52, 211, 153, 0.35);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4),
                0 0 30px rgba(52, 211, 153, 0.12);
}}

.insight-box-green:hover {{
    border-color: rgba(52, 211, 153, 0.6);
    box-shadow: 0 16px 48px rgba(0, 0, 0, 0.5),
                0 0 48px rgba(52, 211, 153, 0.22);
}}

.insight-box-green h4 {{
    color: #34d399;
    text-shadow: 0 0 12px rgba(52, 211, 153, 0.5);
}}

/* ── Streamlit widgets on dark background ── */
[data-testid="stWidgetLabel"] label,
.stSelectbox label, .stSlider label,
.stNumberInput label, .stRadio label,
.stCheckbox label {{
    color: #ffffff !important;
    font-weight: 600 !important;
}}

[data-testid="stSelectbox"] > div > div,
[data-testid="stNumberInput"] input,
[data-testid="stTextInput"] input {{
    background: #0d1b3e !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(0, 212, 255, 0.25) !important;
    border-radius: 10px !important;
}}

/* ── Primary Button ── */
.stButton > button {{
    width: 100% !important;
    background: linear-gradient(135deg, #0057b8 0%, #0284c7 50%, #00d4ff 100%) !important;
    color: #ffffff !important;
    font-weight: 800 !important;
    font-size: 1.1em !important;
    height: 60px !important;
    border-radius: 16px !important;
    border: 1px solid rgba(0, 212, 255, 0.5) !important;
    box-shadow: 0 8px 24px rgba(0, 132, 199, 0.5),
                inset 0 1px 0 rgba(255,255,255,0.1) !important;
    transition: all 0.3s ease !important;
    text-shadow: 0 1px 4px rgba(0,0,0,0.3) !important;
}}

.stButton > button:hover {{
    transform: translateY(-3px) !important;
    box-shadow: 0 14px 40px rgba(0, 132, 199, 0.65),
                inset 0 1px 0 rgba(255,255,255,0.15) !important;
}}

/* ── Download Button ── */
.stDownloadButton > button {{
    background: linear-gradient(135deg, #065f46 0%, #059669 60%, #34d399 100%) !important;
    color: #ffffff !important;
    width: 100% !important;
    border-radius: 16px !important;
    font-weight: 800 !important;
    font-size: 1.05em !important;
    height: 55px !important;
    border: 1px solid rgba(52, 211, 153, 0.45) !important;
    box-shadow: 0 8px 24px rgba(5, 150, 105, 0.45) !important;
    transition: all 0.3s ease !important;
}}

.stDownloadButton > button:hover {{
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 36px rgba(5, 150, 105, 0.6) !important;
}}

/* ── Download Button Icon – dark blue ── */
.stDownloadButton > button svg {{
    fill: #00008b !important;
    color: #00008b !important;
}}

/* ── Alerts ── */
.stInfo {{
    background: rgba(0, 100, 200, 0.12) !important;
    border: 1px solid rgba(0, 212, 255, 0.3) !important;
    border-radius: 12px !important;
    padding: 18px 24px !important;
    font-weight: 600 !important;
    color: #93c5fd !important;
}}

.stSuccess {{
    background: rgba(5, 150, 105, 0.12) !important;
    border: 1px solid rgba(52, 211, 153, 0.3) !important;
    border-radius: 12px !important;
    padding: 18px 24px !important;
    font-weight: 600 !important;
    color: #6ee7b7 !important;
}}

.stWarning {{
    background: rgba(180, 83, 9, 0.12) !important;
    border: 1px solid rgba(251, 146, 60, 0.35) !important;
    border-radius: 12px !important;
    padding: 18px 24px !important;
    font-weight: 600 !important;
    color: #fdba74 !important;
}}

.stError {{
    background: rgba(180, 20, 20, 0.12) !important;
    border: 1px solid rgba(239, 68, 68, 0.35) !important;
    border-radius: 12px !important;
    padding: 18px 24px !important;
    font-weight: 600 !important;
    color: #fca5a5 !important;
}}

/* ── Responsive ── */
@media (max-width: 768px) {{
    .premium-header h1 {{ font-size: 2.2em; }}
    .card {{ padding: 25px; }}
}}
</style>
"""