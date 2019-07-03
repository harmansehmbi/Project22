import pandas as pd
import numpy as np

arr = np.arange(1, 51, 2)
S1 = pd.Series(arr)
print("---------------------------")
print(S1)
print("---------------------------")
print(S1.axes)
print("---------------------------")

data = S1.values
print(data)
print(type(data))