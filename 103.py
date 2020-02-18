import pandas as pd

marathon_2017 = pd.read_csv("C:\\AI\\data\\marathon_results_2017.csv")

print("------------------------------------")
marathon_2017_clean["Senior"] = marathon_2017_clean.Age > 60
print(marathon_2017_clean.head())

print("------------------------------------")
marathon_2017_clean["Year"] = "2017"
print(marathon_2017_clean.head())

print("------------------------------------")
print(marathon_2017_clean.info())

print("------------------------------------")
names = marathon_2017_clean.Name
print(names)

print("------------------------------------")
Official_Time = marathon_2017_clean["Official Time"]
print(Official_Time)
