#!/usr/bin/env python3
"""
INDIA RUNS - Track 01: Data & AI Challenge
NUCLEAR OPTION - Scores first, then sorts safely for validate_submission.py
"""

import json
import csv
from datetime import datetime, date
from decimal import Decimal, ROUND_HALF_UP

CONSULTING_COMPANIES = {
    "tcs", "infosys", "wipro", "cognizant", "accenture", "capgemini",
    "tech mahindra", "hcl", "mindtree", "lti", "mphasis"
}

PRODUCT_COMPANIES = {
    "swiggy", "zomato", "uber", "ola", "razorpay", "cred", "flipkart",
    "amazon", "google", "microsoft", "meta", "redrob"
}

TARGET_TITLES = {
    "recommendation systems", "recommendation", "ranking", "search",
    "nlp engineer", "nlp", "machine learning", "ml engineer",
    "applied ml", "ai engineer", "llm", "retrieval", "vector search"
}

CORE_SKILLS = {
    "embeddings", "sentence transformers", "vector search", "faiss",
    "pinecone", "qdrant", "weaviate", "milvus", "opensearch",
    "elasticsearch", "bm25", "information retrieval", "ranking",
    "learning to rank", "reranking", "hybrid search"
}

def is_consulting_company(company):
    if not company:
        return False
    company_lower = company.lower()
    for bad in CONSULTING_COMPANIES:
        if bad in company_lower:
            return True
    return False

def is_product_company(company):
    if not company:
        return False
    company_lower = company.lower()
    for good in PRODUCT_COMPANIES:
        if good in company_lower:
            return True
    return False

def title_match_score(title):
    if not title:
        return Decimal('0.0')
    title_lower = title.lower()
    for target in TARGET_TITLES:
        if target in title_lower:
            return Decimal('1.0')
    if any(word in title_lower for word in ["ml", "ai", "data scientist"]):
        return Decimal('0.7')
    if "engineer" in title_lower and any(skill in title_lower for skill in ["search", "ranking", "recommend"]):
        return Decimal('0.8')
    return Decimal('0.2')

def skills_score(skills):
    if not skills:
        return Decimal('0.0')
    core_skill_count = 0
    total_skills = len(skills)
    for skill in skills:
        skill_name = skill.get("name", "").lower()
        proficiency = skill.get("proficiency", "")
        duration = skill.get("duration_months", 0)
        endorsements = skill.get("endorsements", 0)
        for core in CORE_SKILLS:
            if core in skill_name:
                if proficiency == "expert" and endorsements > 10 and duration > 12:
                    core_skill_count += 2
                elif proficiency in ["advanced", "expert"]:
                    core_skill_count += 1
                break
    stuffing_penalty = Decimal('1.0')
    if total_skills > 20:
        stuffing_penalty = Decimal('0.5')
    raw_score = min(Decimal('1.0'), Decimal(core_skill_count) / Decimal('5.0'))
    return raw_score * stuffing_penalty

def career_history_score(career_history):
    if not career_history:
        return Decimal('0.0')
    score = Decimal('0.0')
    product_roles = 0
    consulting_roles = 0
    total_roles = len(career_history)
    for role in career_history:
        company = role.get("company", "")
        title = role.get("title", "")
        if is_product_company(company):
            product_roles += 1
            if title_match_score(title) > Decimal('0.5'):
                score += Decimal('0.3')
            else:
                score += Decimal('0.2')
        elif is_consulting_company(company):
            consulting_roles += 1
            score -= Decimal('0.15')
    if total_roles > 0:
        score = max(Decimal('0'), min(Decimal('1.0'), score + (Decimal(product_roles) / Decimal(total_roles)) * Decimal('0.5')))
    if consulting_roles == total_roles and total_roles > 0:
        score *= Decimal('0.2')
    return score

def experience_score(years):
    if 5 <= years <= 9:
        return Decimal('1.0')
    elif 3 <= years < 5:
        return Decimal('0.7')
    elif 9 < years <= 12:
        return Decimal('0.6')
    elif years < 3:
        return Decimal('0.3')
    else:
        return Decimal('0.4')

def education_score(education):
    if not education:
        return Decimal('0.3')
    score = Decimal('0.0')
    for edu in education:
        tier = edu.get("tier", "").lower()
        if tier == "tier_1":
            score = max(score, Decimal('1.0'))
        elif tier == "tier_2":
            score = max(score, Decimal('0.8'))
        elif tier == "tier_3":
            score = max(score, Decimal('0.5'))
        else:
            score = max(score, Decimal('0.3'))
    return score

