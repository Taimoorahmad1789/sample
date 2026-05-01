"""
Reusable UI components for Cardiac Risk Assessment App
"""
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
            f"<p style='text-align:center;color:#64748b;font-size:0.85em;font-weight:600;'>🏆 Cardiac Risk Assessment v{version}<br>AI-Powered Diagnostic Support</p>",
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


def display_risk_gauge(probability):
    """Display risk gauge chart."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=int(probability * 100),
        title={'text': "<b>Cardiac Risk Score</b>", 'font': {'size': 24, 'color': '#0284c7'}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 2, 'tickcolor': '#64748b'},
            'bar': {'color': "#dc2626" if probability > 0.7 else "#f97316" if probability > 0.3 else "#16a34a"},
            'steps': [
                {'range': [0, 30], 'color': "#f0fdf4"},
                {'range': [30, 70], 'color': "#fffbeb"},
                {'range': [70, 100], 'color': "#fef2f2"}
            ],
            'threshold': {'line': {'color': "#dc2626", 'width': 5}, 'value': 70}
        },
        number={'font': {'size': 50, 'color': '#0284c7', 'family': 'Arial Black'}}
    ))
    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,0)",
        font={'family': "Inter, sans-serif", 'color': "#1e293b", 'size': 14},
        height=420,
        margin=dict(l=20, r=20, t=80, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)


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
    <div style='background: linear-gradient(135deg, rgba(6, 182, 212, 0.05) 0%, rgba(3, 139, 180, 0.05) 100%); 
                border: 2px dashed #0ea5e9; border-radius: 16px; padding: 40px; text-align: center;'>
        <h3 style='color: #0284c7; margin-bottom: 10px;'>👈 Ready for Analysis</h3>
        <p style='color: #64748b; font-size: 1.05em;'>Fill in the patient data and click "Generate Diagnostic Report".</p>
    </div>
    """, unsafe_allow_html=True)