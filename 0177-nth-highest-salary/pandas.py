import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted = employee['salary'].sort_values(ascending=False).drop_duplicates()

    if N > len(sorted):
        return pd.DataFrame({'getNthHighestSalary': [None]})

    nth_highest = sorted.iloc[N -1]
    
    return pd.DataFrame({'getNthHighestSalary': [nth_highest]})
