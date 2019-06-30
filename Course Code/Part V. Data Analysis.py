# Pandas and Series
import pandas as pd

se = pd.Series([1, 3, 5, 7, 9])
se
se[1]

se = pd.Series([100, 300, 500, 700, 900], index=["a", "b", "c", "d", "e"])
se
se["a"]

# Converting dictionaries to Series
salary = {"John": 3000,
          "Tim": 4500,
          "Rob": 5600}
salary
salary_series = pd.Series(salary)
salary_series["John"]

# Data frame basics
data = {"Name": ["John", "Tim", "Rob"],
        "Age": [23, 45, 61],
        "Salary": [4000, 5000, 6000]
        }
data

datadf = pd.DataFrame(data)
datadf

new_datadf = pd.DataFrame(data=data, columns=["Age", "Name", "Salary"])

# For getting the column
new_datadf["Salary"]
# For getting the row
new_datadf.iloc[2]

new_datadf["Profile"] = "Doctor"
new_datadf

new_datadf["Education"] = "MS"
new_datadf

# Transposing the data frame
test_frame = new_datadf.T
test_frame

# Re-indexing series and data frames
se
reindexed = se.reindex(["b", "a", "c", "d", "e"])
reindexed

new_datadf
reindexed_df = new_datadf.reindex([0, 2, 1])
reindexed_df

fields = ["Name", "Age", "Salary"]
reindexed_df = new_datadf.reindex(columns=fields)
reindexed_df

# Deleting rows and columns
new_datadf

# Rows
new_datadf2 = new_datadf.drop([2])
new_datadf2

new_datadf2 = new_datadf.drop([1, 2])
new_datadf2

# Columns
new_datadf
new_datadf3 = new_datadf.drop(["Education"], axis=1)
new_datadf3

new_datadf3 = new_datadf.drop("Education", axis=1)
new_datadf3

# Operations with series and data frames









