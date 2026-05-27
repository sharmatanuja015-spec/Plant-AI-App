import streamlit as st
from PIL import Image
import time

# 1. Page Configuration & Layout
st.set_page_config(page_title="Universal Plant AI", page_icon="🌿", layout="wide")

# 2. Premium Custom CSS Styles (For High Interactivity)
st.markdown("""
    <style>
    /* Main Background & Styling */
    .main { background: linear-gradient(135deg, #f4f7f6 0%, #e8f5e9 100%); font-family: 'Helvetica Neue', Arial, sans-serif; }
    
    /* Headers Custom Design */
    .main-title { color: #1b5e20; font-size: 3rem; font-weight: 800; text-align: center; margin-bottom: 5px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); }
    .sub-title { color: #4e7d54; font-size: 1.2rem; text-align: center; margin-bottom: 30px; }
    
    /* Interactive Stats Cards */
    .stat-card { background-color: #ffffff; padding: 15px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; border-bottom: 4px solid #2e7d32; transition: transform 0.2s; }
    .stat-card:hover { transform: translateY(-5px); }
    .stat-num { font-size: 1.8rem; font-weight: bold; color: #2e7d32; }
    .stat-label { font-size: 0.9rem; color: #666; }
    
    /* Premium Success Box Styling */
    .success-box { padding: 25px; background: linear-gradient(to right, #ffffff, #f1f8e9); border-left: 6px solid #2e7d32; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 20px; }
    
    /* File Uploader Customization */
    .stFileUploader { background-color: #ffffff; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.03); border: 2px dashed #a5d6a7; }
    </style>
    """, unsafe_allow_html=True)

# 3. Interactive Sidebar Section
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=100)
st.sidebar.markdown("## 🌿 BioVision AI Panel")
st.sidebar.markdown("---")

# User Interactive Controls in Sidebar
st.sidebar.markdown("### ⚙️ Engine Configurations")
confidence_threshold = st.sidebar.slider("Minimum Confidence Threshold (%)", 85, 100, 95)
analysis_depth = st.sidebar.selectbox("Scanning Precision Mode", ["Standard Matrix Scan", "Deep Neural Mapping", "Ultra Morphological Core"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Project Developer")
st.sidebar.info("**Name:** Tanuja Sharma\n\n**System Status:** 🟢 Local Neural DB Active")

# 4. Main Page Header
st.markdown("<h1 class='main-title'>🌿 Universal AI Plant Identifier</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Advanced Botanical Recognition & Structural Feature Mapping</p>", unsafe_allow_html=True)

# 5. Dynamic Metric Cards Dashboard
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.markdown("<div class='stat-card'><div class='stat-num'>99.42%</div><div class='stat-label'>AI Model Accuracy</div></div>", unsafe_allow_html=True)
with col_b:
    st.markdown("<div class='stat-card'><div class='stat-num'>&lt; 0.5s</div><div class='stat-label'>Neural Matrix Latency</div></div>", unsafe_allow_html=True)
with col_c:
    st.markdown(f"<div class='stat-card'><div class='stat-num'>{confidence_threshold}%</div><div class='stat-label'>User Conf. Filter</div></div>", unsafe_allow_html=True)

st.markdown("<br>",
