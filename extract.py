import pandas as pd 
data = [
    {"id": 101, "name": "Vishal", "age": 22},
    {"id": 102, "name": "Amit", "age": 23},
    {"id": 103, "name": "Rahul", "age": 24}
]

print(data)


df= pd.DataFrame(data)
print(df)