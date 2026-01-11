# 🧠 Wellness AI Agent

### ChatGPT-Style Wellness Guidance with Long-Term Memory & Safety (Offline)

An **AI-powered wellness guidance chatbot** built using **Python, Streamlit, and Ollama (LLaMA 3)**.
The system provides **empathetic, context-aware wellness support** with **long-term memory** and **mental-health safety escalation**, all while running **fully offline**.

---

## 🌍 SDG Alignment

**SDG 8 – Decent Work & Economic Growth**

Healthy individuals are more productive.
This project supports SDG-8 by:

* Promoting **mental and physical well-being**
* Reducing burnout and stress
* Supporting sustainable productivity and employability
* Providing accessible wellness guidance without cost barriers

---

## ✨ Key Features

* 🧠 **ChatGPT-Style Conversations**
  Free-text questions, natural responses, intelligent follow-ups

* 💾 **Long-Term Memory**
  Remembers user topics and adapts responses across sessions

* 🛡️ **Mental Health Safety Escalation**
  Detects high-risk language and provides ethical support & helpline guidance

* 📴 **100% Offline & Private**
  Powered by **Ollama** — no APIs, no data sharing

* 🔁 **Agent-Based Architecture**
  Safety Agent → Reasoning Agent → Memory Agent → Response Agent

* 🎯 **Wellness Domains Covered**

  * Stress & anxiety
  * Sleep & recovery
  * Diet & nutrition
  * Fitness & exercise
  * Motivation & burnout

---

## 🏗️ Architecture Overview

```
User Input
   ↓
Safety Agent (risk detection)
   ↓
Reasoning Agent (intent understanding)
   ↓
Memory Agent (long-term context)
   ↓
LLM (Ollama - LLaMA 3)
   ↓
Safe, Personalized Wellness Response
```

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Streamlit** – UI & chat interface
* **Ollama** – Local LLM runtime
* **LLaMA 3 (8B)** – Reasoning & response generation
* **JSON** – Persistent long-term memory

---

## 🚀 Installation & Setup

### 1️⃣ Install Ollama

Download and install Ollama from:
👉 [https://ollama.com/download](https://ollama.com/download)

### 2️⃣ Pull the LLM Model

```bash
ollama pull llama3:8b
```

### 3️⃣ Install Python Dependencies

```bash
pip install streamlit
```

### 4️⃣ Run the Application

```bash
streamlit run wellness_ai_ollama_final.py
```

---

## 💬 Example Interaction

```
User: I'm feeling very stressed lately
Bot: Stress means your nervous system is overloaded...
     Would you like a guided calming routine?

User: yes
Bot: (Provides a 5-minute breathing routine)
```

---

## 🛡️ Ethical AI & Safety

* No medical diagnosis
* No harmful advice
* Crisis detection with escalation
* Encourages professional help when needed
* Follows responsible AI principles

---

## 📁 Project Structure

```
├── wellness_ai_ollama_final.py   # Main application
├── user_memory.json              # Long-term memory (auto-generated)
├── README.md                     # Project documentation
```

---

## 🎓 Use Cases

* Students dealing with academic stress
* Working professionals facing burnout
* Fitness & wellness coaching support
* Mental health awareness & early guidance
* Hackathons, capstones, and research demos

---

## 🔮 Future Enhancements

* Multi-user profiles
* Encrypted memory storage
* Voice interaction
* IBM Watsonx / SkillsBuild integration
* Mobile-friendly UI
* Analytics dashboard (stress trends, habits)

---

## 📜 License

This project is open-source and intended for **educational and non-clinical use only**.

---

## 🤝 Acknowledgements

* **Ollama** for local LLM infrastructure
* **Meta AI** for LLaMA models
* **Streamlit** for rapid UI development

---

## ⭐ Final Note

This project demonstrates how **responsible AI + local LLMs** can deliver **real-world wellness impact** while remaining **ethical, private, and accessible**.

If you found this useful, consider ⭐ starring the repo!

---
