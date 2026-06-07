# 🚀 INDIA RUNS - Track 01: Data & AI Challenge

> A high-performance candidate ranking system designed to evaluate and prioritize **100,000+ profiles** against Redrob's AI Engineering Job Description using a custom rule-based scoring engine.

---

## 📌 Project Overview

This project was developed as part of the **INDIA RUNS – Track 01: Data & AI Challenge**.

The objective was to build an intelligent ranking system capable of identifying the most suitable candidates from a large talent pool by analyzing professional background, technical skills, education, experience, and behavioral indicators.

---

## 🎯 Ranking Methodology

Each candidate is assigned a composite score based on multiple weighted factors:

| Criteria             | Weight |
| -------------------- | ------ |
| 🎓 Education Tier    | 10%    |
| 💼 Experience Years  | 15%    |
| 🛠️ Skills Relevance | 25%    |
| 🏢 Company Quality   | 20%    |
| 📋 Job Title Match   | 30%    |

### 🧠 Behavioral Intelligence Layer

An additional behavioral scoring layer contributes up to **30% of the final ranking score**, helping identify stronger candidates beyond keyword matching.

---

## 1. 🔍 Anti-Gaming & Quality Controls

To improve ranking quality and reduce false positives, the system includes several defensive mechanisms:

### 2. 🛡️ Consulting Background Detection

Profiles heavily associated with mass-service consulting organizations are appropriately weighted based on challenge requirements.

### 3. 🚨 Keyword Stuffing Detection

Identifies profiles that artificially inflate relevance through excessive keyword repetition.

### 4. 🍯 Honeypot Candidate Identification

Detects suspicious or low-quality profiles that may bypass traditional matching systems.

### 5. 📊 Signal-Based Evaluation

Uses multiple indicators rather than relying solely on skill keywords.

---

## ⚙️ Technical Highlights

* Processes **100,000+ candidate profiles**
* Weighted multi-factor scoring engine
* Rule-based explainable ranking system
* Data validation and submission verification
* Scalable and lightweight architecture

---

## 📂 Project Structure

```text
.
├── ranker_complete.py
├── validate_submission.py
├── submission_READY.csv
└── README.md
```

---

## 🚀 Getting Started

### 1. Run the Ranking Engine

```bash
python ranker_complete.py
```

### 2. Validate the Final Submission

```bash
python validate_submission.py submission_READY.csv
```

---

## 📈 Features

✅ Multi-factor candidate evaluation

✅ Behavioral signal analysis

✅ Explainable scoring methodology

✅ Anti-manipulation safeguards

✅ Large-scale profile processing

✅ Automated submission validation

---

## 🏆 Challenge Goal

Build a robust Candidate Ranking Framework capable of identifying top AI Engineering talent while minimizing ranking bias, profile manipulation, and low-quality matches.

---

## 👨‍💻 Author

**Jai Rane**

**Participant in INDIA RUNS Hackathon Track 01: The Data & AI Challenge**

**Passionate about AI, Cybersecurity, Data Science, and Full Stack Development.**
