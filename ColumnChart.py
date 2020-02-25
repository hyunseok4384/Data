import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

marathon_2015_2017 = pd.read_csv("C:\\AI\\data\\marathon_2015_2017.csv")
#print(marathon_2015_2017.head())

USA_runner = marathon_2015_2017[marathon_2015_2017.Country == "USA"]
print(USA_runner)

"""
#USA에서 참가한 인원수 중에서 주 별로 참가자 인원 수
plt.figure(figsize=(20,10))
runner_state = sns.countplot("State",data=USA_runner)
runner_state.set_title("Number of Runner by State : USA",fontsize=18)
runner_state.set_xlabel("State", fontdict={"size":16})
runner_state.set_ylabel("Number of Runner", fontdict={"size":16})
plt.show()
"""
"""
#USA에서 참가한 인원수 중에서 남녀별로 참가자 인원수
plt.figure(figsize=(20,10))
runner_state = sns.countplot("State",data=USA_runner,hue="M/F",palette={"F":"r","M":"b"})
runner_state.set_title("Number of Runner by State, Gender - USA",fontsize=18)
runner_state.set_xlabel("State", fontdict={"size":16})
runner_state.set_ylabel("Number of Runner", fontdict={"size":16})
plt.show()
"""

"""
#USA에서 참가한 인원수 중에서 년도별 참가자 인원수
plt.figure(figsize=(20,10))
runner_state = sns.countplot("State",data=USA_runner,hue="Year")
runner_state.set_title("Number of Runner by State, Year - USA",fontsize=18)
runner_state.set_xlabel("State", fontdict={"size":16})
runner_state.set_ylabel("Number of Runner", fontdict={"size":16})
plt.show()
"""
