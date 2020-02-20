import pandas as pd
import numpy as np

marathon_2015 = pd.read_csv("C:\\AI\\data\\marathon_results_2015.csv")
marathon_2016 = pd.read_csv("C:\\AI\\data\\marathon_results_2016.csv")
marathon_2017 = pd.read_csv("C:\\AI\\data\\marathon_results_2017.csv")

#년도별 새로운 칼럼 추가
marathon_2015["Year"] = "2015"
marathon_2016["Year"] = "2016"
marathon_2017["Year"] = "2017"

#2015 ~ 2017까지의 csv파일을 합치기
marathon_2015_2017 = pd.concat([marathon_2015,marathon_2016,marathon_2017],ignore_index=True,sort=False)
print(marathon_2015_2017.head())
print(marathon_2015_2017.info())
print("---------------------------------------------------------")

#칼럼당 널이 들어있는 합계 출력한 후에 필요없는 칼럼 삭제
print(marathon_2015_2017.isnull().sum(axis=0))
marathon_2015_2017_clean = marathon_2015_2017.drop(["Unnamed: 0","Bib","Citizen","Unnamed: 9","Proj Time"],axis="columns")
print("---------------------------------------------------------")
print(marathon_2015_2017_clean.info())

#타임델타 값으로 변경해서 값을 넣어준다
marathon_2015_2017_clean["Official Time"] = pd.to_timedelta(marathon_2015_2017_clean["Official Time"])
marathon_2015_2017_clean["5K"] = pd.to_timedelta(marathon_2015_2017_clean["5K"])
marathon_2015_2017_clean["10K"] = pd.to_timedelta(marathon_2015_2017_clean["10K"])
marathon_2015_2017_clean["15K"] = pd.to_timedelta(marathon_2015_2017_clean["15K"])
marathon_2015_2017_clean["20K"] = pd.to_timedelta(marathon_2015_2017_clean["20K"])
marathon_2015_2017_clean["Half"] = pd.to_timedelta(marathon_2015_2017_clean["Half"])
marathon_2015_2017_clean["25K"] = pd.to_timedelta(marathon_2015_2017_clean["25K"])
marathon_2015_2017_clean["30K"] = pd.to_timedelta(marathon_2015_2017_clean["30K"])
marathon_2015_2017_clean["35K"] = pd.to_timedelta(marathon_2015_2017_clean["35K"])
marathon_2015_2017_clean["40K"] = pd.to_timedelta(marathon_2015_2017_clean["40K"])
marathon_2015_2017_clean["Pace"] = pd.to_timedelta(marathon_2015_2017_clean["Pace"])
print(marathon_2015_2017_clean.info())

#타임델타값을 시간:분:초 가 아닌 초 단위로 변경해서 넣어준다
marathon_2015_2017_clean["Official Time"] = marathon_2015_2017_clean["Official Time"].astype("m8[s]").astype(np.int64)
marathon_2015_2017_clean["5K"] = marathon_2015_2017_clean["5K"].astype("m8[s]").astype(np.int64)
marathon_2015_2017_clean["10K"] = marathon_2015_2017_clean["10K"].astype("m8[s]").astype(np.int64)
marathon_2015_2017_clean["15K"] = marathon_2015_2017_clean["15K"].astype("m8[s]").astype(np.int64)
marathon_2015_2017_clean["20K"] = marathon_2015_2017_clean["20K"].astype("m8[s]").astype(np.int64)
marathon_2015_2017_clean["Half"] = marathon_2015_2017_clean["Half"].astype("m8[s]").astype(np.int64)
marathon_2015_2017_clean["25K"] = marathon_2015_2017_clean["25K"].astype("m8[s]").astype(np.int64)
marathon_2015_2017_clean["30K"] = marathon_2015_2017_clean["30K"].astype("m8[s]").astype(np.int64)
marathon_2015_2017_clean["35K"] = marathon_2015_2017_clean["35K"].astype("m8[s]").astype(np.int64)
marathon_2015_2017_clean["40K"] = marathon_2015_2017_clean["40K"].astype("m8[s]").astype(np.int64)
marathon_2015_2017_clean["Pace"] = marathon_2015_2017_clean["Pace"].astype("m8[s]").astype(np.int64)
print(marathon_2015_2017_clean.head())

#데이터들을 새로운 csv파일로 저장
marathon_2015_2017_clean.to_csv("C:\\AI\\data\\marathon_2015_2017.csv")
