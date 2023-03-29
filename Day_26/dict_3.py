#How to iterate over pandas data frame

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}

for (key,value) in student_dict.items():
    print(key)
# student
# score

for (key,value) in student_dict.items():
    print(value)
# ['Angela', 'James', 'Lily']
# [56, 76, 98]

import pandas as pd
student_df = pd.DataFrame (student_dict)
print(student_df)

# Loop through data frame
for (key,value) in student_df.items():
    print(value)

# Loop through rows data frame
for (index, row) in student_df.iterrows():
    print(row.student)