import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    freq_act = actor_director.groupby(['actor_id', 'director_id'])['director_id'].count().reset_index(name='count')
    freq_act = freq_act[freq_act['count'] >= 3][['actor_id', 'director_id']]
    
    return freq_act
