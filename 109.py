import statistics as st
import csv
import plotly_express as px 
import plotly.figure_factory as ff 
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
reading_score = df["reading score"].tolist()
fig = ff.create_distplot([reading_score],["reading score"],show_hist=False)
fig.show()
mean = st.mean(reading_score)
print("mean:",mean)
std = st.stdev(reading_score)
print("standard deviation:",std)
SD1_START,SD1_END = mean-std,mean+std
SD2_START,SD2_END = mean-(2*std),mean-(2*std)
SD3_START,SD3_END = mean-(3*std),mean-(3*std)
listdata_1SD = [result for result in reading_score if result>SD1_START and result<SD1_END]
listdata_2SD = [result for result in reading_score if result>SD2_START and result<SD2_END]
listdata_3SD = [result for result in reading_score if result>SD3_START and result<SD3_END]
print("{}% of data lies between 1SD".format(len(listdata_1SD)*100.0/len(reading_score)))
print("{}% of data lies between 2SD".format(len(listdata_2SD)*100.0/len(reading_score)))
print("{}% of data lies between 3SD".format(len(listdata_3SD)*100.0/len(reading_score)))