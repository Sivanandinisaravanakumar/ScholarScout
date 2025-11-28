# ScholarScout – Scholarship Discovery & Eligibility Agent

## 1. Problem Statement
Many students miss out on scholarships because:
- Information is scattered across multiple websites,
- Eligibility rules are confusing,
- Students lack awareness or guidance,
- Manual searching takes time,
- Deadlines and documents are hard to track.

**ScholarScout** solves this problem by acting as an intelligent Scholarship Discovery Agent that:
- Collects scholarship opportunities,
- Matches them with a student’s profile,
- Checks eligibility,
- Generates personalized application plans.

Its goal is to make scholarship discovery accessible to all students.

---

## 2. Why Agents?
Scholarship matching is a multi-step workflow that requires:
- Searching for opportunities,
- Analyzing eligibility,
- Prioritizing deadlines,
- Planning documentation.

A single LLM prompt is not enough.

Agents allow:
- Modular workflow,
- Parallel task execution,
- Context-aware decisions,
- Persistent memory of profiles,
- Reusable execution state,
- Clean separation between tools and logic.

---

## 3. Architecture Overview
ScholarScout uses a **multi-agent architecture**:

### 1. Profile Agent  
Stores and retrieves student profile details using session-based memory.

### 2. Discovery Agent  
Uses a custom tool (`ScholarshipSearchTool`) to fetch scholarships.

### 3. Eligibility Agent  
Checks if the student meets scholarship criteria using `EligibilityTool`.

### 4. Planning Agent  
Builds an application checklist using `ApplicationPlanTool`.

### 5. Orchestrator Agent (main agent)
Runs agents sequentially and merges results.

---

## 4. Tools Used
Custom tools implemented:
- `ScholarshipSearchTool`
- `EligibilityTool`
- `ApplicationPlanTool`

These simulate external database calls and workflow tools.

---

## 5. Project Flow
1. Input student profile  
2. Store profile in memory  
3. Search for matching scholarships  
4. Evaluate eligibility  
5. Generate application plan  
6. Return structured final output  

---

## 6. Technologies Used
- Python  
- Custom tool functions  
- Basic agent orchestration (Sequential)  
- Minimal dependency environment

---

## 7. If I Had More Time
- Add real API-based scholarship search  
- Add Memory Bank for long-term history  
- Add ranking system based on priority  
- Integrate Google Search / MCP tools  
- Deploy on Vertex AI or Cloud Run  
- Create a web UI

---

## 8. Output Example
{
"profile": {...},
"discovered": {...},
"eligibility": {...},
"plans": {...}
}