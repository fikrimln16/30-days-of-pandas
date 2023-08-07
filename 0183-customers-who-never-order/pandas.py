import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    not_ordering_customer = customers[~customers['id'].isin(orders['customerId'])]
    not_ordering_customer = not_ordering_customer[['name']].rename(columns={'name': 'Customers'})
    return not_ordering_customer
