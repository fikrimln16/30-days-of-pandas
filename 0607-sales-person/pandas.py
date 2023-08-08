import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_sales_ids = orders[orders['com_id'].isin(company[company['name'] == 'RED']['com_id'])]['sales_id'].unique()
    non_ordered = sales_person[~sales_person['sales_id'].isin(red_sales_ids)][['name']]
    
    return non_ordered
