# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RVeX7HQyVwmC2UmvUUTeya2nHpawTPo3
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from google.colab  import files
from io import StringIO
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier  
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report, confusion_matrix
import warnings
import pickle
from scipy import stats 
warnings.filterwarnings('ignore')
plt.style.use('fivethirtyeight') 

data = files.upload()

data = pd.read_csv(io.StringIO(data['Data_Train.csv'].decode('utf-8')))
data.head

from pandas.core.base import unique1d
for i in data :
  print(i, data[i],unique1d(i))

data.info()

data.Date_of_Journey=data.Date_of_Journey.str.split('/')
data.Date_of_Journey

data['Date']=data.Date_of_Journey.str[0]
data['Month']=data.Date_of_Journey.str[1]
data['Year']=data.Date_of_Journey.str[2]
data.Total_Stops.unique()

data.Route=data.Route.str.split('→')
data.Route

data['City1']=data.Route.str[0]
data['City1']=data.Route.str[1]
data['City2']=data.Route.str[2]
data['City3']=data.Route.str[3]

data.Dep_Time=data.Dep_Time.str.split(':')
data['Dep_Time_Hour']=data.Dep_Time.str[0]
data['Dep_Time_Mins']=data.Dep_Time.str[1]

data.Arrival_Time=data.Arrival_Time.str.split(' ')

data['Arrival_date']=data.Arrrival_Time.str[1]
data['Time_of_Arrival']=data.Arrrival_Time.str[0]

data['Time_of_Arrival']=data.Time_of_Arrrival.str.split(':')

data['Arrival_Time_Hour']=data.Time_of_Arrival.str[0]
data['Arrival_Time_Mins']=data.Time_of_Arrival.str[1]

data.Duration=data.Duration.str.split('')

data['Travel_Hours']=data.Duration.str[0]
data['Travel_Hours']=data['Travel_Hours'].str.split('h')
data['Travel_Hours']=data['Travel_Hours'].str[0]
data.Travel_Hour=data.Travel_Hours
data['Travel_Mins']=data.Duration.str[1]

data.travel_Mins=data.Travel_Mins.str.split('m')
data.travel_Mins=data.Travel_Mins.str[0]

data.Duration=data.Duration.str.split('')

data['Travel_Hour']=data.Duration.str[0]
data['Travel_Hour']=data['Travel_Hours'].str.split('h')
data['Travel_Hour']=data['Travel_Hours'].str[0]
data.Travel_Hours=data.Travel_Hours
data['Travel_Mins']=data.Duration.str[1]

data.Travel_Mins=data.Travel_Mins.str.split('m')
data.Travel_Mins=data.Travel_Mins.str[0]

data.Total_Stops.replace('non_stop',0,inplace=True)
data.Total_Stops=data.Total_Stops.str.split(' ')
data.Total_Stops+data.Toyal_Stops.str[0]

data.Additional_info.unique()

data.isnull().sum()

