# import numpy as np                

""" A = np.array([
    [23, 45],
    [56, 12],
    [15, 14]
])

v=np.array(
    [12, 26]
)
result= A @ v
print("Vector shape:", v.shape)
print("Matrix shape:", A.shape)
print("Result:", result)
"""

""" students=np.array([
    [2, 6],
    [8, 4],
    [7, 9]
])
weights=np.array([23, 45])

scores=students @ weights
print(" students scores:", scores)
"""
from collections import defaultdict
# map
text="big data big analysis data big"

mapped = [(word, 1) for word in text,split()]
# suffle

for key, value in mapped:
    grouped[key].append(value)
    
# reduce
result = {
    key:sum(values) for key, value in grouped.items()
}
print(dict(result))