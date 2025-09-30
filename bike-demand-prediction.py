#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import *

import matplotlib.pyplot as plt
import seaborn as sns
import glob
import calendar


# In[4]:


flist = glob.glob('/kaggle/input/bike-sharing-datasets/*.csv')


# In[7]:


df = pd.DataFrame()

for f in flist:
    if 'divvy' in f:
        temp = pd.read_csv(f)
        df = pd.concat([df,temp],axis =0)


# In[8]:


df.head()


# In[10]:


df['started_at'] = pd.to_datetime(df['started_at'])


# In[13]:


df['started_at'] = df['started_at'].dt.date


# In[14]:


df['start_station_name'].nunique()


# In[16]:


station_demand = pd.DataFrame(df['start_station_name'].value_counts())


# In[20]:


df2 = df.groupby(['started_at','rideable_type','start_station_name','member_casual']).ride_id.count()


# In[21]:


df2.head()


# In[22]:


df2 = df2.reset_index()


# In[23]:


df2.head()


# In[24]:


sns.lineplot(x='started_at',y='ride_id',data=df2)


# In[26]:


df2['started_at'] = pd.to_datetime(df2['started_at'])


# In[34]:


df2['day'] = df2['started_at'].apply(lambda x : x.weekday())
df2['month'] = df2['started_at'].dt.month


# In[54]:


df2['day'].min()


# In[62]:


dayname = dict(enumerate(calendar.day_name))


# In[63]:


dayname


# In[57]:


month_name = dict(enumerate(list(calendar.month_name)))


# In[58]:


month_name


# In[67]:


df2['day'] = df2['day'].apply(lambda x : dayname[x])


# In[68]:


df2['month'] = df2['month'].apply(lambda x : month_name[x])


# In[70]:


sns.boxplot(x='day',y='ride_id',data=df2)


# In[71]:


sns.boxplot(x='month',y='ride_id',data=df2)


# In[73]:


df.columns


# In[76]:


pos = df[['start_station_name','start_lat', 'start_lng']]
pos = pos.round(2)


# In[78]:


pos = pos.dropna()


# In[80]:


pos = pos.drop_duplicates('start_station_name')


# In[81]:


pos.shape


# In[83]:


df2.isnull().sum()


# In[85]:


df2 = pd.merge(df2,pos,on=['start_station_name'])


# In[86]:


df2.isnull().sum()


# In[87]:


df2['start_lat'] = df2['start_lat'].apply(np.radians)
df2['start_lng'] = df2['start_lng'].apply(np.radians)


# In[93]:


data = df2.drop(['started_at','start_station_name'],axis=1)


# In[95]:


data.columns


# In[97]:


data = data.groupby(['rideable_type', 'member_casual', 'day', 'month',
       'start_lat', 'start_lng']).ride_id.mean()


# In[101]:


data = data.reset_index()


# In[102]:


data = pd.get_dummies(data)


# In[103]:


data


# In[104]:


x = data.drop('ride_id',axis=1)
y = data.ride_id


# In[105]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2)


# In[106]:


model = RandomForestRegressor(max_depth = 10,n_estimators=200)
model.fit(x_train,y_train)


# In[107]:


trainPred = model.predict(x_train)
testPred = model.predict(x_test)


# In[108]:


r2_score(y_train,trainPred)


# In[109]:


r2_score(y_test,testPred)


# In[112]:


import optuna


# In[116]:


# 1. Define an objective function to be maximized.
def objective(trial):

    # 2. Suggest values for the hyperparameters using a trial object.
    reg_name = trial.suggest_categorical('regressor', ['LR', 'KNN','DT','RF'])
    
    if reg_name == 'LR':
        model = LinearRegression()
    elif reg_name == 'KNN':
        knn_neg = trial.suggest_int('knn_neg', 3, 23)
        model = KNeighborsRegressor(n_neighbors = knn_neg)
    elif reg_name == 'DT':
        dt_max_depth = trial.suggest_int('dt_max_depth', 2, 32, log=True)
        model = DecisionTreeRegressor(max_depth=dt_max_depth)
    elif reg_name == 'RF':
        rf_max_depth = trial.suggest_int('rf_max_depth', 2, 32, log=True)
        rf_estimators = trial.suggest_int('rf_n_estimators',10,1000)
        model = RandomForestRegressor(max_depth=rf_max_depth, n_estimators=rf_estimators)
    
    score = cross_val_score(estimator=model,X=x_train,y=y_train,scoring='r2')
    return np.mean(score)

# 3. Create a study object and optimize the objective function.
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)


# In[117]:


study.best_params


# In[118]:


study.best_value


# In[119]:


model = DecisionTreeRegressor(max_depth=18)
model.fit(x_train,y_train)


# In[120]:


trainPred = model.predict(x_train)
testPred = model.predict(x_test)


# In[121]:


r2_score(y_test,testPred)


# In[123]:


import pickle


# In[124]:


# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))


# In[ ]:




