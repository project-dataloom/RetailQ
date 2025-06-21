import streamlit as st
import pandas as pd
import openai
from demand_forecasting.predict import predict as predict_demand
from inventory_agent.inventory_decision import inventory_decision
from pricing_agent.predict import predict_price
import os

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_llm(prompt: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"LLM error: {str(e)}"

# Load data
demand_df = pd.read_csv("data/demand_data.csv")
inventory_df = pd.read_csv("data/inventory_sample.csv")
pricing_df = pd.read_csv("data/pricing_data.csv")

st.set_page_config(page_title="RetailQ AI Dashboard", layout="wide")
st.markdown("""
    <style>
        .main {
            background: linear-gradient(to bottom right, #f0f4f8, #e2e8f0);
            padding: 20px;
            font-family: 'Segoe UI', sans-serif;
        }
        .card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        h2 {
            color: #2c3e50;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 RetailQ - Multi-Agent Retail Intelligence Dashboard")

# --- Demand Forecasting ---
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("📈 Demand Forecasting")
forecast = predict_demand(demand_df)
demand_df["Predicted Units Sold"] = forecast
predicted_demand = demand_df.groupby("Product ID")["Predicted Units Sold"].mean().to_dict()
st.dataframe(demand_df[["Product ID", "Predicted Units Sold"]].drop_duplicates(), use_container_width=True)

if st.checkbox("🧠 Show LLM Reasoning (Demand)"):
    for product_id, units in predicted_demand.items():
        prompt = f"Forecasted demand for Product {product_id} is {units:.2f} units. What factors might explain this?"
        explanation = ask_llm(prompt)
        st.markdown(f"*Product {product_id}:* {explanation}")
st.markdown("</div>", unsafe_allow_html=True)

# --- Inventory Agent ---
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("📦 Inventory Decisions")
inventory_actions = inventory_decision(inventory_df, predicted_demand)
st.dataframe(inventory_actions, use_container_width=True)

if st.checkbox("📘 Show LLM Reasoning (Inventory)"):
    for i, row in inventory_actions.iterrows():
        if row["Status"] == "REORDER":
            prompt = (
                f"Product {row['Product ID']} has current stock {inventory_df.loc[i, 'Current Stock']}, "
                f"predicted demand {predicted_demand[row['Product ID']]:.2f}, "
                f"reorder point {inventory_df.loc[i, 'Reorder Point']}, "
                f"and lead time {row['Lead Time (days)']} days. Should we reorder? Explain."
            )
            response = ask_llm(prompt)
            st.markdown(f"*Product {row['Product ID']}:* {response}")
st.markdown("</div>", unsafe_allow_html=True)

# --- Pricing Agent ---
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("💰 Pricing Recommendations")
pricing_results = []
for product_id in inventory_df["Product ID"]:
    row = pricing_df[pricing_df["Product ID"] == product_id].iloc[-1:].copy()
    if row.empty:
        continue
    predicted_price = predict_price(row)[0]
    pricing_results.append({
        "Product ID": product_id,
        "Suggested Price": round(predicted_price, 2),
        "Stock Remaining": row["Stock Remaining"].values[0],
        "Competitor Price": row["Competitor Price"].values[0]
    })

pricing_df_out = pd.DataFrame(pricing_results)
st.dataframe(pricing_df_out, use_container_width=True)

if st.checkbox("💬 Show LLM Reasoning (Pricing)"):
    for i, row in pricing_df_out.iterrows():
        prompt = (
            f"Product {row['Product ID']} has a competitor price of ₹{row['Competitor Price']}, "
            f"our suggested price is ₹{row['Suggested Price']}, and stock remaining is {row['Stock Remaining']}. "
            f"Explain if this pricing is strategic and market-aligned."
        )
        response = ask_llm(prompt)
        st.markdown(f"*Product {row['Product ID']}:* {response}")
st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<hr/>
<p style='text-align:center; font-size: 0.8em;'>RetailQ AI Dashboard © 2025</p>
""", unsafe_allow_html=True)
