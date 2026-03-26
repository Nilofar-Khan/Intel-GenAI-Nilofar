import streamlit as st
import pandas as pd
import json
import requests
from utils import filter_logs

# Configuration for Qwen3-8B on EC2
MODEL_URL = "http://host.docker.internal:11434/api/generate" 

st.set_page_config(page_title="IntelGen AI: Triage", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'home'

def query_qwen3(log_data):
    """Sends expert-context prompt to Qwen3-8B"""
    prompt = f"""
    [Expert Context: Intel Firmware/DevOps]
    Analyze these log snippets. Classify as HARDWARE, CONFIGURATION, or SCRIPT.
    Identify the specific fault in CSME, FSP, or Servod if present.
    
    Logs:
    {log_data}
    
    Return ONLY a JSON array of objects:
    [{"category": "...", "root_cause": "...", "fix": "..."}]
    """
    payload = {"model": "qwen3:8b", "prompt": prompt, "stream": False, "format": "json"}
    try:
        response = requests.post(MODEL_URL, json=payload, timeout=30)
        return json.loads(response.json()['response'])
    except:
        return [{"category": "Error", "root_cause": "Model Timeout", "fix": "Check EC2 Connection"}]

# --- Home Page ---
if st.session_state.page == 'home':
    st.title("🤖 IntelGen AI Log Triage")
    st.markdown("### Reduce analysis from 2 hours to 5 minutes.")
    
    file = st.file_uploader("Upload Log File", type=['log', 'txt'])
    if file:
        if st.button("Start AI Analysis"):
            with st.spinner("Qwen3-8B is triaging..."):
                raw_content = file.read().decode("utf-8")
                # Pre-filter to save tokens/time
                important_logs = filter_logs(raw_content)
                st.session_state.results = query_qwen3(important_logs)
                st.session_state.page = 'results'
                st.rerun()

# --- Results Page ---
elif st.session_state.page == 'results':
    st.title("📊 Analysis Results")
    if st.button("⬅ Upload New Log"):
        st.session_state.page = 'home'
        st.rerun()
    
    df = pd.DataFrame(st.session_state.results)
    st.table(df) # The requested tabulation