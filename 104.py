import pandas as pd

marathon_2017 = pd.read_csv("C:\\AI\\data\\marathon_results_2017.csv")

print("------------------------------------")
seniors = marathon_2017_clean.Age > 60
print(seniors)

print("------------------------------------")
KEN_runner = marathon_2017_clean[marathon_2017_clean.Country == "KEN"]
print(KEN_runner)

print("------------------------------------")
print(marathon_2017_clean["Country"] == "KEN")
