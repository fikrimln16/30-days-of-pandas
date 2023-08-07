import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_countries_data = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return big_countries_data[['name', 'population', 'area']]
