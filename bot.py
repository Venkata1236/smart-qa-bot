# bot.py
# Core Q&A Bot logic — Direct API calls via LangChain + OpenAI
# Concepts covered: system prompts, temperature tuning, token management, conversation history

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from personas import PERSONAS


class QABot:
    def __init__(self, persona_key: str, api_key: str):
        """
        Initialize the bot with a chosen persona.
        
        Args:
            persona_key: Key from PERSONAS dict (e.g. "1", "2")
            api_key: OpenAI API key
        """
        self.persona = PERSONAS[persona_key]
        self.conversation_history = []  # Stores full chat history for multi-turn memory
        self.total_tokens_used = 0

        # LangChain's ChatOpenAI — wraps OpenAI API with temperature control
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=self.persona["temperature"],  # Controls randomness
            openai_api_key=api_key,
            max_tokens=600,
        )

        print(f"\n{self.persona['emoji']}  Bot initialized as: {self.persona['name']}")
        print(f"📌 Temperature: {self.persona['temperature']}")
        print(f"📋 System Prompt: {self.persona['system_prompt'][:80]}...")

    def chat(self, user_input: str) -> str:
        """
        Send a message and get a response.
        Maintains conversation history for multi-turn context.

        Args:
            user_input: The user's question

        Returns:
            Bot's reply as a string
        """
        # Add user message to history
        self.conversation_history.append(HumanMessage(content=user_input))

        # Build full message list: system prompt + entire conversation history
        messages = [
            SystemMessage(content=self.persona["system_prompt"])
        ] + self.conversation_history

        # Make the API call
        response = self.llm.invoke(messages)

        # Extract reply text
        reply = response.content

        # Save bot reply to history (for next turn's context)
        self.conversation_history.append(AIMessage(content=reply))

        # Track token usage from response metadata
        if hasattr(response, "response_metadata"):
            token_info = response.response_metadata.get("token_usage", {})
            self.total_tokens_used += token_info.get("total_tokens", 0)

        return reply

    def reset(self):
        """Clear conversation history to start fresh."""
        self.conversation_history = []
        print("\n🔄 Conversation history cleared.")

    def show_stats(self):
        """Display session statistics."""
        print(f"\n📊 Session Stats:")
        print(f"   Messages exchanged : {len(self.conversation_history)}")
        print(f"   Total tokens used  : {self.total_tokens_used}")
        print(f"   Persona            : {self.persona['name']}")
        print(f"   Temperature        : {self.persona['temperature']}")
