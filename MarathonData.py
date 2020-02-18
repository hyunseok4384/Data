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

#새로운 칼럼을 만들어주고 타임델타 값으로 변경해서 넣어준다
marathon_2015_2017_clean["Official Time New"] = pd.to_timedelta(marathon_2015_2017_clean["Official Time"])
print(marathon_2015_2017_clean.info())

#타임델타값을 시간:분:초 가 아닌 초 단위로 변경해서 넣어준다
marathon_2015_2017_clean["Official Time Sec"] = marathon_2015_2017_clean["Official Time New"].astype("m8[s]").astype(np.int64)
print(marathon_2015_2017_clean.head())

#데이터들을 새로운 csv파일로 저장
marathon_2015_2017_clean.to_csv("C:\\AI\\data\\marathon_2015_2017.csv")
