# 🛒 RetailQ – Multi-Agent Retail AI System

> Reinventing retail intelligence with AI-driven agents for *demand forecasting, **inventory optimization, and **pricing strategy* — powered by ML and LLMs.

![RetailQ Banner](https://img.shields.io/badge/Built%20With-Python%20%7C%20Streamlit%20%7C%20ScikitLearn-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Demo%20Ready-green?style=flat-square)

---

## 🚀 Live Demo

🔗  https://retailq-v3td2mj8lzu5davhvbqgch.streamlit.app/  
 

---

## 🎯 Project Overview

RetailQ is a modular AI system that helps retail businesses:
- ✅ Forecast product demand using ML
- ✅ Optimize inventory by making proactive reorder decisions
- ✅ Suggest smart, competitive prices using pricing models
- ✅ Add explainable LLM reasoning for transparency

It’s built around a *multi-agent architecture* where each agent focuses on a specific retail domain.

---

## 🧠 Key Agents

| Agent              | Purpose                                                                 |
|-------------------|-------------------------------------------------------------------------|
| 📈 Demand Agent    | Predicts units sold using historical data                               |
| 📦 Inventory Agent | Triggers reorder actions based on predicted demand and current stock   |
| 💰 Pricing Agent   | Suggests optimized prices based on competitor prices & stock levels     |
| 🧠 LLM Reasoning   | Generates natural language explanations for model decisions (Mistral/Ollama) |

---

## 🖥 Dashboard UI (Streamlit)

<img src="https://github.com/project-dataloom/RetailQ/blob/main/RetailQ_Logo.jpg" width="100%"/>

> Responsive layout with live data outputs for each agent  
> Optional LLM-based explanations included using Mistral / Mock LLM

---

## 📁 Folder Structure

RetailQ/
├── dashboard.py # Streamlit frontend
├── main.py # Multi-agent flow logic
├── multi_agent_loop.py # (optional orchestration logic)
├── ollama_client.py # Handles LLM prompts (mock or local)
├── /data/ # All CSV datasets
├── /models/ # Saved model .pkl files
├── /demand_forecasting/ # Demand ML logic
├── /inventory_agent/ # Inventory logic
├── /pricing_agent/ # Pricing logic
└── requirements.txt

---

## ⚙ Tech Stack

- *Frontend*: Streamlit
- *ML Models*: Scikit-learn
- *LLM Reasoning*: Ollama (Mistral) or Demo/Mock
- *Deployment*: Streamlit Cloud (easy and free)

---

## 🚧 Deployment Instructions

### 1. Clone the project

```bash
git clone https://github.com/HemanthKumarMusirana/RetailQ.git
cd RetailQ
pip install -r requirements.txt
streamlit run dashboard.py


📢 Credits
Built by Hemanth Kumar Musirana and Raghavendra Vempuluru
Part of the RetailQ AI Personal Project under Team DataLoom

💡 Future Scope
Integrate real-time databases (Firebase/PostgreSQL)

Add real API integration with OpenAI/GPT for LLM reasoning

Build user authentication & admin dashboards

Deploy with backend APIs (Flask/FastAPI) for production-grade use

🌟 Show Your Support!
If you found this project helpful:

⭐ Star the repo

📌 Fork and customize for your own startup or project

🧠 Share feedback or ideas
