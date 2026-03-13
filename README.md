# 🤖 Smart Q&A Bot — Day 1 Project
**Concepts:** Direct API calls · System Prompts · Temperature Tuning · Token Management

---

## 📁 Project Structure
```
smart_qa_bot/
├── app.py            ← Main entry point (run this)
├── bot.py            ← Core bot logic (LangChain + OpenAI)
├── personas.py       ← All 5 bot personalities defined here
├── .env              ← Your API key goes here (never share this!)
├── requirements.txt  ← Python dependencies
└── README.md
```

---

## ⚙️ Setup & Run

**Step 1 — Install dependencies:**
```bash
pip install -r requirements.txt
```

**Step 2 — Add your OpenAI API key in `.env`:**
```
OPENAI_API_KEY=sk-your-actual-key-here
```

**Step 3 — Run the bot:**
```bash
python app.py
```

---

## 💬 Commands Inside the Chat
| Command  | Action                        |
|----------|-------------------------------|
| `reset`  | Clear conversation history    |
| `stats`  | Show tokens used & session info |
| `switch` | Change to a different persona |
| `quit`   | Exit the bot                  |

---

## 🧠 Day 1 Concepts in This Code

| Concept | Where in Code |
|---|---|
| Direct API Call | `bot.py` → `self.llm.invoke(messages)` |
| System Prompt | `bot.py` → `SystemMessage(content=...)` |
| Temperature Tuning | `bot.py` → `ChatOpenAI(temperature=...)` |
| Token Management | `bot.py` → `self.total_tokens_used` |
| Conversation History | `bot.py` → `self.conversation_history` list |
| Custom Personality | `personas.py` → `PERSONAS` dict |
