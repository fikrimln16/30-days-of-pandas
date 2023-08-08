import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login = activity.groupby('player_id')['event_date'].min().reset_index(name='first_login')
    return first_login
