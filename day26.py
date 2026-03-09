import pandas as pd
data = {
    "Name": ["Akshmith", "Roopesh", "Pranvi", "Karan", "Suraksha"],
    "Python": [90, 82, 89, 76, 91],
    "Machine Learning": [85, 78, 92, 74, 88],
    "Java": [80, 76, 95, 70, 84],
    "DBMS": [88, 90, 91, 75, 86]
}

df = pd.DataFrame(data)
print("Dataset of student:\n")
print(df)

selected_columns = df[["Name", "Python"]]
print("\nSelected Columns:\n")
print(selected_columns)

rows = df.iloc[0:3]
print("\nSelected Rows:\n")
print(rows)

data_selection = df.loc[1:3, ["Python", "Java"]]
print("\nSelected Rows and Columns:\n")
print(data_selection)

high_scores = df[df["Python"] > 90]
print("\nStudents with Python score > 85:\n")
print(high_scores)
