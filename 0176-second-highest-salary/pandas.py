import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted = employee['salary'].sort_values(ascending=False).drop_duplicates()

    if len(sorted) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    second_highest = sorted.iloc[1]

    return pd.DataFrame({'SecondHighestSalary': [second_highest]})
