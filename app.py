# app.py
# Main entry point — runs the Smart Q&A Bot in your terminal
# Project: OpenAI API Mastery

import os
from dotenv import load_dotenv
from personas import PERSONAS
from bot import QABot

# ── Load API key from .env file ──────────────────────────────────────────────
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    print("❌ ERROR: Please set your OPENAI_API_KEY in the .env file.")
    exit(1)


def show_personas():
    """Print available personas for the user to choose from."""
    print("\n" + "=" * 50)
    print("       🤖  SMART Q&A BOT Project")
    print("=" * 50)
    print("\nChoose a Bot Personality:\n")
    for key, persona in PERSONAS.items():
        print(f"  [{key}] {persona['emoji']}  {persona['name']:<18} — {persona['description']}")
    print()


def get_persona_choice() -> str:
    """Prompt user to pick a persona."""
    while True:
        choice = input("Enter choice (1-5): ").strip()
        if choice in PERSONAS:
            return choice
        print("❌ Invalid choice. Enter a number between 1 and 5.")


def main():
    show_personas()
    choice = get_persona_choice()

    bot = QABot(persona_key=choice, api_key=API_KEY)

    print("\n" + "-" * 50)
    print("💬 Chat started! Commands:")
    print("   'reset'  → Clear conversation history")
    print("   'stats'  → Show token usage & session info")
    print("   'switch' → Change persona")
    print("   'quit'   → Exit")
    print("-" * 50 + "\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            # ── Special commands ─────────────────────────────────────────────
            if user_input.lower() == "quit":
                bot.show_stats()
                print("\n👋 Bye!")
                break

            elif user_input.lower() == "reset":
                bot.reset()
                continue

            elif user_input.lower() == "stats":
                bot.show_stats()
                continue

            elif user_input.lower() == "switch":
                show_personas()
                new_choice = get_persona_choice()
                bot = QABot(persona_key=new_choice, api_key=API_KEY)
                print("\n" + "-" * 50)
                continue

            # ── Normal chat ──────────────────────────────────────────────────
            print(f"\n{bot.persona['emoji']} Bot: ", end="", flush=True)
            reply = bot.chat(user_input)
            print(reply)
            print()

        except KeyboardInterrupt:
            bot.show_stats()
            print("\n\n👋 Interrupted. Bye!")
            break

        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    main()
