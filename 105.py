import pandas as pd
import numpy as np

marathon_2017 = pd.read_csv("C:\\AI\\data\\marathon_results_2017.csv")

marathon_2017_clean = marathon_2017.drop(['Unnamed: 0','Bib','Unnamed: 9'],axis="columns")
#print(marathon_2017_clean)

marathon_2017_clean["Year"] = "2017"
marathon_2017_clean["Senior"] = marathon_2017_clean.Age > 60
print(marathon_2017_clean.head())
print("--------------------------------------------------")

"""
#유저 디파인 함수로 오피셜 타임을 초단위로 바꿔주는것
def to_seconds(record):
    hms = record.str.split(":", n = 2, expand = True)
    return hms[0].astype(int)*3600 + hms[1].astype(int)*60 + hms[2].astype(int)

marathon_2017["Official Time Sec"] = to_seconds(marathon_2017["Official Time"])
print(marathon_2017.head())
print("---------------------------------------------------")
"""

#내장함수를 통해서 오피셜 타임을 초단위로 바꿔주는것
marathon_2017["Official Time Sec"] = pd.to_timedelta(marathon_2017["Official Time"])
#->pd.to_timedelta로 "Official Time"을 타임 델타 값으로 바꿔준뒤 "Official Time Sec" 칼럼에다가 넣어준다

marathon_2017["Official Time New"] = marathon_2017["Official Time Sec"].astype("m8[s]").astype(np.int64)
#->"Official Time Sec"에서 시간을 가져온뒤 astype("m8[s]")로 초 단위로 바꿔준뒤 astype(np.int64)로 인트형으로 바꿔준다
print(marathon_2017)
