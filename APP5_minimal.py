import streamlit as st
import os

# Set page configuration
st.set_page_config(
    page_title="Gastric Cancer Prediction - Minimal Test",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Gastric Cancer Prediction - Minimal Test")

# Debug: List all files
st.subheader("📁 Available Files")
try:
    files = os.listdir('.')
    st.write("Files in current directory:", files)
    
    # Check for model files
    model_files = [f for f in files if f.endswith('.pkl')]
    st.write("Model files found:", model_files)
    
except Exception as e:
    st.error(f"Error listing files: {e}")

# Simple test
st.subheader("✅ Basic Functionality Test")
st.success("If you can see this message, the app is working!")

# Test basic Streamlit components
st.subheader("🧪 Component Tests")
st.button("Test Button")
st.slider("Test Slider", 0, 100, 50)
st.selectbox("Test Selectbox", ["Option 1", "Option 2", "Option 3"])

st.subheader("🔧 System Information")
st.write(f"Streamlit version: {st.__version__}")
st.write(f"Current working directory: {os.getcwd()}")
st.write(f"Python executable: {os.sys.executable}")

# Test if we can import other packages
st.subheader("📦 Package Import Test")
try:
    import numpy as np
    st.success("✅ NumPy imported successfully")
    st.write(f"NumPy version: {np.__version__}")
except Exception as e:
    st.error(f"❌ NumPy import failed: {e}")

try:
    import pandas as pd
    st.success("✅ Pandas imported successfully")
    st.write(f"Pandas version: {pd.__version__}")
except Exception as e:
    st.error(f"❌ Pandas import failed: {e}")

try:
    import joblib
    st.success("✅ Joblib imported successfully")
    st.write(f"Joblib version: {joblib.__version__}")
except Exception as e:
    st.error(f"❌ Joblib import failed: {e}")

st.subheader("🎯 Next Steps")
st.info("If all tests pass, we can gradually add more functionality.")
