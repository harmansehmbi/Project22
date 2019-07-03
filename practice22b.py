import pandas as pd
import numpy as np

arr = list(range(1, 51))
S1 = pd.Series(arr)
print("---------------------------")
print(S1)
print("---------------------------")
print(S1.axes)
print("---------------------------")

data = S1.values
print(data)
print(type(data))