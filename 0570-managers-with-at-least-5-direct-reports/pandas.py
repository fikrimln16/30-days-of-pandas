import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    direct_reports_count = employee.groupby('managerId')['id'].count().reset_index(name='report_count')
    managers_with_five_reports = direct_reports_count[direct_reports_count['report_count'] >= 5]
    manager = pd.merge(managers_with_five_reports, employee, left_on='managerId', right_on='id', how='inner')

    return manager[['name']]
