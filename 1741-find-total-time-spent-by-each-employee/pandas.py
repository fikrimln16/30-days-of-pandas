import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees['day'] = employees['event_day'].dt.strftime('%Y-%m-%d')
    
    time_spent = employees.groupby(['emp_id', 'day'], as_index=False)['total_time'].sum()
    time_spent = time_spent[['day', 'emp_id', 'total_time']]
    
    return time_spent
