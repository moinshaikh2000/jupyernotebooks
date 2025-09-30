#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd

from tensorflow.keras.layers import Dense,Dropout,Input,InputLayer
from tensorflow.keras.models import Sequential

from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.utils import compute_class_weight

import seaborn as sns


# In[6]:


df = pd.read_csv('/kaggle/input/personal-key-indicators-of-heart-disease/2020/heart_2020_cleaned.csv')


# In[7]:


df.columns


# In[8]:


df.head()


# In[23]:


data = pd.get_dummies(df,drop_first=True,dtype=float)


# In[24]:


data.dtypes


# In[25]:


x = data.drop('HeartDisease_Yes',axis=1)
y = data.HeartDisease_Yes


# In[26]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)


# In[27]:


n_features = x_train.shape[1]
n_features


# In[64]:


model = Sequential([
    Input(shape=(n_features,)),
    Dense(128,activation='relu'),
    Dropout(0.2),
    Dense(1,activation='sigmoid')
])


# In[65]:


model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['Precision','Recall'])


# In[66]:


compute_class_weight(class_weight='balanced',classes=y_train.unique(),y=y_train)


# In[67]:


sum(y_train)/len(y_train)


# In[70]:


history = model.fit(x_train,y_train.values,epochs=10,validation_split=0.2,class_weight={0:1,1:12})


# In[82]:


test_probs = model.predict(x_test)


# In[87]:


test_probs = test_probs.reshape(-1,)


# In[88]:


RocCurveDisplay.from_predictions(y_test,test_probs)


# In[89]:


temp = pd.DataFrame()
temp['act']= y_test
temp['score'] = test_probs


# In[93]:


sns.histplot(x='score',data=temp,binwidth=0.1,hue='act')


# In[109]:


model.predict(np.array(x_test.loc[301988,:].values).reshape(1,-1))[0][0]*100


# In[110]:


x_test.columns


# In[105]:


from xgboost import XGBClassifier
import numpy as np


# In[72]:


clf = XGBClassifier(scale_pos_weight = 8,n_estimators=100)


# In[73]:


clf.fit(x_train,y_train)


# In[74]:


train_probs = clf.predict_proba(x_train)[:,1]
test_probs = clf.predict_proba(x_test)[:,1]


# In[75]:


RocCurveDisplay.from_predictions(y_test,test_probs)


# In[77]:


print(classification_report(y_test,clf.predict(x_test)))


# In[ ]:




