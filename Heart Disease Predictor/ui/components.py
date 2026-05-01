"""
Reusable UI components for Cardiac Risk Assessment App
"""
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from config import RISK_HIGH_THRESHOLD, RISK_MODERATE_THRESHOLD


def show_header(app_title, app_subtitle):
    """Display premium header."""
    st.markdown(f"""
    <div class='premium-header'>
        <h1>{app_title}</h1>
        <p>{app_subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def show_sidebar_info(version):
    """Display sidebar information."""
    with st.sidebar:
        st.markdown("### 👨‍⚕️ Patient Information")
        st.info("📝 Fill the patient details in the main panel to get AI-based cardiac risk assessment.")

        st.markdown("---")
        st.markdown("### 💡 Health Tips")
        st.success("✅ Maintain a healthy, balanced diet")
        st.success("✅ Exercise regularly (30 mins daily)")
        st.success("✅ Monitor BP & cholesterol levels")
        st.success("✅ Avoid smoking & excessive alcohol")
        st.success("✅ Manage stress effectively")

        st.markdown("---")
        st.markdown(
            f"<p style='text-align:center;color:#4a7a9b;font-size:0.85em;font-weight:600;'>🏆 Cardiac Risk Assessment v{version}<br>AI-Powered Diagnostic Support</p>",
            unsafe_allow_html=True)


def show_input_card_header():
    """Display input card header."""
    st.markdown("""
    <div class='card'>
        <h2>📋 Patient Clinical Data</h2>
        <p class='subtitle'>Enter accurate patient details for best prediction accuracy</p>
    </div>
    """, unsafe_allow_html=True)


def show_results_card_header():
    """Display results card header."""
    st.markdown("""
    <div class='card'>
        <h2>🔍 Diagnostic Analysis</h2>
        <p class='subtitle'>Click to generate comprehensive AI-powered diagnostic report</p>
    </div>
    """, unsafe_allow_html=True)


def show_divider():
    """Display input divider."""
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)


def display_risk_distribution_chart(probability):
    """Display risk distribution curve with colored bands and a right-side info card."""
    score = int(probability * 100)

    # Determine risk category and styling
    if probability > 0.85:
        risk_label = "Very High Risk"
        risk_color = "#ef4444"
        emoji = "🛑"
        percentile = min(99, 90 + int((score - 85) / 15 * 9))
        description = "Critical cardiac risk level identified."
        action = "Immediate cardiologist consultation strongly recommended."
    elif probability > RISK_HIGH_THRESHOLD:
        risk_label = "High Risk"
        risk_color = "#f97316"
        emoji = "🔶"
        percentile = 75 + int((score - 70) / 15 * 15)
        description = "Significant cardiac risk factors detected."
        action = "Close monitoring and medical consultation required."
    elif probability > RISK_MODERATE_THRESHOLD:
        risk_label = "Moderate Risk"
        risk_color = "#f59e0b"
        emoji = "⚠️"
        percentile = 35 + int((score - 30) / 40 * 40)
        description = "Some cardiac risk factors are present."
        action = "Regular medical checkups and lifestyle modifications recommended."
    else:
        risk_label = "Low Risk"
        risk_color = "#22c55e"
        emoji = "✅"
        percentile = int((score / 30) * 35) if score > 0 else 0
        description = "Patient appears to be in good cardiac health."
        action = "Maintain current lifestyle and periodic checkups."

    # Build bell-curve distribution (mu=45, sigma=20), peak normalised to 1
    x = np.linspace(0, 100, 600)
    mu, sigma = 45, 20
    y = np.exp(-0.5 * ((x - mu) / sigma) ** 2)

    # Risk band definitions: (start, end, fill_color, legend_label)
    bands = [
        (0,  30,  "rgba(34,197,94,0.28)",  "Low"),
        (30, 70,  "rgba(245,158,11,0.22)", "Moderate"),
        (70, 85,  "rgba(249,115,22,0.28)", "High"),
        (85, 100, "rgba(239,68,68,0.30)",  "Very High"),
    ]
    band_label_info = [
        (15,   "Low",       "#22c55e"),
        (50,   "Moderate",  "#f59e0b"),
        (77.5, "High",      "#f97316"),
        (92.5, "Very High", "#ef4444"),
    ]

    fig = go.Figure()

    # Coloured band fills
    for x_start, x_end, fill_color, label in bands:
        mask = (x >= x_start) & (x <= x_end)
        xb, yb = x[mask], y[mask]
        if len(xb) > 1:
            fig.add_trace(go.Scatter(
                x=np.concatenate([[xb[0]], xb, [xb[-1]]]),
                y=np.concatenate([[0], yb, [0]]),
                fill='toself',
                fillcolor=fill_color,
                line=dict(width=0),
                name=label,
                showlegend=True,
                hoverinfo='skip',
            ))

    # Main bell-curve line
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        line=dict(color='#00d4ff', width=2.5),
        showlegend=False,
        hoverinfo='skip',
    ))

    # Dashed vertical line at user's score
    fig.add_trace(go.Scatter(
        x=[score, score],
        y=[0, 1.18],
        mode='lines',
        line=dict(color=risk_color, width=2.5, dash='dash'),
        name=f'Score: {score}',
        showlegend=True,
    ))

    # Diamond marker on the curve at user's score
    y_at_score = np.exp(-0.5 * ((score - mu) / sigma) ** 2)
    fig.add_trace(go.Scatter(
        x=[score],
        y=[y_at_score],
        mode='markers+text',
        marker=dict(size=14, color=risk_color, symbol='diamond',
                    line=dict(color='white', width=1.5)),
        text=[f'  {score}'],
        textposition='middle right',
        textfont=dict(color=risk_color, size=13, family='Arial Black'),
        showlegend=False,
        hovertemplate=f'Score: {score}<extra></extra>',
    ))

    # Band labels below x-axis
    for bx, blabel, bcolor in band_label_info:
        fig.add_annotation(
            x=bx, y=-0.14,
            text=f"<b>{blabel}</b>",
            showarrow=False,
            font=dict(color=bcolor, size=10),
            xref='x', yref='paper',
        )

    fig.update_layout(
        title=dict(
            text="<b>Cardiac Risk Distribution Curve</b>",
            font=dict(size=18, color='#00d4ff'),
            x=0.5, xanchor='center',
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.55)",
        font=dict(family="Inter, sans-serif", color="#e2e8f0", size=12),
        height=360,
        margin=dict(l=40, r=20, t=60, b=55),
        xaxis=dict(
            range=[0, 100],
            title=dict(text="Risk Score", font=dict(color='#94a3b8')),
            tickfont=dict(color='#94a3b8'),
            tickvals=[0, 30, 70, 85, 100],
            gridcolor='rgba(71,85,105,0.3)',
            showgrid=True,
            zeroline=False,
        ),
        yaxis=dict(
            range=[0, 1.25],
            showticklabels=False,
            title=dict(text="Population Density", font=dict(color='#94a3b8')),
            gridcolor='rgba(71,85,105,0.3)',
            showgrid=True,
            zeroline=False,
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom", y=1.02,
            xanchor="right", x=1,
            font=dict(color='#e2e8f0', size=11),
            bgcolor='rgba(0,0,0,0)',
        ),
    )

    # Render chart + info card side by side
    chart_col, card_col = st.columns([3, 1])

    with chart_col:
        st.plotly_chart(fig, use_container_width=True)

    with card_col:
        top_pct = 100 - percentile
        st.markdown(f"""
        <div style='background: linear-gradient(160deg, rgba(5,15,35,0.96) 0%, rgba(10,20,50,0.96) 100%);
                    border: 1.5px solid {risk_color}66;
                    border-radius: 16px;
                    padding: 22px 14px;
                    margin-top: 18px;
                    box-shadow: 0 0 28px {risk_color}33, inset 0 0 30px rgba(0,0,0,0.3);
                    text-align: center;'>
            <div style='font-size: 2.2em; margin-bottom: 8px;'>{emoji}</div>
            <h4 style='color: {risk_color}; margin: 0 0 10px 0; font-size: 1em; letter-spacing: 0.5px;'>{risk_label}</h4>
            <div style='margin-bottom: 14px;'>
                <span style='font-size: 2.8em; font-weight: 900; color: {risk_color};'>{score}</span>
                <span style='color: #64748b; font-size: 0.9em;'>&nbsp;/ 100</span>
            </div>
            <div style='background: rgba(255,255,255,0.04); border-radius: 10px; padding: 8px 10px; margin-bottom: 14px;'>
                <p style='color: #64748b; font-size: 0.7em; margin: 0; text-transform: uppercase; letter-spacing: 1px;'>Percentile</p>
                <p style='color: #e2e8f0; font-size: 1.05em; font-weight: 700; margin: 4px 0 0 0;'>Top {top_pct}%</p>
            </div>
            <p style='color: #cbd5e1; font-size: 0.8em; margin-bottom: 8px; line-height: 1.5;'>{description}</p>
            <p style='color: #64748b; font-size: 0.75em; font-style: italic; margin: 0; line-height: 1.4;'>{action}</p>
        </div>
        """, unsafe_allow_html=True)


def display_risk_status(probability):
    """Display risk status badge and message."""
    if probability > RISK_HIGH_THRESHOLD:
        st.markdown("<div class='risk-high'>🛑 HIGH RISK - IMMEDIATE ACTION REQUIRED</div>", unsafe_allow_html=True)
        st.error("⚠️ **URGENT:** Immediate consultation with a cardiologist is strongly recommended.")
    elif probability > RISK_MODERATE_THRESHOLD:
        st.markdown("<div class='risk-moderate'>⚠️ MODERATE RISK - CLOSE MONITORING NEEDED</div>", unsafe_allow_html=True)
        st.warning("💡 Regular medical checkups and preventive lifestyle modifications are recommended.")
    else:
        st.markdown("<div class='risk-low'>✅ LOW RISK - GOOD HEALTH STATUS</div>", unsafe_allow_html=True)
        st.success("🌟 Patient appears to be in good cardiac health. Maintain current lifestyle and periodic checkups.")


def display_insights(top_positive, top_negative):
    """Display AI insights boxes."""
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown(f"""
        <div class='insight-box'>
            <h4>🔴 Major Risk Factor</h4>
            <p><strong>{top_positive.replace('_', ' ').title()}</strong></p>
            <p style='font-size:0.9em; margin-top:10px; opacity:0.9;'>Focus on monitoring and management.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown(f"""
        <div class='insight-box insight-box-green'>
            <h4>🟢 Protective Factor</h4>
            <p><strong>{top_negative.replace('_', ' ').title()}</strong></p>
            <p style='font-size:0.9em; margin-top:10px; opacity:0.9;'>Continue maintaining this aspect.</p>
        </div>
        """, unsafe_allow_html=True)


def show_ready_state():
    """Display ready state message."""
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(0,212,255,0.06) 0%, rgba(59,130,246,0.06) 100%);
                border: 2px dashed rgba(0,212,255,0.4); border-radius: 16px; padding: 40px; text-align: center;'>
        <h3 style='color: #00d4ff; margin-bottom: 10px; text-shadow: 0 0 14px rgba(0,212,255,0.5);'>👈 Ready for Analysis</h3>
        <p style='color: #7fa8c9; font-size: 1.05em;'>Fill in the patient data and click "Generate Diagnostic Report".</p>
    </div>
    """, unsafe_allow_html=True)