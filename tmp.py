import pandas as pd
import numpy as np

marathon_2017 = pd.read_csv("C:\\AI\\data\\marathon_results_2017.csv")

print(marathon_2017.columns)
print("--------------------------------------------------------")
print(marathon_2017.isnull().sum(axis=0))
print("--------------------------------------------------------")
marathon_2017_clean = marathon_2017.drop(["Unnamed: 0","Bib","State","Unnamed: 9"],axis="columns")
print(marathon_2017_clean.head())
marathon_2017_clean["Official Time New"] = pd.to_timedelta(marathon_2017_clean["Official Time"])
print(marathon_2017_clean.head())
marathon_2017_clean["Official Time Sec"] = marathon_2017_clean["Official Time New"].astype("m8[s]").astype(np.int64)
print(marathon_2017_clean.head())
print("--------------------------------------------------------")

def to_seconds(a):
    hms = a.split(":")
    print(hms)

a = to_seconds("10:10:10")
