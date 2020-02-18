import pandas as pd

marathon_2017 = pd.read_csv("C:\\AI\\data\\marathon_results_2017.csv")

print("------------------------------------")
print("marathon_2017.isnull().sum(axis=0)")
print(marathon_2017.isnull().sum(axis=0))
#marathon_2017.isnull().sum(axis=0)

print("------------------------------------")
print("marathon_2017.columns")
print(marathon_2017.columns)

print("------------------------------------")
print("marathon_2017_clean = marathon_2017.drop(['Unnamed: 0','Bib','Unnamed: 9'],axis=columns)")
marathon_2017_clean = marathon_2017.drop(['Unnamed: 0','Bib','Unnamed: 9'],axis="columns")
print(marathon_2017_clean.info())
