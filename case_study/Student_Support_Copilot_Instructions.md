# Student Support Copilot - Case Study Instructions

## Audience
IITM BS Bhubaneswar Meetup participants learning to use LLMs with Python.

## Overview
Build a small **AI copilot for student support** using a fictional program handbook, student support tickets, and Python + an LLM API.

## Why this case study?
- Covers **prompting**, **structured output**, **retrieval**, and **evaluation** in one project
- Feels real without requiring a large backend or complex framework

---

## Learning objectives

By the end, every learner should be able to:

1. Send a prompt from Python to an LLM
2. Request and parse structured JSON output
3. Retrieve relevant context from a document
4. Draft a response grounded in policy text
5. Decide when human escalation is safer than auto-resolution

---

## Dataset files

| File | Description |
|------|-------------|
| `data/program_handbook.md` | Fictional policy handbook (late penalties, regrading, refunds, exams, office hours, academic integrity, accessibility, etc.) |
| `data/student_support_tickets.jsonl` | Realistic student support tickets |
| `data/rag_questions.json` | Starter questions for the retrieval demo |

> All data is fictional and meant only for workshop use.

---

## Workflow for the session

### Part 1 — Warm-up (10-15 min)
```bash
python 01_basic_prompting.py
python 02_prompt_patterns.py
python 03_structured_output.py
```
Discuss: What changed when the prompt became more specific? Why is JSON output easier for programs to consume?

### Part 2 — Retrieval demo (15-20 min)
```bash
python 06_rag_simple.py
```
Discuss: Why does the handbook matter? How does retrieval reduce hallucination? Why is "answer only from context" useful but not perfect?

### Part 3 — Main build (35-45 min)
```bash
python 07_case_study_support_copilot.py
```

---

## Learner task

For each ticket, build a system that produces:

| Field | Type | Purpose |
|-------|------|---------|
| `category` | string | Classify the ticket |
| `priority` | low / medium / high | Triage urgency |
| `needs_human_review` | boolean | Flag sensitive cases |
| `policy_basis` | string | Cite the relevant handbook section |
| `draft_reply` | string | Student-facing response |

### What makes a good output?
- Polite and clear
- Cites the relevant policy
- Does **not** promise exceptions outside the handbook
- Escalates when misconduct, accessibility, or exceptional approval is involved

---

## Beginner track

Focus: Run scripts, read prompts, tweak inputs, observe what changes.

**Success criteria:**
- Made one successful LLM call
- Produced valid JSON output
- Answered one handbook question using retrieval

---

## Intermediate track

Focus: Extend the baseline — improve reliability, not just style.

**Suggested tasks:**
1. Tighten the prompt for shorter, more consistent replies
2. Add JSON validation after parsing
3. Attach chunk IDs or citations to answers
4. Compare two models on the same ticket
5. Add rules for automatic human-review flagging
6. Build a simple evaluation sheet for 5 tickets

**Success criteria:**
- Improved reliability (not just cosmetics)
- Can explain why retrieval matters
- Can identify failure modes

---

## Suggested categories

You may use categories like:
- quiz issue
- assignment issue
- regrading
- exam reschedule
- refund
- technical issue
- academic integrity
- accessibility/accommodation
- routine doubt
- certificate/completion

Students do not need to use exactly these labels, but labels should be consistent.

---

## Suggested priority rubric

| Priority | When to use |
|----------|-------------|
| **Low** | Routine question, no urgent loss or escalation risk |
| **Medium** | Deadline impact or important learner action required |
| **High** | Serious escalation, policy exception, academic integrity, accessibility, or missed exam with evidence |

---

## Discussion prompts (for facilitator)

- A polished answer that isn't in the handbook — is that a *good* answer?
- Should a bot handle academic integrity complaints automatically?
- When should an AI system stop and hand off to a human?
- What is the difference between memory (script 05) and retrieval (script 06)?

---

## Extension ideas

| Extension | What to do |
|-----------|------------|
| **A — Confidence** | Add a confidence score + reason for low confidence to the output |
| **B — Evaluation** | Create a gold set with expected category + escalation decisions |
| **C — Better retrieval** | Swap TF-IDF with embedding-based retrieval |
| **D — Frontend** | Wrap the system in Streamlit |

---

## Common failure modes

| Problem | Fix |
|---------|-----|
| **Hallucinated policy** | Force answers to cite retrieved text |
| **Overconfident promises** | Add "do not promise exceptions outside policy" to prompt |
| **Wrong routing** | Add human-review rules for sensitive cases |
| **Inconsistent JSON** | Validate and retry on parse failure |
| **Weak retrieval** | Tune chunk size and top-k |

---

## Team deliverables

Each team submits:
1. Updated Python code
2. One screenshot or terminal output
3. Two example tickets with outputs
4. A short note on one limitation of their solution

---

## Closing message

You didn't just "call an API." You combined **prompting, output design, retrieval, policy grounding, and decision-making** — that's what turns an LLM demo into a usable application.
