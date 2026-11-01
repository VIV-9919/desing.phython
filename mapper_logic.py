import time
""" 
sizes=[100_00, 1_000_000, 10_000_000]
for size in sizes:
    start=time.perf_counter()
    total=sum(range(size))
    elapsed=time.perf_counter() - start
    print(f"size: {size:,}," 
          f"Time: {elapsed:.4f} seconds, "
          f"Total:{total}"
    ) 
    """

from collections import defaultdict
"""
sales=[
    ("laptop", 25000),
    ("mobile", 10000),
    ("frizzes", 22000),
    ("tablet", 15000)
]
totals=defaultdict(int)
for category, amount in sales:
    totals[category] += amount
    for category, total in sorted(totals.items()):
        print(category, total) """
        
import pandas as pd  
data={
    "index_no": [1, 2, 3, 4],
    "Order_ID": [101, 102, 103, 104],
    "Category": ["mobile", "laptop", "AC", "TV"],
    "Amount": [1230, 3048, 5890, 4759]
    
}
df=pd.DataFrame(data)
revenue=(
    df.groupby("Category")["Amount"].sum().sort_values(ascending=False))

print(revenue)