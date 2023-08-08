import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    fulfilled_class = courses['class'].value_counts().reset_index()
    fulfilled_class.columns = ['class', 'count']
    return fulfilled_class[fulfilled_class['count'] >= 5][['class']]
