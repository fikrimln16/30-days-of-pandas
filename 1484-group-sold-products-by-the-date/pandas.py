import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    sold = activities.groupby('sell_date').agg(
        num_sold=pd.NamedAgg(column='product', aggfunc='nunique'),
        products=pd.NamedAgg(column='product', aggfunc=lambda x: ','.join(sorted(x.unique())))
    ).reset_index()

    return sold
