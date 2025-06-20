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

<img src="https://github.com/project-dataloom/RetailQ/blob/main/RetailQ_Logo.jpg" width="50%"/>

> Responsive layout with live data outputs for each agent  
> Optional LLM-based explanations included using Mistral / Mock LLM

---

## 📁 Folder Structure
   roject Root

dashboard.py – Streamlit dashboard UI

main.py – Orchestrates all agents

multi_agent_loop.py – Runs the complete multi-agent flow

ollama_client.py – Handles LLM responses using Ollama

requirements.txt – Lists project dependencies

Data Folder (/data)

demand_data.csv – Dataset for demand forecasting

inventory_sample.csv – Sample stock and inventory data

pricing_data.csv – Dataset for pricing agent

Models Folder (/models)

demand_model.pkl – Trained model for demand prediction

Demand Forecasting Agent (/demand_forecasting)

train.py – Model training script

predict.py – Demand prediction logic

preprocess.py – Cleans and prepares data

Inventory Agent (/inventory_agent)

inventory_decision.py – Decides whether to reorder stock

Pricing Agent (/pricing_agent)

predict.py – Suggests dynamic pricing based on inputs


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
