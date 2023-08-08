import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate_count = (delivery['order_date'] == delivery['customer_pref_delivery_date']).sum()
    total_rows = len(delivery)
    immediate_percentage = round(immediate_count / total_rows * 100, 2)
    return pd.DataFrame({'immediate_percentage': [immediate_percentage]})
