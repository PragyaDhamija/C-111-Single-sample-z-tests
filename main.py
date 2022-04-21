import pandas as pd
import plotly.figure_factory as pff
import statistics as st 
import random
import plotly.graph_objects as pgo

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
fig = pff.create_distplot([data], ["Maths score"], show_hist = False)
#fig.show()
mean = st.mean(data)
std = st.stdev(data)
print("mean of population: ",mean)
print("Std of population: ", std)

def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = st.mean(dataSet)
    return mean
mean_list = []
for i in range(0,1000):
    setOfMeans = randomSetOfMean(100)
    mean_list.append(setOfMeans)
mean = st.mean(mean_list)
std = st.stdev(mean_list)
print("Mean of sample data: ",mean)
print("Std of sample data: ", std)

fig = pff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
#fig.show()

firststdstart,firststdend = mean-std, mean+std
secondstdstart,secondstdend = mean-(2*std), mean+(2*std)
thirdstdstart,thirdstdend = mean-(3*std), mean+(3*std)

fig = pff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(pgo.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))

fig.add_trace(pgo.Scatter(x=[firststdstart, firststdstart], y=[0, 0.17], mode="lines", name="FIRST STD START"))
fig.add_trace(pgo.Scatter(x=[firststdend, firststdend], y=[0, 0.17], mode="lines", name="FIRST STD END"))

fig.add_trace(pgo.Scatter(x=[secondstdstart, secondstdstart], y=[0, 0.17], mode="lines", name="SECOND STD START"))
fig.add_trace(pgo.Scatter(x=[secondstdend, secondstdend], y=[0, 0.17], mode="lines", name="SECOND STD END"))

fig.add_trace(pgo.Scatter(x=[thirdstdstart, thirdstdstart], y=[0, 0.17], mode="lines", name="THIRD STD START"))
fig.add_trace(pgo.Scatter(x=[thirdstdend, thirdstdend], y=[0, 0.17], mode="lines", name="THIRD STD END"))

#fig.show()

# finding the mean of the first data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.
df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()
meanOfSample1 = st.mean(data)
fig = pff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(pgo.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(pgo.Scatter(x=[meanOfSample1, meanOfSample1], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE 1"))
fig.add_trace(pgo.Scatter(x=[firststdend, firststdend], y=[0, 0.17], mode="lines", name="FIRST STD END"))
#fig.show()

# finding the mean of the SECOND data (STUDENTS WHO HAD EXTRA CLASSES ) and plotting it on the plot.
df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()
meanOfSample2 = st.mean(data)
fig = pff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(pgo.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(pgo.Scatter(x=[meanOfSample2, meanOfSample2], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE 2"))
fig.add_trace(pgo.Scatter(x=[firststdend, firststdend], y=[0, 0.17], mode="lines", name="FIRST STD END"))
fig.add_trace(pgo.Scatter(x=[secondstdend, secondstdend], y=[0, 0.17], mode="lines", name="SECOND STD END"))
#fig.show()

# finding the mean of the THIRD data (STUDENTS WHO GOT FUNSHEET) and plotting it on the plot.
df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
meanOfSample3 = st.mean(data)
fig = pff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(pgo.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(pgo.Scatter(x=[meanOfSample3, meanOfSample3], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE 3"))
fig.add_trace(pgo.Scatter(x=[firststdend, firststdend], y=[0, 0.17], mode="lines", name="FIRST STD END"))
fig.add_trace(pgo.Scatter(x=[secondstdend, secondstdend], y=[0, 0.17], mode="lines", name="SECOND STD END"))
fig.add_trace(pgo.Scatter(x=[thirdstdend, thirdstdend], y=[0, 0.17], mode="lines", name="THIRD STD END"))
#fig.show()

#finding the z score using the formula
#zScore = (New Sample Mean - Sampling Distribution Mean) / standard deviation

zScore1 = (meanOfSample1 - mean)/std
print(zScore1)
zScore2 = (meanOfSample2 - mean)/std
print(zScore2)
zScore3 = (meanOfSample3 - mean)/std
print(zScore3)

#If z < 1 or z < 2; the impact of the intervention might not be statistically significant
#Third group from the analysis that were given fun sheets got the best reslut among the three groups...