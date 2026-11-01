import numpy as np
import pandas as pd
df=pd.DataFrame({
    "Name": ["vivekanand", "sachchidanand", "ravi", "davide", "virat"],
    "Math": [95, 99, 89, 96, 98],
    "Science":[90, 92, 94, 69, 87],
    "English":[86, 84, 89, 60, 81],
    "Ai/Ml":[93, 95, 75, 67, 64]
})
df["Total"]=df[["Math", "Science", "English", "Ai/Ml"]].sum(axis=1)
df["Percentage"]=(df["Total"]/400)*100
grade=[]
for i in df["Percentage"]:
    if i>=80:
        grade.append("A")
    elif i>=70:
        grade.append("B")
    elif i>=60:
        grade.append("C")
df["Grade"]=grade
print(df)