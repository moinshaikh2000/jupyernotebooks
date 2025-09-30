#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import yfinance as yf
import time
from tqdm import tqdm
tqdm.pandas()


# In[4]:


df = pd.read_csv('ind_nifty50list.csv')
df.head()


# In[5]:


symbol ='APOLLOHOSP'
url = f'''https://www.screener.in/company/{symbol}/consolidated/'''
print(url)


# In[32]:


data = pd.read_html(url)
data = data[0]
data.rename(columns={'Unnamed: 0':'Header'},inplace=True)
data = data.iloc[:-1,:]
data = data.T
data.columns = data.iloc[0,:]
data = data.iloc[1:,:]
data['symbol'] = symbol


# In[33]:


data


# In[37]:


data = pd.DataFrame()
for i in tqdm(df.Symbol):
    symbol =i
    url = f'''https://www.screener.in/company/{symbol}/consolidated/'''
    temp = pd.read_html(url)
    temp = temp[0]
    temp.rename(columns={'Unnamed: 0':'Header'},inplace=True)
    temp = temp.iloc[:-1,:]
    temp = temp.T
    temp.columns = temp.iloc[0,:]
    temp = temp.iloc[1:,:]
    temp['symbol'] = symbol
    data = pd.concat([data,temp])
    time.sleep(3)


# In[38]:


data


# In[39]:


data.to_csv('nifty50 Fundamental data.csv')


# In[69]:


df_target = pd.DataFrame()
for i in tqdm(df.Symbol):
    ticker = f'''{i}.NS'''
    temp = yf.download(tickers=[ticker])
    temp = temp.asfreq('D')
    temp = temp.fillna(method='ffill')
    temp = temp.asfreq('Q')
    temp['target'] = temp['Adj Close'].pct_change()
    temp['Symbol'] = i
    temp['target'] = temp['target'].shift(-1)
    temp = temp.reset_index()
    df_target = pd.concat([df_target,temp])


# In[70]:


df_target.to_csv('target.csv')


# In[3]:


data = pd.read_csv('nifty50 Fundamental data.csv')
target = pd.read_csv('target.csv')


# In[4]:


data.head()


# In[5]:


data.rename(columns={'Unnamed: 0':'Date'},inplace=True)


# In[6]:


target = target[['Date','Symbol','target']]
target.head()


# In[7]:


data['Date'] = pd.to_datetime(data['Date'])+ pd.offsets.MonthEnd(0) 


# In[8]:


data.columns


# In[9]:


data.rename(columns={'symbol':'Symbol'},inplace=True)


# In[10]:


target.dtypes


# In[11]:


target['Date'] = pd.to_datetime(target['Date'])


# In[12]:


target.head()


# In[13]:


df = pd.merge(data,target,how='left',on=['Date','Symbol'])


# In[14]:


nifty =pd.read_csv('ind_nifty50list.csv')


# In[15]:


nifty = nifty[['Symbol','Industry']]


# In[16]:


df = pd.merge(df,nifty,how='left',on = ['Symbol'])


# In[17]:


df.isnull().sum()/len(df)


# In[18]:


df.drop(['Revenue','Financing Profit','Financing Profit','Gross NPA %',
         'Net NPA %'],axis=1,inplace=True)


# In[19]:


df.isnull().sum()/len(df)


# In[20]:


df.drop(['Financing Margin %'],axis=1,inplace=True)


# In[21]:


df = df[~df['Sales\xa0+'].isnull()]


# In[22]:


df.isnull().sum()/len(df)


# In[23]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[24]:


sns.scatterplot(x='EPS in Rs',y='target',data=df)


# In[25]:


df['OPM %'] = df['OPM %'].apply(lambda x : int(x.replace("%","")))

df['Tax %'] = df['Tax %'].apply(lambda x : int(x.replace("%","")))


# In[26]:


df.columns


# In[27]:


df.columns  = [i.replace(u'\xa0', u' ').replace(" ","_").lower() for i in df.columns]


# In[28]:


sns.scatterplot(x='net_profit_+',y='target',data=df)


# In[29]:


sns.boxplot(x='industry',y='target',data=df)
plt.xticks(rotation= 90)
plt.show()


# In[30]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from xgboost import XGBRegressor


# In[31]:


train = df[df.date < '2023-01-01']
test = df[df.date >= '2023-01-01']


# In[32]:


x_train  = train.drop(['date','symbol','target'],axis=1)
y_train = train.target

x_test = test.drop(['date','symbol','target'],axis=1)
y_test = test.target


# In[33]:


x_train = pd.get_dummies(x_train)


# In[34]:


x_test = pd.get_dummies(x_test)


# In[35]:


model = LinearRegression()
model.fit(x_train,y_train)


# In[36]:


trainPred = model.predict(x_train)
testPred = model.predict(x_test)


# In[37]:


r2_score(y_train,trainPred)


# In[38]:


model = XGBRegressor(n_estimators = 200,max_depth=5)


# In[39]:


model.fit(x_train,y_train)


# In[40]:


trainPred = model.predict(x_train)
testPred = model.predict(x_test)


# In[41]:


r2_score(y_train,trainPred)


# In[46]:


temp = pd.DataFrame()
temp['actual'] = y_test
temp['predict'] = testPred
temp = temp.dropna()
r2_score(temp.actual,temp.predict)


# In[49]:


import optuna
import numpy as np


# In[61]:


# 1. Define an objective function to be maximized.
def objective(trial):
    
    depth = trial.suggest_int('depth',1,10)
    estimators = trial.suggest_int('estimator',10,1000)
    alpha = trial.suggest_float('alpha',0,10)
    _lambda = trial.suggest_float('lambda',0,10)



    model = XGBRegressor(n_estimators = estimators,max_depth=depth,reg_alpha = alpha,reg_lambda = _lambda)
    
    score = cross_val_score(estimator=model,X=x_train,y=y_train,scoring='neg_mean_squared_error')
    return np.mean(score)

# 3. Create a study object and optimize the objective function.
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=20)


# In[62]:


study.best_params


# In[63]:


model = XGBRegressor(max_depth = 2,n_estimators = 436,reg_alpha = 2.13, reg_lambda = 2.89)
model.fit(x_train,y_train)


# In[64]:


trainPred = model.predict(x_train)
testPred = model.predict(x_test)


# In[67]:


np.sqrt(mean_squared_error(y_train,trainPred))


# In[68]:


y_train


# In[ ]:




