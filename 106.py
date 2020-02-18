import pandas as pd
import numpy as np

marathon_2015 = pd.read_csv("C:\\AI\\data\\marathon_results_2015.csv")
marathon_2016 = pd.read_csv("C:\\AI\\data\\marathon_results_2016.csv")
marathon_2017 = pd.read_csv("C:\\AI\\data\\marathon_results_2017.csv")

marathon_2015["Year"] = "2015"
marathon_2016["Year"] = "2016"
marathon_2017["Year"] = "2017"

marathon_2015["Senior"] = marathon_2015.Age > 60
marathon_2016["Senior"] = marathon_2016.Age > 60
marathon_2017["Senior"] = marathon_2017.Age > 60


marathon_2015_2017 = pd.concat([marathon_2015,marathon_2016,marathon_2017],ignore_index=True,sort=False).set_index("Official Time")
print(marathon_2015_2017.describe())

#나이를 기준으로 오름차순 정렬
marathon_2015_2017.sort_values(by=["Age"])

#나이를 기준으로 내림차순 정렬
marathon_2015_2017.sort_values(by=["Age"],ascending=False)

marathon_2015_2017.to_csv("C:\\AI\\data\\marathon_2015_2017.csv",index=None,header=True)
