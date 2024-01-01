import pandas as pd

def biggest_window(user_visits: pd.DataFrame) -> pd.DataFrame:
    user_visits.sort_values(['user_id', 'visit_date'], inplace= True)
    user_visits['lead_visit_date(1)'] = user_visits.groupby('user_id')['visit_date'].shift(-1).fillna(pd.Timestamp('2021-01-01'))
    user_visits['biggest_window'] = (user_visits['lead_visit_date(1)']- user_visits['visit_date']).dt.days
    result = user_visits.groupby('user_id')['biggest_window'].max().reset_index()
    return result[['user_id', 'biggest_window']]


data = [['1', '2020-11-28'], ['1', '2020-10-20'], ['1', '2020-12-3'], ['2', '2020-10-5'], ['2', '2020-12-9'], ['3', '2020-11-11']]
user_visits = pd.DataFrame(data, columns=['user_id', 'visit_date']).astype({'user_id':'Int64', 'visit_date':'datetime64[ns]'})

ans = biggest_window(user_visits)
print(ans)