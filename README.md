# 🚀 INDIA RUNS — Track 01: Data & AI Challenge

> **Nuclear Option candidate ranking engine targeting Redrob's AI Engineer mandate.** > Processes, scores, and optimally sorts 100,000+ profiles with exact mathematical tie-breaking precision.

---

## 📊 Evaluation Architecture

The scoring core evaluates candidates via dual pipelines combining job description positioning (70%) alongside active behavioral engagement markers (30%).

### ⚙️ Scoring Weight Matrix

┌──────────────────────────────────────────────────────────┐
│              CORE JD MATCHING ENGINE (70%)               │
├───────────────┬──────────────────┬───────────┬───────────┤
│ Title Match   │ Company Quality  │ Skills    │ Exp/Edu   │
│ 30%           │ 20%              │ 25%       │ 15% / 10% │
└───────────────┴──────────────────┴───────────┴───────────┘
│
▼
┌──────────────────────────────────────────────────────────┐
│              BEHAVIORAL ENGAGEMENT (30%)                 │
├──────────────────────────────────────────────────────────┤
│ Response rate, platform activity, notice period limits  │
└──────────────────────────────────────────────────────────┘


* **🎯 Role Identification (30%):** Strict structural grading for targeted titles (`Vector Search`, `LLM`, `Applied ML`, `NLP`).
* **💡 Core Tech Capabilities (25%):** Weighted search coverage on embeddings, vector indexing (`FAISS`, `Pinecone`), and modern indexing heuristics.
* **🏢 Placement Background (20%):** Higher grading for proven technology footprints, down-weighting service/consulting layers.
* **⏳ Seniority Index (15%):** Premium scaling curve focused squarely on the optimal 5–9 years experience horizon.
* **🎓 Academic Tiering (10%):** Strict matrix processing across Tier-1, Tier-2, and Tier-3 credentials.

---

## 🛡️ Anti-Manipulation & Structural Safety

The platform integrates deep telemetry checks designed to expose artificial profile optimization:

* **🚫 Service Footprint Filter:** Automated penalty layers targeting mass consulting platforms (*TCS, Infosys, Wipro, Cognizant*).
* **📉 Keyword Stuffing Throttles:** Activates an aggressive score reduction multiplier whenever skill arrays cross the 20+ count threshold.
* **🪤 Honeypot Assertions:** Instant 90% score drop for candidate entities claiming "Expert" status while exposing fraudulent zero-month duration values.

---

## 🏃 Run & Validate Execution Trace

The engine uses standard Python decimal-base numeric formatting (`Decimal`) to guarantee true mathematical sorting without floating-point precision slippage. 

Follow this two-step validation pipeline to execute the ranker and confirm compliance against the tournament testing harness:

### 1. Execute Ranking System
```bash
python ranker_nuclear.py
2. Verify Output Schema & Constraints
Bash
python validate_submission.py submission_FINAL_SUBMIT.csv
