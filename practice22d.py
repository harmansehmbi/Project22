import pandas as pd
import numpy as np

oddNums = np.arange(1, 100, 2)
evenNums = np.arange(0, 100, 2)

data = {"odds":oddNums, "evens":evenNums}
frame = pd.DataFrame(data)
print(frame)
print("-----------sum----------")
print(frame.sum())
print("------------------------")
print(frame.std())
print("-----------max-----------")
print(frame.max())
print("-----------min-----------")
print(frame.min())