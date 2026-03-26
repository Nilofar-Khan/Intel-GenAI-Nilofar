# IntelGen AI: 5-Minute Log Triage

*The problem:* Engineers spend ~2 hours manually parsing 10,000+ lines of firmware logs to find a root cause.
*The Solution:* An automated triage tool powered by *Qwen3-8B* that identifies Hardware, Config, and Script errors in under 5 minutes.

### Tech Stack
- *Model:* Qwen3-8B (Self-hosted on EC2)
- *UI:* Streamlit
- *Infrastructure:* Docker & AWS EC2
- *Domain:* Intel CSME, FSP, and Servod Firmware Validation

### How to Run
1. Ensure Qwen3 is running on the host (Ollama/vLLM).
2. docker build -t intel-triage .
3. docker run -p 8501:8501 --add-host=host.docker.internal:host-gateway intel-triage.

<br>

| **Task** | **Manual Triage** | **IntelGen AI Triage** |
| :--- | :--- | :--- |
| **Log Scanning** | 45-60 Minutes (Reading text) | 10 Seconds (Automated Regex) |
| **Root Cause ID** | 30-60 Minutes (Searching Wiki/Docs) | 2 Minutes (Qwen3-8B Analysis) |
| **Fix Generation** | 15 Minutes (Drafting fix) | 30 Seconds (AI Recommendation) |
| **Total Time** | **~2 Hours** | **< 5 Minutes** |