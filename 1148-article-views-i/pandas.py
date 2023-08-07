import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    unique_value = sorted(views.loc[views['author_id'] == views['viewer_id'], 'author_id'].unique())
    result = pd.DataFrame({'id': unique_value})
    return result
