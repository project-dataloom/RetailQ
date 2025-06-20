
import pandas as pd
from demand_forecasting.predict import predict as predict_demand
from inventory_agent.inventory_decision import inventory_decision
from pricing_agent.predict import predict_price

# --- Load datasets ---
demand_df = pd.read_csv("data/demand_data.csv")
inventory_df = pd.read_csv("data/inventory_sample.csv")
pricing_df = pd.read_csv("data/pricing_data.csv")

# --- STEP 1: Demand Forecasting Agent ---
forecast = predict_demand(demand_df)
demand_df["Predicted Units Sold"] = forecast
predicted_demand = demand_df.groupby("Product ID")["Predicted Units Sold"].mean().to_dict()

# --- STEP 2: Inventory Agent Decision ---
inventory_actions = inventory_decision(inventory_df, predicted_demand)

# --- STEP 3: Pricing Agent for All Products ---
pricing_recommendations = []
for product_id in inventory_df["Product ID"]:
    row = pricing_df[pricing_df["Product ID"] == product_id].iloc[-1:].copy()

    if row.empty:
        continue

    # Simulate today's row
    predicted_price = predict_price(row)[0]

    pricing_recommendations.append({
        "Product ID": product_id,
        "Suggested Price": round(predicted_price, 2),
        "Stock Remaining": row["Stock Remaining"].values[0],
        "Competitor Price": row["Competitor Price"].values[0]
    })

pricing_df_out = pd.DataFrame(pricing_recommendations)

# --- Final Output ---
print("\n🧠 DEMAND FORECASTING:")
print(pd.DataFrame.from_dict(predicted_demand, orient='index', columns=['Predicted Units']).reset_index().rename(columns={"index": "Product ID"}))

print("\n📦 INVENTORY ACTIONS:")
print(inventory_actions)

print("\n💸 PRICING RECOMMENDATIONS:")
print(pricing_df_out)

#------------ Ollama Integration -------------

from ollama_client import ask_ollama

print("\n🧠 LLM Agent Reasoning (via Mistral):")
for i, row in inventory_actions.iterrows():
    if row["Status"] == "REORDER":
        prompt = (
            f"Product {row['Product ID']} has current stock {inventory_df.loc[i, 'Current Stock']}, "
            f"predicted demand {predicted_demand[row['Product ID']]:.2f}, "
            f"reorder point {inventory_df.loc[i, 'Reorder Point']}, "
            f"and lead time {row['Lead Time (days)']} days.\n"
            f"Explain if it's a good idea to reorder and why."
        )
        response = ask_ollama(prompt)
        print(f"🧾 Product {row['Product ID']} → {response}\n")
 
