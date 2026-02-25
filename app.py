import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import norm
import os
import time
from datetime import datetime
import uuid

# =================================================================
# 🛡️ [1] INSTITUTIONAL FRAMEWORK & CONSTANTS
# =================================================================
st.set_page_config(
    page_title="Capgemini Invent | Sovereign Intelligence v16.0",
    page_icon="⚜️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Principal Architect Global Constants
OPTIMIZATION_ALPHA = 0.1425  
CONFIDENCE_LEVEL = 0.99      
SYSTEM_VERSION = "16.0.4-SOVEREIGN"
BASE_REVENUE = 150000000 
LOGO_URL = "https://upload.wikimedia.org/wikipedia/commons/9/9d/Capgemini_2017_logo.svg"

# =================================================================
# 🧬 [2] THE SOVEREIGN KERNEL (QUANTITATIVE ENGINE)
# =================================================================
class SovereignKernel:
    """The mathematical heart of the system."""
    @staticmethod
    def calculate_pareto_front(profits, sustainability):
        points = np.vstack((profits, sustainability)).T
        pareto_front = []
        for i, p in enumerate(points):
            if not any((points[:, 0] >= p[0]) & (points[:, 1] >= p[1]) & (np.arange(len(points)) != i)):
                pareto_front.append(p)
        return np.array(sorted(pareto_front, key=lambda x: x[0]))

    @staticmethod
    def compute_var(entropy_val, shock_factor=1.0):
        mu = BASE_REVENUE
        sigma = mu * entropy_val * shock_factor
        return mu + (norm.ppf(1 - CONFIDENCE_LEVEL) * sigma)

    @staticmethod
    def generate_risk_matrix():
        return np.random.randint(1, 10, size=(5, 5))

# =================================================================
# 🛰️ [3] ROBUST BOOTSTRAP ENGINE (FIXED STATE INITIALIZATION)
# =================================================================
def bootstrap_system():
    """Guaranteeing all session keys exist to prevent AttributeErrors."""
    initial_state = {
        'instance_id': str(uuid.uuid4())[:8],
        'is_optimized': False,
        'shock_factor': 1.0,
        'active_scenario': "Nominal Operations",
        'logs': [f"[{datetime.now().strftime('%H:%M:%S')}] System Bootstrapped."],
        'drift_level': 0.0012,
        'last_rebalance': "N/A"
    }
    for key, value in initial_state.items():
        if key not in st.session_state:
            st.session_state[key] = value

bootstrap_system()

def log_event(msg):
    st.session_state.logs.insert(0, f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

# =================================================================
# 🎨 [4] THE "CAPGEMINI MIDNIGHT" DESIGN SYSTEM
# =================================================================
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;700&display=swap');
    .stApp {{ background-color: #000D1A; color: #F2F4F7; font-family: 'Space Grotesk', sans-serif; }}
    
    /* Executive Header Styling */
    .top-bar {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 0px; border-bottom: 1px solid rgba(0, 112, 173, 0.3);
        margin-bottom: 30px;
    }}
    .glitch-header {{
        font-size: 2.8rem; font-weight: 700;
        background: linear-gradient(90deg, #00d4ff, #FFFFFF, #0070AD);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}
    
    /* Bento-Box Metrics */
    [data-testid="stMetric"] {{
        background: rgba(0, 112, 173, 0.1);
        border: 1px solid rgba(0, 112, 173, 0.4);
        border-left: 6px solid #0070AD;
        padding: 20px !important; border-radius: 4px;
    }}
    
    /* Sidebar Sophistication */
    [data-testid="stSidebar"] {{ background-color: #00050A; border-right: 1px solid #003087; }}
    
    .audit-log {{ font-family: 'Courier New', monospace; font-size: 0.85rem; color: #00d4ff; }}
    .stress-alert {{
        background: rgba(255, 75, 75, 0.15); border: 1px solid #FF4B4B;
        padding: 15px; border-radius: 4px; margin: 10px 0px;
    }}
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 🎮 [5] SIDEBAR CONTROL PLANE (WITH LOGO)
# =================================================================
with st.sidebar:
    st.image("asserts/7cb5dfa2786c33a3411f252313aeefb3.jpg", width=180) # --- SIDEBAR LOGO ---
    st.markdown("### 🛰️ Operational Control")
    
    scenario_options = ["Nominal Operations", "Suez Canal Blockade", "Tier-1 Cyber Attack", "Regional Conflict"]
    selected_scenario = st.selectbox("Trigger Stress Scenario", scenario_options)
    
    scenario_weights = {"Nominal Operations": 1.0, "Suez Canal Blockade": 2.8, "Tier-1 Cyber Attack": 4.2, "Regional Conflict": 7.0}
    
    if st.button("🚀 INJECT SYSTEMIC SHOCK"):
        st.session_state.shock_factor = scenario_weights[selected_scenario]
        st.session_state.active_scenario = selected_scenario
        st.session_state.is_optimized = False 
        log_event(f"SHOCK INJECTED: {selected_scenario}")
        st.rerun()

    st.divider()
    entropy_choice = st.select_slider("Systemic Entropy", ["Stable", "Unstable", "Chaotic"])
    e_val = {"Stable": 0.05, "Unstable": 0.15, "Chaotic": 0.40}[entropy_choice]
    
    if st.button("Purge Neural State"):
        st.session_state.clear()
        st.rerun()

# =================================================================
# 🏢 [6] EXECUTIVE MISSION CONTROL (WITH TOP LOGO)
# =================================================================

# --- TOP HEADER BAR ---
with st.container():
    col_header, col_logo = st.columns([4, 1])
    with col_header:
        st.markdown("<h1 class='glitch-header'>NEURAL SOVEREIGNTY</h1>", unsafe_allow_html=True)
        st.caption(f"Instance: {st.session_state.instance_id} | v{SYSTEM_VERSION} | Scenario: {st.session_state.active_scenario}")
    with col_logo:
        st.image("asserts/7cb5dfa2786c33a3411f252313aeefb3.jpg", width=180) # --- TOP MAIN LOGO ---

st.divider()

# --- CALCULATION LOGIC ---
raw_var = SovereignKernel.compute_var(e_val, st.session_state.shock_factor)
if st.session_state.is_optimized:
    savings = abs(raw_var) * OPTIMIZATION_ALPHA
    display_var = raw_var + savings
else:
    savings = 0.0
    display_var = raw_var

# --- KPI LAYER ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("NETWORK GMV", f"${BASE_REVENUE/1e6:.1f}M", "STABLE")
m2.metric("99% VaR EXPOSURE", f"${abs(display_var/1e6):.1f}M", 
          delta=f"-${savings/1e6:.1f}M Saved" if st.session_state.is_optimized else f"x{st.session_state.shock_factor} Shock",
          delta_color="inverse" if not st.session_state.is_optimized else "normal")
m3.metric("ESG RESILIENCE", "96.2/100", "-14% CO2")
m4.metric("SYSTEM DRIFT", f"{st.session_state.drift_level}", "Optimal")

if st.session_state.shock_factor > 1.0:
    st.markdown(f"<div class='stress-alert'>🚨 <b>CRITICAL EVENT:</b> {st.session_state.active_scenario} active. VaR Threshold expanded.</div>", unsafe_allow_html=True)

# --- ANALYTICS BENTO BOX ---
tab_risk, tab_math, tab_agents = st.tabs(["🌐 RISK TOPOLOGY", "📈 STOCHASTIC MATH", "🤖 AGENTIC BOARDROOM"])

with tab_risk:
    c_map, c_matrix = st.columns([2, 1])
    with c_map:
        st.markdown("#### Digital Twin Node Resilience")
        
        map_df = pd.DataFrame({
            'lat': [20, 30, 15, 25, 12], 'lon': [75, 70, 77, 85, 80],
            'risk': [85, 45, 15, 95, 5] if st.session_state.shock_factor > 1 else [10, 5, 2, 8, 1]
        })
        fig_map = px.scatter_mapbox(map_df, lat="lat", lon="lon", size="risk", color="risk",
                                    color_continuous_scale="Reds", zoom=3.2, height=450, mapbox_style="carto-darkmatter")
        fig_map.update_layout(margin=dict(l=0,r=0,t=0,b=0))
        st.plotly_chart(fig_map, use_container_width=True)
    
    with c_matrix:
        st.markdown("#### Impact vs Likelihood")
        
        matrix = SovereignKernel.generate_risk_matrix()
        fig_heat = px.imshow(matrix, labels=dict(x="Impact", y="Likelihood"),
                             x=['Minor', 'Mod', 'Major', 'Crit', 'Fatal'],
                             y=['Rare', 'Unlikely', 'Possible', 'Likely', 'Frequent'],
                             color_continuous_scale="YlOrRd")
        fig_heat.update_layout(height=400, margin=dict(l=0,r=0,t=0,b=0))
        st.plotly_chart(fig_heat, use_container_width=True)

with tab_math:
    col_v, col_p = st.columns(2)
    with col_v:
        st.markdown("#### Probabilistic VaR Distribution")
        
        x = np.linspace(BASE_REVENUE*0.3, BASE_REVENUE*1.7, 250)
        y = norm.pdf(x, BASE_REVENUE, BASE_REVENUE * e_val * st.session_state.shock_factor)
        fig_v = go.Figure()
        fig_v.add_trace(go.Scatter(x=x, y=y, fill='tozeroy', name='Revenue Density', line=dict(color='#0070AD')))
        fig_v.add_vline(x=display_var, line_dash="dash", line_color="red", annotation_text="VaR Limit")
        fig_v.update_layout(template="plotly_dark", height=400)
        st.plotly_chart(fig_v, use_container_width=True)
    
    with col_p:
        st.markdown("#### Pareto Frontier: ESG vs Profit")
        
        prof = np.random.normal(100, 20, 300); esg = np.random.normal(100, 20, 300)
        front = SovereignKernel.calculate_pareto_front(prof, esg)
        fig_pf = go.Figure()
        fig_pf.add_trace(go.Scatter(x=prof, y=esg, mode='markers', opacity=0.3, marker=dict(color='grey')))
        fig_pf.add_trace(go.Scatter(x=front[:,0], y=front[:,1], mode='lines+markers', line=dict(color='#00d4ff')))
        fig_pf.update_layout(template="plotly_dark", height=400, xaxis_title="Profitability", yaxis_title="Sustainability")
        st.plotly_chart(fig_pf, use_container_width=True)

with tab_agents:
    st.markdown("#### Nash Equilibrium Strategy Consensus")
    
    a1, a2 = st.columns(2)
    a1.chat_message("finance", avatar="💹").write(f"Alert: VaR expanded by {((st.session_state.shock_factor-1)*100):.0f}%. Liquidity buffer required.")
    a2.chat_message("ops", avatar="🚛").write("Suez blockade confirmed. Shifting to Air-Rail intermodal via Node_Singapore.")
    
    if st.button("⚖️ EXECUTE ANTI-FRAGILE REBALANCE"):
        with st.status("Solving Nash Equilibrium..."):
            time.sleep(2)
            st.session_state.is_optimized = True
            st.session_state.last_rebalance = datetime.now().strftime("%H:%M:%S")
            log_event(f"SUCCESS: System optimized for {st.session_state.active_scenario}")
        st.rerun()

# --- FOOTER & AUDIT ---
st.divider()
col_l, col_r = st.columns(2)
with col_l:
    st.markdown("#### 🧬 System Audit Trail")
    st.markdown(f"<div class='audit-log'>{'<br>'.join(st.session_state.logs[:10])}</div>", unsafe_allow_html=True)

with col_r:
    st.markdown("#### 📥 Sovereign Strategic Brief")
    memo = f"""
CAPGEMINI INVENT | STRATEGIC ANALYSIS
------------------------------------
SCENARIO: {st.session_state.active_scenario}
MAGNITUDE: {st.session_state.shock_factor}x
STATUS: {"✅ RESILIENT" if st.session_state.is_optimized else "⚠️ EXPOSED"}
MITIGATED CAPITAL: ${savings:,.2f}
REBALANCE TIME: {st.session_state.last_rebalance}

DIRECTIVE: { "Resilience protocols active. System has absorbed the shock." if st.session_state.is_optimized else "ACTION REQUIRED: Perform rebalance immediately." }
------------------------------------
    """
    st.code(memo, language="markdown")
    st.download_button("Download Strategy Report", data=memo, file_name="Sovereign_Brief.txt")


st.markdown("<center style='color: #0070AD; padding: 30px;'>Capgemini Invent | Get The Future You Want | Institutional Visionary v16.0</center>", unsafe_allow_html=True)



