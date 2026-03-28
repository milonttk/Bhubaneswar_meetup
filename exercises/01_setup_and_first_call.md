# Exercise 1 - Setup and First API Call

## Goal
Make your first successful LLM call from Python.

## Steps

1. **Create and activate a virtual environment**
   - Mac/Linux: `python -m venv .venv && source .venv/bin/activate`
   - Windows PowerShell: `python -m venv .venv` then `.venv\Scripts\Activate.ps1`

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get a free API key from Groq** (no credit card needed)
   - Go to [console.groq.com](https://console.groq.com) and sign up (Google/GitHub login works)
   - Click **API Keys** in the left sidebar → **Create API Key**
   - Copy the key (starts with `gsk_`)

4. **Create your `.env` file**
   ```bash
   cp .env.example .env
   ```
   Open `.env` and replace the bottom section with:
   ```
   OPENAI_API_KEY=gsk_paste_your_groq_key_here
   OPENAI_BASE_URL=https://api.groq.com/openai/v1
   MODEL=llama-3.3-70b-versatile
   TEMPERATURE=0.2
   ```

5. **Run your first script**
   ```bash
   python 01_basic_prompting.py
   ```
   You should see the LLM's response in your terminal.

## Try changing
- Ask for 1 line instead of 3 bullet points
- Change the audience from beginner to expert
- Ask for an analogy using cricket or food

## Reflection
- What changed when your prompt became more specific?
- Which part of the prompt controlled style vs content?
