import pandas as pd

def find_continuous_ranges(logs: pd.DataFrame) -> pd.DataFrame:
    logs['rank'] = logs['log_id'].rank(method='first').astype(int)
    logs['diff_group'] = abs(logs['rank'] - logs['log_id'])
    result = logs.groupby('diff_group').agg(start_id=('log_id', 'min'),
                                            end_id=('log_id', 'max')).reset_index()
    return result[['start_id', 'end_id']]

data = [[1], [2], [3], [7], [8], [10]]
logs = pd.DataFrame(data, columns=['log_id']).astype({'log_id': 'Int64'})

ans = find_continuous_ranges(logs)
print(ans)
