import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random 
import pandas as pd
import csv

df = pd.read_csv("temp.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("Population Mean:",population_mean)
print("Standard_Deviation:",std_deviation)

dataset = [] 
for i in range(0, 100): 
      random_index= random.randint(0,len(data)) 
      value = data[random_index] 
      dataset.append(value) 
mean = statistics.mean(dataset) 
std_deviation = statistics.stdev(dataset) 
      
print("Mean of sample:- ",mean) 
print("std_deviation of sample:- ",std_deviation)

def random_set_of_mean(counter): 
    dataset = [] 
    for i in range(0, counter): 
      random_index= random.randint(0,len(data)-1) 
      value = data[random_index] 
      dataset.append(value) 
      mean = statistics.mean(dataset) 
    return mean

def show_fig(mean_list):
    df = mean_list
    print("Mean of sampling distribution:",mean)
    fig = ff.create_distplot([df],["temp"],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

def setup():
     mean_list = [] 
     for i in range(0,1000):
          set_of_means= random_set_of_mean(100) 
          mean_list.append(set_of_means) 
     show_fig(mean_list) 
          
setup()



def standard_deviation(): 
    mean_list = [] 
    for i in range(0,1000): 
        set_of_means= random_set_of_mean(100) 
        mean_list.append(set_of_means) 

    std_deviation = statistics.stdev(mean_list) 
    print("Standard deviation of sampling distribution:- ", std_deviation) 
        
standard_deviation()
