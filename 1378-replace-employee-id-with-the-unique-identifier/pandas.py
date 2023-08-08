import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    unique_val = employees.merge(employee_uni[['id', 'unique_id']], how='left', left_on='id', right_on='id')
    unique_val = unique_val[['unique_id', 'name']]
    
    return unique_val
