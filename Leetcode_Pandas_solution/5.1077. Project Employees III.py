

import pandas as pd

def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df_merged = project.merge(employee, on='employee_id')
    max_experience_per_project = df_merged.groupby('project_id')['experience_years'].max().reset_index()
    result = df_merged.merge(max_experience_per_project, on=['project_id', 'experience_years'])
    return result[['project_id', 'employee_id']]

data_project = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
project = pd.DataFrame(data_project, columns=['project_id', 'employee_id']).astype({'project_id':'Int64', 'employee_id':'Int64'})
data_employee = [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 3], [4, 'Doe', 2]]
employee = pd.DataFrame(data_employee, columns=['employee_id', 'name', 'experience_years']).astype({'employee_id':'Int64', 'name':'object', 'experience_years':'Int64'})

result = project_employees(project, employee)
print(result)
