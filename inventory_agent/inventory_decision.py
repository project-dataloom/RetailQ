import pandas as pd

def inventory_decision(inventory_df, demand_predictions):
    decisions = []

    for i, row in inventory_df.iterrows():
        product_id = row['Product ID']
        stock = row['Current Stock']
        reorder_point = row['Reorder Point']
        lead_time = row['Supplier Lead Time (days)']
        predicted_demand = demand_predictions.get(product_id, 0)

        if stock <= reorder_point or stock < predicted_demand:
            decisions.append({
                'Product ID': product_id,
                'Status': 'REORDER',
                'Reason': 'Predicted demand exceeds stock or below reorder point',
                'Reorder Qty': max(predicted_demand - stock, 50),
                'Lead Time (days)': lead_time
            })
        else:
            decisions.append({
                'Product ID': product_id,
                'Status': 'STOCK_OK',
                'Reason': 'Sufficient stock available',
                'Reorder Qty': 0,
                'Lead Time (days)': lead_time
            })

    return pd.DataFrame(decisions)
