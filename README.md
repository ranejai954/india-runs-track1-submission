# INDIA RUNS - Track 01: Data & AI Challenge

## My Ranking System

Built a rule-based ranker that scores 100,000 candidates against Redrob's AI Engineering JD.

### Scoring Components
- Title match (30%)
- Company quality (20%) 
- Skills relevance (25%)
- Experience years (15%)
- Education tier (10%)
- Behavioral signals (30% of final)

### Anti-Trap Measures
- Penalizes consulting backgrounds (TCS, Infosys, Wipro)
- Detects keyword stuffing
- Honeypot identification

### How to Run

```bash
python ranker_nuclear.py
python validate_submission.py submission_FINAL_SUBMIT.csv