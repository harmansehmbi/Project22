import pandas as pd
import numpy as np

data = np.random.rand(5, 4)

frame = pd.DataFrame(data, columns=["COL1", "COL2", "COL3", "COL4"] )
print(frame)
print("-----------------")
print(frame["COL1"])
print("-----------------")



# Iterate using iteritems functions:

print()
print("-----------iteritems--------------")
print()

for key, value in frame.iteritems():
    print(key)
    print("-----------------")
    print(value)
    print("-----------------")
    print(type(value))
    print("-----------------")

# Conclusion :  DataFrame is collection of Series
#               Series is collection of numpy and arrays

# Iterate using iterrows functions: Rows

print()
print("------------iterrows-----------")
print()

for key, value in frame.iterrows():
    print(key)
    print("-----------------")
    print(value)
    print("-----------------")
    print(type(value))
    print("-----------------")

# Iterate using itertuples function: Rows as a tuple

print()
print("---rows as tuple--------itertuples------------")
print()

for rows in frame.itertuples():
    print(rows)
    print("-----------------")
    print(type(rows))
    print("-----------------")