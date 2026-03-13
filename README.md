# 🤖 Smart Q&A Bot

> A multi-personality AI chatbot powered by OpenAI and LangChain

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.3.7-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--turbo-orange)

---

## 📌 What Is This?

A multi-personality Q&A chatbot built using direct OpenAI API calls and LangChain. Switch between 5 different bot personalities, each with a unique system prompt and temperature setting.

---

## 🗺️ Simple Flow — What Happens When You Ask a Question

```
        You type a question
      (terminal or browser)
               │
               ▼
        Pick a personality
      (mentor, hype coach…)
               │
               ▼
        Build the message
   [personality + history + question]
               │
               ▼
        Send to OpenAI
      (gpt-3.5-turbo processes it)
               │
               ▼
        Reply shown to you
     (saved to memory for next turn)
               │
               └─────────────── loop ◄─┘
```

---

## 🏗️ Detailed Architecture — Which File Does What

```
                        ┌──────────────┐
                        │     User     │
                        └──────┬───────┘
                               │
              ┌────────────────┴──────────────────┐
              │                                   │
     ┌────────▼────────┐                ┌─────────▼─────────┐
     │    app.py       │                │  streamlit_app.py  │
     │ [INTERFACE]     │                │   [INTERFACE]      │
     │ terminal        │                │   browser          │
     │ input()·print() │                │   st.chat_input()  │
     └────────┬────────┘                └─────────┬──────────┘
              │                                   │
              └──────────────┬────────────────────┘
                             │
                  ┌──────────▼──────────┐
                  │       bot.py        │
                  │    [CORE LOGIC]     │
                  │  QABot class        │
                  │  ChatOpenAI         │
                  │  invoke()           │
                  │  history tracking   │
                  └───┬─────────────┬───┘
                      │             │
          ┌───────────▼──┐     ┌────▼──────────────┐
          │ personas.py  │     │      .env          │
          │  [CONFIG]    │     │    [SECRETS]       │
          │ system_prompt│     │  OPENAI_API_KEY    │
          │ temperature  │     │  loaded by dotenv  │
          └──────────────┘     └────────────────────┘
                      │
           ┌──────────▼──────────┐
           │    OpenAI API       │
           │   [EXTERNAL]        │
           │  gpt-3.5-turbo      │
           │  returns reply      │
           └─────────────────────┘

  ┌───────────────────────────────────────┐
  │         requirements.txt             │
  │   installs all libraries above       │
  └───────────────────────────────────────┘

Legend:
  [INTERFACE]  →  app.py, streamlit_app.py
  [CORE LOGIC] →  bot.py
  [CONFIG]     →  personas.py
  [SECRETS]    →  .env
  [EXTERNAL]   →  OpenAI API (cloud)
```

---

## 🎭 5 Bot Personalities

| # | Persona | Temperature | Style |
|---|---|---|---|
| 1 | 🧑‍🏫 Mentor | 0.7 | Patient, step-by-step, asks follow-up questions |
| 2 | 😎 Chill Friend | 0.9 | Casual, fun, no corporate speak |
| 3 | 📊 Data Analyst | 0.3 | Precise, structured, numbered answers |
| 4 | 🏛️ Socratic Teacher | 0.8 | Answers questions with questions |
| 5 | 🔥 Hype Coach | 1.0 | MAX energy, CAPS, emojis, ultra motivating |

---

## 📁 Project Structure

```
smart_qa_bot/
├── streamlit_app.py   ← Streamlit UI (deploy this)
├── app.py             ← Terminal version
├── bot.py             ← Core bot logic — LangChain + OpenAI
├── personas.py        ← All 5 personalities defined here
├── .env               ← Your API key (never push to GitHub!)
├── .gitignore         ← Tells Git to ignore .env
├── requirements.txt   ← Python dependencies
└── README.md
```

---

## ⚙️ Local Setup

**Step 1 — Clone the repo:**
```bash
git clone https://github.com/YOUR_USERNAME/smart-qa-bot.git
cd smart-qa-bot
```

**Step 2 — Install dependencies:**
```bash
pip install -r requirements.txt
```

**Step 3 — Add your OpenAI API key in `.env`:**
```
OPENAI_API_KEY=sk-your-actual-key-here
```

**Step 4 — Run:**

Streamlit UI:
```bash
python -m streamlit run streamlit_app.py
```

Terminal version:
```bash
python app.py
```

---

## 🚀 Deploy on Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repo → select `streamlit_app.py`
4. Go to Settings → Secrets → add:
```toml
OPENAI_API_KEY = "sk-your-key-here"
```
5. Click Deploy → get your live public URL ✅

---

## 💬 Terminal Commands

| Command | Action |
|---|---|
| `reset` | Clear conversation history |
| `stats` | Show tokens used and session info |
| `switch` | Change to a different persona |
| `quit` | Exit |

---

## 📦 Tech Stack

- **OpenAI** — GPT-3.5-turbo via direct API calls
- **LangChain** — Chat model wrapper, message schema
- **Streamlit** — Web UI
- **python-dotenv** — API key management

---

## 👤 Author

**Venkata Reddy Bommavaram**
- 📧 bommavaramvenkat2003@gmail.com
- 💼 [LinkedIn](https://linkedin.com/in/venkatareddy1203)
- 🐙 [GitHub](https://github.com/venkata1236)
