**LOG-GUARD AI:AUTONOMOUS TRiage for Fimware CI/CD**
​Log-Guard AI is a GenAI-powered triage assistant designed to accelerate the debugging of hardware-in-the-loop (HIL) testing failures. 
By leveraging the OPEA framework and Qwen2.5, it reduces the time to analyze complex firmware logs (CSME, FSP, Servod) from 2 hours to under 5 minutes.
**​Key Value Proposition**
​​**Triage Acceleration:** Automates the "needle in a haystack" search for root causes in multi-gigabyte build logs.
​**Cost Reduction:** Prevents expensive Intel Xeon/Gaudi compute hours from being wasted on re-running tests doomed by persistent hardware hangs.
**​Actionable Insights: ** Doesn't just report failure; it suggests recovery steps (e.g., "Reset Servod on Port 9999").
**​Technical Architecture**
​This project is built using the OPEA (Open Platform for Enterprise AI) microservices architecture, optimized for Intel hardware.
​LLM: Qwen2.5-7B-Instruct (optimized via OpenVINO).
​Vector Database: Redis/Milvus (storing historical "Known-Error" patterns).
​Framework: OPEA ChatQnA / GenAIComps.
​Compute: Intel® Xeon® Scalable Processors.
