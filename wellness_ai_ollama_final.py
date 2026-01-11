import streamlit as st
import subprocess
import json
import os
import datetime

# =============================
# CONFIG
# =============================
OLLAMA_MODEL = "llama3:8b"
MEMORY_FILE = "user_memory.json"

# =============================
# MEMORY HANDLING (LONG-TERM)
# =============================
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {
        "topics": [],
        "risk_flag": False
    }

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

# =============================
# SAFETY AGENT
# =============================
def safety_agent(text):
    danger_phrases = [
        "suicide", "kill myself", "end my life",
        "i want to die", "no reason to live",
        "self harm", "hurt myself"
    ]
    return any(p in text.lower() for p in danger_phrases)

def safety_response():
    return (
        "🛑 **I’m really glad you told me this.**\n\n"
        "You’re not alone, and what you’re feeling matters.\n\n"
        "Please reach out **right now**:\n"
        "- A trusted friend or family member\n"
        "- A mental health professional\n"
        "- Emergency services if you feel unsafe\n\n"
        "**India Helpline:** AASRA – 91-9820466726\n\n"
        "If you want, we can slow your breathing together."
    )

# =============================
# OLLAMA LLM CALL
# =============================
def call_llm(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL],
            input=prompt,
            text=True,
            capture_output=True,
            timeout=60
        )
        return result.stdout.strip()
    except Exception:
        return (
            "I’m here with you. Let’s slow things down.\n\n"
            "Can you tell me a little more about what you’re feeling?"
        )

# =============================
# REASONING AGENT
# =============================
def reasoning_agent(text):
    t = text.lower()
    if t in ["yes", "yeah", "yep", "sure"]:
        return "yes"
    if t in ["no", "nope", "nah"]:
        return "no"
    if any(k in t for k in ["stress", "anxiety", "panic", "overwhelmed"]):
        return "stress"
    if any(k in t for k in ["diet", "nutrition", "fat loss", "weight loss"]):
        return "diet"
    if any(k in t for k in ["muscle", "gym", "workout", "exercise"]):
        return "fitness"
    if any(k in t for k in ["sleep", "insomnia", "tired"]):
        return "sleep"
    if any(k in t for k in ["motivation", "burnout", "lazy"]):
        return "motivation"
    return "general"

# =============================
# ANSWER AGENT (THINKING + MEMORY)
# =============================
def answer_agent(user_input):
    memory = st.session_state.memory

    # SAFETY FIRST
    if safety_agent(user_input):
        memory["risk_flag"] = True
        save_memory(memory)
        return safety_response()

    intent = reasoning_agent(user_input)

    # YES FOLLOW-UP
    if intent == "yes" and st.session_state.last_question == "calming":
        return (
            "🧘 **5-Minute Calming Routine**\n\n"
            "1️⃣ Inhale for 4 seconds\n"
            "2️⃣ Hold for 4 seconds\n"
            "3️⃣ Exhale slowly for 6 seconds\n"
            "4️⃣ Repeat 5 times\n\n"
            "Place one hand on your chest while breathing.\n\n"
            "Tell me how your body feels now."
        )

    # STORE TOPIC MEMORY
    if intent in ["stress", "diet", "fitness", "sleep", "motivation"]:
        memory["topics"].append(intent)
        save_memory(memory)

    # LOCAL GUIDED RESPONSES
    if intent == "stress":
        st.session_state.last_question = "calming"
        return (
            "🌿 **Stress means your nervous system is overloaded.**\n\n"
            "✔ Slow breathing\n"
            "✔ Reduce screen stimulation\n"
            "✔ Gentle movement\n\n"
            "Would you like a **guided calming routine**?"
        )

    if intent == "diet":
        return (
            "🥗 **Diet depends on your goal.**\n\n"
            "For fat loss:\n"
            "✔ Small calorie deficit\n"
            "✔ High protein & fiber\n\n"
            "For muscle growth:\n"
            "✔ Protein + carbs\n"
            "✔ Strength training\n\n"
            "Tell me your exact goal."
        )

    if intent == "fitness":
        return (
            "🏋️ **Fitness works when it’s sustainable.**\n\n"
            "✔ Train 3–5x/week\n"
            "✔ Progressive overload\n"
            "✔ Proper recovery\n\n"
            "Are you a beginner or experienced?"
        )

    if intent == "sleep":
        return (
            "😴 **Better sleep comes from routine.**\n\n"
            "✔ Fixed bedtime\n"
            "✔ No phone 1 hour before sleep\n"
            "✔ Dark, cool room\n\n"
            "Want a night routine?"
        )

    if intent == "motivation":
        return (
            "🔥 **Low motivation is mental fatigue, not laziness.**\n\n"
            "✔ Start small\n"
            "✔ Reduce friction\n"
            "✔ Track progress\n\n"
            "Want a simple daily system?"
        )

    # LLM THINKING RESPONSE (CHATGPT-LIKE)
    prompt = f"""
You are a calm, supportive wellness assistant.

Rules:
- No medical diagnosis
- No self-harm encouragement
- Be empathetic, practical, and clear
- Answer like ChatGPT

User message:
{user_input}
"""
    return call_llm(prompt)

# =============================
# STREAMLIT UI
# =============================
st.set_page_config(page_title="Wellness AI Agent", page_icon="🧠")
st.title("🧠 Wellness AI Agent")
st.caption("Ask anything about wellness. I think, remember & respond safely.")

if "chat" not in st.session_state:
    st.session_state.chat = []

if "memory" not in st.session_state:
    st.session_state.memory = load_memory()

if "last_question" not in st.session_state:
    st.session_state.last_question = None

for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask anything about your wellness...")

if user_input:
    st.session_state.chat.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    reply = answer_agent(user_input)

    st.session_state.chat.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)

st.markdown("---")
st.caption("🧠 Wellness AI | Ollama • Long-Term Memory • Safety • Reasoning")
st.caption(datetime.datetime.now().strftime("Session Time: %H:%M:%S"))
