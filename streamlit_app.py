# streamlit_app.py
# Smart Q&A Bot — Streamlit UI
# Run: streamlit run streamlit_app.py

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Smart Q&A Bot",
    page_icon="🤖",
    layout="centered"
)

# ── Personas ──────────────────────────────────────────────────────────────────
PERSONAS = {
    "🧑‍🏫 Mentor": {
        "temperature": 0.7,
        "system_prompt": "You are a patient and knowledgeable AI mentor. Explain concepts clearly with real-world examples. Encourage curiosity and guide the learner step by step. Always end your response with a follow-up question to deepen understanding.",
    },
    "😎 Chill Friend": {
        "temperature": 0.9,
        "system_prompt": "You are a super chill, knowledgeable friend who answers questions in a casual and fun tone. Use simple language, be conversational, and avoid corporate or overly formal language. Keep it real.",
    },
    "📊 Data Analyst": {
        "temperature": 0.3,
        "system_prompt": "You are a precise data analyst. Always give structured, factual answers. Use numbered points and bullet points. Be concise and professional. Quantify things whenever possible.",
    },
    "🏛️ Socratic Teacher": {
        "temperature": 0.8,
        "system_prompt": "You are a Socratic teacher. Instead of directly answering, respond with thoughtful counter-questions that guide the user to discover the answer themselves. Only give direct answers when the user seems truly stuck.",
    },
    "🔥 Hype Coach": {
        "temperature": 1.0,
        "system_prompt": "You are an EXTREMELY enthusiastic hype coach and knowledge expert! Answer every question with massive energy, use CAPS for emphasis, add relevant emojis, and make learning feel absolutely EPIC. Nothing is impossible!",
    },
}

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🤖 Smart Q&A Bot")
st.caption("Project · OpenAI Direct API · LangChain")
st.divider()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")

    import os
    from dotenv import load_dotenv
    import streamlit as st

    load_dotenv()

    # Works locally (.env) AND on Streamlit Cloud (secrets)
    api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", "")

    st.divider()

    persona_name = st.selectbox(
        "🎭 Bot Personality",
        options=list(PERSONAS.keys())
    )

    persona = PERSONAS[persona_name]

    st.info(f"**Temperature:** {persona['temperature']}")

    with st.expander("📋 System Prompt"):
        st.write(persona["system_prompt"])

    st.divider()

    if st.button("🔄 Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    # Stats
    if "total_tokens" not in st.session_state:
        st.session_state.total_tokens = 0

    st.metric("Tokens Used", st.session_state.total_tokens)

# ── Chat History Init ─────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_persona" not in st.session_state:
    st.session_state.last_persona = persona_name

# Reset history if persona changed
if st.session_state.last_persona != persona_name:
    st.session_state.messages = []
    st.session_state.last_persona = persona_name
    st.toast(f"Switched to {persona_name}. Chat cleared!", icon="🔄")

# ── Display Chat History ──────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ── Chat Input ────────────────────────────────────────────────────────────────
user_input = st.chat_input("Ask anything...")

if user_input:
    if not api_key:
        st.error("❌ API key not found. Please check your .env file.")
        st.stop()

    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    # Save to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Build LangChain messages
    lc_messages = [SystemMessage(content=persona["system_prompt"])]
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            lc_messages.append(HumanMessage(content=msg["content"]))
        else:
            lc_messages.append(AIMessage(content=msg["content"]))

    # Call OpenAI
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                llm = ChatOpenAI(
                    model="gpt-3.5-turbo",
                    temperature=persona["temperature"],
                    openai_api_key=api_key,
                    max_tokens=600,
                )
                response = llm.invoke(lc_messages)
                reply = response.content

                st.write(reply)

                # Save bot reply
                st.session_state.messages.append({"role": "assistant", "content": reply})

                # Token tracking
                if hasattr(response, "response_metadata"):
                    tokens = response.response_metadata.get("token_usage", {}).get("total_tokens", 0)
                    st.session_state.total_tokens += tokens

            except Exception as e:
                st.error(f"❌ Error: {e}")