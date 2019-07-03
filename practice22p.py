import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

table = pd.read_csv("soccer.csv")

# Let us create weights for attributes
w1 = 1
w2 = 2
w3 = 3
w4 = 4

table["Best_GoalKeepers"] = (w1 * table.GK_Positioning + w2 * table.GK_Diving + w3 * table.GK_Handling + w4 * table.GK_Reflexes)
print(table["Best_GoalKeepers"])

sortedData = table.sort_values("Best_GoalKeepers")
# print(sortedData)

print("===============")
print(sortedData.head(5))
print("===============")
print(sortedData.tail(5))
print("===============")


# Assignment
# Fetch Data from espn cric info and analyze world cup stats :)