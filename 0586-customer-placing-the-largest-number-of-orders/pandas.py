import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    customer_mode = orders['customer_number'].mode().values
    top_cust = pd.DataFrame({'customer_number': customer_mode})
    return top_cust
