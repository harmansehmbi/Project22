import pandas as pd
import numpy as np

data = np.random.rand(5, 4)

frame = pd.DataFrame(data, columns=["COL1", "COL2", "COL3", "COL4"] )
print(frame)
print("-----------------")
print(frame["COL1"])
print("-----------------")



# Iterate using iteritems functions:

for key, value in frame.iteritems():
    print(key)
    print("-----------------")
    print(value)
    print("-----------------")
    print(type(value))
    print(">>>>>>>>>>>>>>>>>")