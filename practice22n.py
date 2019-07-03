import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

# seaborn cant work alone ... it req matplotlib
# Explore Seaborn :https://seaborn.pydata.org/

table = pd.read_csv("soccer.csv")
# print(table)

# print(table.head(5))
# print(table.tail(5))

# print(table["Name"])
print(table.Name)

# Take less samples to plot and check
sns.countplot(y=table.Nationality, palette="Set2")
plt.show()
