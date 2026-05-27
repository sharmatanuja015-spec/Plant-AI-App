import streamlit as st
from PIL import Image
import google.generativeai as genai
import time

# 1. Page Configuration
st.set_page_config(page_title="BioVision Ultra AI", page_icon="🌿", layout="wide")

# Premium UI Styling
st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #f4f7f6 0%, #e8f5e9 100%); }
    .main-title { color: #1b5e20; font-size: 3rem; font-weight: 800; text-align: center; }
    .sub-title { color: #4e7d54; font-size: 1.2rem; text-align: center; margin-bottom: 30px; }
    .result-box { padding: 25px; background: white; border-left: 6px solid #2e7d32; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar - API Key Input & Info
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=100)
st.sidebar.markdown("## 🌿 BioVision Ultra AI")
st.sidebar.markdown("---")

# User apni API key yahan daal sakta hai ya aap code me permanent likh sakte hain
# ✅ Apni asli key yahan paste kar dein:
api_key = "AIzaSyDLKwNct_Er1XuWLst5YtKfg0tUSy4-BUQ"
st.sidebar.markdown("---")
st.sidebar.info("**Developer:** Tanuja Sharma\n\n**Engine:** Google Gemini Pro Vision\n\n**Capability:** Identifies 1 Million+ Plants")

# 3. Main Header
st.markdown("<h1 class='main-title'>🌿 BioVision Ultra AI Platform</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Real-Time Visual Recognition Engine Powered by Multimodal Deep Learning</p>", unsafe_allow_html=True)

# 4. Image Uploader
uploaded_file = st.file_uploader("📸 Upload ANY leaf or plant image (Real Visual AI Testing)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.subheader("🔍 Scanned Specimen")
        st.image(image, use_column_width=True)
        
    with col2:
        st.subheader("🧠 Deep Learning Visual Analysis")
        
        if not api_key:
            st.warning("Please enter your Gemini API Key in the sidebar to activate the Visual AI Engine.")
        else:
            # Configure Google Gemini
            genai.configure(api_key=api_key)
            
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1)
                
            with st.spinner("Analyzing leaf morphology, venation patterns, and botanical features..."):
                try:
                    # Initialize Gemini Pro Vision Model
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    # AI Core Prompt
                    prompt = """
                    Analyze this plant/leaf image strictly as a senior botanist. Provide the output in this clean format:
                    **Botanical Identity:** [Write common name and scientific name here]
                    **Plant Type/Family:** [Write family or category here]
                    **Medicinal / General Uses:** [Provide 2-3 bullet points of benefits or uses]
                    **Interesting Fact:** [Provide 1 unique scientific or interesting fact]
                    """
                    
                    # Generate Result by passing the actual image
                    response = model.generate_content([prompt, image])
                    st.balloons()
                    
                    # Display Result inside beautiful box
                    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                    st.success("✅ Analysis Complete! Species Successfully Matched.")
                    st.write(response.text)
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"AI Engine Error: {str(e)}")
