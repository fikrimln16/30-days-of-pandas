import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    distinct_value = daily_sales.groupby(['date_id', 'make_name']).agg(
        unique_leads=pd.NamedAgg(column='lead_id', aggfunc='nunique'),
        unique_partners=pd.NamedAgg(column='partner_id', aggfunc='nunique')
    ).reset_index()

    return distinct_value
