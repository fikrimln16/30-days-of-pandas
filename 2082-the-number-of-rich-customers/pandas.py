import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    rich_count = store.loc[store['amount'] > 500, 'customer_id'].nunique()
    return pd.DataFrame({'rich_count': [rich_count]})
