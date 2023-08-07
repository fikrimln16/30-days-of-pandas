import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    modified_table = products.set_index('product_id').stack().reset_index()
    modified_table.columns = ['product_id', 'store', 'price']
    return modified_table.dropna()
