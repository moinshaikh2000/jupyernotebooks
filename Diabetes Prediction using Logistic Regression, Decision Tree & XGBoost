#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np

from tensorflow.keras.layers import Dense,Dropout,Input,InputLayer
from tensorflow.keras.models import Sequential

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import *

import matplotlib.pyplot as plt
import seaborn as sns
import glob


# In[2]:


df = pd.read_csv(r"C:\Users\shaik\OneDrive\Desktop\Pyton Class\Data set\Dibeties\diabetes.csv")


# In[3]:


df.head()


# In[5]:


df.shape


# In[6]:


sns.countplot(data=df,x='Outcome')


# In[7]:


sns.heatmap(df.corr())


# In[8]:


df.corr()['Outcome'][:-1].sort_values().plot(kind='bar')


# In[9]:


df.describe()


# In[22]:


len(df.columns)//2


# In[17]:


df = df.astype(float)


# In[19]:


df.dtypes


# In[11]:


num_columns = len(df.columns) - 1
num_rows = (num_columns + 1) // 2

plt.figure(figsize=(10, 5*num_rows))

for i, column in enumerate(df.columns.drop('Outcome')):
    plt.subplot(num_rows, 2, i+1)

    sns.histplot(data=df, x=column, kde=True, fill=True)

    plt.title(f'Histogram with KDE of {column}')

plt.tight_layout()
plt.savefig('foo.png')
plt.savefig('foo.pdf')
plt.show()


# In[25]:


dk=pd.get_dummies(df)


# In[26]:


x= dk.drop(['Outcome'],axis=1)
y= dk['Outcome']


# In[27]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=324)


# In[33]:


model = LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)


# In[35]:


trainPred = model.predict(x_train)
testPred = model.predict(x_test)


# In[36]:


y_predicted = model.predict(x_test)


# In[39]:


y_predictedtrain = model.predict(x_train)


# In[37]:


RocCurveDisplay.from_predictions(y_test,y_predicted)


# In[40]:


RocCurveDisplay.from_predictions(y_train,y_predictedtrain)


# In[51]:


r2_score(y_test,testPred)


# In[52]:


feat_imp = model.coef_


# In[53]:


sns.barplot(x=x_train.columns,y=feat_imp,color='blue')
plt.xticks(rotation=90)
plt.show()


# In[54]:


sns.heatmap(x_train.corr(),annot=True)


# # Trying Decision Tree #

# In[67]:


Diabetes_Predictor=DecisionTreeClassifier(max_leaf_nodes=50,random_state=0)
Diabetes_Predictor.fit(x_train,y_train)


# In[68]:


y_predicted = Diabetes_Predictor.predict(x_test)


# In[69]:


accuracy_score(y_test,y_predicted)*100


# In[70]:


confusion_matrix(y_test,y_predicted)


# In[71]:


RocCurveDisplay.from_predictions(y_test,y_predicted)


# In[72]:


temp = pd.DataFrame()
temp['act']= y_test
temp['score'] = y_predicted


# In[73]:


sns.histplot(x='score',data=temp,binwidth=0.1,hue='act')


# In[11]:


from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans


# In[14]:


n_clusters = [2,3,4,5,6,7,8,9,10]
inertia = []
sil_score = []
for n in n_clusters:
    model = KMeans(n_clusters=n)
    model.fit(df)
    labels = model.predict(df)
    
    inertia.append(model.inertia_)
    score = silhouette_score(df,labels)
    sil_score.append(score)


# In[15]:


sns.lineplot(x=n_clusters,y=inertia)
plt.title('Elbow Curve')
plt.show()


# In[17]:


sns.lineplot(x=n_clusters,y=sil_score)
plt.title('Elbow Curve')
plt.show()


# In[19]:


model = KMeans(n_clusters=4)
model.fit(df)


# In[21]:


labels = model.predict(df)


# In[ ]:





# In[ ]:





# In[ ]:





# # Trying booster model #

# In[3]:


from xgboost import XGBClassifier


# In[1]:


pip install xgboost


# In[12]:


import os


# In[18]:


os.getcwd()


# In[ ]:




