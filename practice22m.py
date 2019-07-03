import pandas as pd

Teams = ["Rajasthan Royals",
         "Deccan Chargers",
         "Chennai Super Kings",
         "Chennai Super Kings",
         "Kolkata Knight Riders",
         "Mumbai Indians",
         "Kolkata Knight Riders",
         "Mumbai Indians",
         "Sunrisers Hydrabad",
         "Mumbai Indians",
         "Chennai Super Kings",
         "Mumbai Indians"]

Ranks = [2, 3, 3, 5, 1, 6, 1, 1, 3, 4, 4, 5]

Years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

data1 = {  "Team": Teams,
          "Rank": Ranks,
          "Year": Years
       }

data2 = {  "Team": ["Kings XI", "RCB", "Delhi Capitals"],
           "Rank": [8, 9, 5]

       }

frame1 = pd.DataFrame(data1)
frame2 = pd.DataFrame(data2)

print("=========================")
print(frame1)
print("=========================")
print(frame2)

frame3 = pd.merge(frame1, frame2, on="Team", how="inner")
print("==========inner=============")
print(frame3)


# Explore how joins work
# http://www.w3school.co.in/SQL Joins ....