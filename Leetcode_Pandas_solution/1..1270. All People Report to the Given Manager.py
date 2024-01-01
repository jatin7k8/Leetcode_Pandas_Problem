import pandas as pd

def find_reporting_people(employees: pd.DataFrame) -> pd.DataFrame:
    e1 = employees.copy() 
    e2 = employees.copy() 
    df = e1.merge(e2, left_on = 'manager_id' , right_on = 'employee_id',how = 'left')
    e3 = employees.copy()
    data = df.merge(e3, left_on ='manager_id_y' , right_on = 'employee_id',how = 'left')
    result = data[(data['manager_id'] == 1) & (data['employee_id_x'] != 1)][['employee_id_x', 'manager_id']]
    d = result.rename(columns={'employee_id_x':'employee_id'})
    return d[['employee_id']]

data = [[1, 'Boss', 1], [3, 'Alice', 3], [2, 'Bob', 1], [4, 'Daniel', 2], [7, 'Luis', 4], [8, 'John', 3], [9, 'Angela', 8], [77, 'Robert', 1]]
employees = pd.DataFrame(data, columns=['employee_id', 'employee_name', 'manager_id']).astype({'employee_id':'Int64', 'employee_name':'object', 'manager_id':'Int64'})

ans = find_reporting_people(employees)
print(ans)