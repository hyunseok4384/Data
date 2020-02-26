import pandas as pd
import matplotlib.pyplot as plt

marathon_2015_2017 = pd.read_csv("C:\\AI\\data\\marathon_2015_2017.csv")

#나이가 18살 이상 60세 미만인 사람들만 추려내서 저장
runner_1860 = marathon_2015_2017[marathon_2015_2017.Age.isin(range(18,60))]

#연령별로 카운터 해준다
runner_1860_counting = runner_1860["Age"].value_counts()
print(runner_1860_counting)

#연령만 추려내서 x에 저장해준다
x = runner_1860_counting.index

#x 값을 스트링값으로 변환해서 다시 넣어준다(안해주면 18세부터 정렬돠어버림)
x = [str(i) for i in x]

#인원수만 추려내서 y에 저장해준다
y = runner_1860_counting.values

#퍼센테이지 구하기
ratio = y / y.sum()

#값들이 계속 누적되어지면서 나온다
ratio_sum = ratio.cumsum()

#Configure figure size
fig, barChart = plt.subplots(figsize=(20,10))

#Create bar Chart
barChart.bar(x,y)

#Create Line LineChart
lineChart = barChart.twinx()
lineChart.plot(x, ratio_sum, "-ro", alpha=0.5)

#Create right side labels
ranges = lineChart.get_yticks()
lineChart.set_yticklabels(["{:,.1%}".format(x) for x in ranges])

#Create annotations on line chart
ratio_sum_percentages = ["{0:.0%}".format(x) for x in ratio_sum]
for i, txt in enumerate(ratio_sum_percentages):
    lineChart.annotate(txt, (x[i], ratio_sum[i]), fontsize=14)

barChart.set_xlabel("Age", fontdict={"size":16})
barChart.set_ylabel("Number of runner", fontdict = {"size":16})
plt.title("Pareto Chart - Number of runner by Age", fontsize=18)
plt.show()
