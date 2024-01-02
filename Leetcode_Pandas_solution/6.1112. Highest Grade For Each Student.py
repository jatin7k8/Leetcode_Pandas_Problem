import pandas as pd

def highest_grade(enrollments: pd.DataFrame) -> pd.DataFrame:
    enrollments.sort_values(by = ['grade','course_id'], ascending = [False, True], inplace = True)
    enrollments['rnk']= enrollments.groupby('student_id').cumcount() + 1
    result = enrollments[enrollments['rnk'] ==1]
    result.sort_values(by='student_id', inplace = True)
    return result[['student_id', 'course_id','grade']]

data = [[2, 2, 95], [2, 3, 95], [1, 1, 90], [1, 2, 99], [3, 1, 80], [3, 2, 75], [3, 3, 82]]
enrollments = pd.DataFrame(data, columns=['student_id', 'course_id', 'grade']).astype({'student_id':'Int64', 'course_id':'Int64', 'grade':'Int64'})
ans = highest_grade(enrollments)
print(ans)