def behavioral_score(signals):
    if not signals:
        return Decimal('0.3')
    score = Decimal('0.0')
    response_rate = Decimal(str(signals.get("recruiter_response_rate", 0)))
    score += response_rate * Decimal('0.25')
    if signals.get("open_to_work_flag", False):
        score += Decimal('0.15')
    saved = min(Decimal('1.0'), Decimal(str(signals.get("saved_by_recruiters_30d", 0))) / Decimal('20'))
    score += saved * Decimal('0.15')
    interview_rate = Decimal(str(signals.get("interview_completion_rate", 0)))
    score += interview_rate * Decimal('0.15')
    notice = signals.get("notice_period_days", 90)
    if notice <= 30:
        score += Decimal('0.15')
    elif notice <= 60:
        score += Decimal('0.1')
    elif notice <= 90:
        score += Decimal('0.05')
    last_active = signals.get("last_active_date", "")
    if last_active:
        try:
            last_date = datetime.strptime(last_active, "%Y-%m-%d").date()
            today = date.today()
            days_ago = (today - last_date).days
            if days_ago < 7:
                score += Decimal('0.1')
            elif days_ago < 30:
                score += Decimal('0.05')
            elif days_ago > 180:
                score -= Decimal('0.1')
        except:
            pass
    return min(Decimal('1.0'), max(Decimal('0.0'), score))

def rank_candidate(candidate):
    profile = candidate.get("profile", {})
    career = candidate.get("career_history", [])
    skills = candidate.get("skills", [])
    education = candidate.get("education", [])
    signals = candidate.get("redrob_signals", {})
    
    title = profile.get("current_title", "")
    title_sc = title_match_score(title)
    
    company = profile.get("current_company", "")
    if is_consulting_company(company):
        company_sc = Decimal('0.2')
    elif is_product_company(company):
        company_sc = Decimal('1.0')
    else:
        company_sc = Decimal('0.5')
    
    skills_sc = skills_score(skills)
    career_sc = career_history_score(career)
    exp_sc = experience_score(profile.get("years_of_experience", 0))
    edu_sc = education_score(education)
    behavior_sc = behavioral_score(signals)
    
    jd_match = (title_sc * Decimal('0.30') + company_sc * Decimal('0.20') + skills_sc * Decimal('0.25') + exp_sc * Decimal('0.15') + edu_sc * Decimal('0.10'))
    final_score = (jd_match * Decimal('0.70')) + (behavior_sc * Decimal('0.30'))
    
    impossible_skills = 0
    for skill in skills:
        if skill.get("proficiency") == "expert" and skill.get("duration_months", 0) == 0:
            impossible_skills += 1
    if impossible_skills > 3:
        final_score *= Decimal('0.1')
    
    return {
        "candidate_id": candidate.get("candidate_id"),
        "score": final_score,
        "title": title,
        "company": company,
        "years": profile.get("years_of_experience", 0),
        "response_rate": signals.get("recruiter_response_rate", 0)
    }

def main():
    data_file = "candidates.jsonl"
    output_file = "submission_READY.csv"
    
    # EXPLICIT TERMINAL PRINT LOGS ADDED HERE:
    print("=" * 60)
    print("INDIA RUNS - Track 01: Data & AI Challenge")
    print("Candidate Ranking System - Scores first, then sorts safely for 'validate_submission.py'")
    print("=" * 60)
    
    print(f"📂 Loading candidates...")
    candidates = []
    with open(data_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                candidates.append(json.loads(line))
    print(f"✅ Loaded {len(candidates)} candidates")
    
    print(f"\n📊 Scoring...")
    scored = []
    for i, cand in enumerate(candidates):
        if i % 10000 == 0:
            print(f"  {i}/{len(candidates)}...")
        result = rank_candidate(cand)
        
        # ROUND SCORE TO 4 DECIMALS EXPLICITLY USING DECIMAL
        result["score"] = result["score"].quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
        scored.append(result)
    
    print(f"\n🔧 Sorting...")
    # CRITICAL TIE-BREAKER: Sort score descending, then raw string candidate_id ascending!
    scored.sort(key=lambda x: (-x["score"], x["candidate_id"]))
    
    top_100 = scored[:100]
    
    print(f"\n💾 Writing CSV to {output_file}...")
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["candidate_id", "rank", "score", "reasoning"])
        for rank, cand in enumerate(top_100, 1):
            reasoning = f"{cand['title']} at {cand['company']} with {cand['years']} yrs exp; response rate {cand['response_rate']:.2f}"
            writer.writerow([cand["candidate_id"], rank, cand["score"], reasoning])
    
    print(f"✅ Generated file matches strict rules. Ready for validation utility script.")
    print(f"Run this script --> python validate_submission.py submission_READY.csv")

if __name__ == "__main__":
    main()
