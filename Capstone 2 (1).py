#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
from collections import Counter

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, losses
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout, RepeatVector, TimeDistributed 
from sklearn.metrics import classification_report

from collections import Counter
from sklearn.datasets import make_classification


# In[3]:


df = pd.read_csv(r"C:\Users\shaik\OneDrive\Desktop\Pyton Class\Data set\Nifty closing price\spx.csv", parse_dates=['date'], index_col='date') 

df.head()


# In[4]:


plt.plot(df, label='close price') 
plt.legend()


# In[15]:


dk=pd.get_dummies(df)


# In[16]:


dk


# In[17]:


x= dk.drop(['close'],axis=1)
y= dk['close']


# In[18]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=40)


# In[8]:


train_size = int(len(df) * 0.95)
test_size = len(df) - train_size
train, test = df.iloc[0:train_size], df.iloc[train_size:len(df)] 
print(train.shape, test.shape)
scaler = StandardScaler()
scaler = scaler.fit(train[['close']])
train['close'] = scaler.transform(train[['close']]) 
test['close'] = scaler.transform(test[['close']])


# In[9]:


def create_seq(X, y, time_steps=1): 
    Xs, ys = [], []
    for i in range(len(X) - time_steps):
        v = X.iloc[i:(i + time_steps)].values 
        Xs.append(v)
        ys.append(y.iloc[i + time_steps])
    return np.array(Xs), np.array(ys)


# In[13]:


TIME_STEPS = 30


# In[14]:


X_train, y_train = create_seq(train[['close']], train.close, TIME_STEPS)
X_test, y_test = create_seq(test[['close']], test.close, TIME_STEPS)


# In[23]:


keras = tf.keras


# In[24]:


model = tf.keras.models.Sequential() 
model.add(keras.layers.LSTM(units=64,input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(keras.layers.Dropout(rate=0.2)) 
model.add(keras.layers.RepeatVector(n=X_train.shape[1])) 
model.add(keras.layers.LSTM(units=64, return_sequences=True)) 
model.add(keras.layers.Dropout(rate=0.2))
model.add(keras.layers.TimeDistributed( keras.layers.Dense(units=X_train.shape[2])))

model.compile(loss='mae', optimizer='adam')


# In[25]:


model.summary()


# In[26]:


history = model.fit( X_train, y_train, epochs=10, batch_size=32, 
                    validation_split=0.1, shuffle=False)


# In[27]:


plt.plot(history.history['loss'], label='Training loss') 
plt.plot(history.history['val_loss'], label='Validation loss') 
plt.legend()


# In[28]:


model.evaluate(X_test, y_test)


# In[29]:


X_train_pred = model.predict(X_train)
train_mae_loss = np.mean(np.abs(X_train_pred - X_train), axis=1)


# In[30]:


sns.distplot(train_mae_loss, bins=50, kde=True)


# In[39]:


THRESHOLD = 0.75
X_test_pred = model.predict(X_test)
test_mae_loss = np.mean(np.abs(X_test_pred - X_test), axis=1)


# In[40]:


test_score_df = pd.DataFrame(index=test[TIME_STEPS:].index) 
test_score_df['loss'] = test_mae_loss
test_score_df['threshold'] = THRESHOLD
test_score_df['anomaly'] = test_score_df.loss > test_score_df.threshold 
test_score_df['close'] = test[TIME_STEPS:].close


# In[41]:


plt.plot(test_score_df.index, test_score_df.loss, label='loss') 
plt.plot(test_score_df.index, test_score_df.threshold, label='threshold') 
plt.xticks(rotation=25)
plt.legend()


# In[42]:


anomalies = test_score_df[test_score_df.anomaly == True] 
anomalies.head()


# In[43]:


anomalies_close = anomalies[["close"]].values.flatten()
anomalies_close = anomalies_close.reshape(-1, 1) # Reshape to a 2D array
anomalies_close = scaler.inverse_transform(anomalies_close)

plt.plot(test[TIME_STEPS:].index, 
         scaler.inverse_transform(test[TIME_STEPS:][["close"]]), 
         label='close price')

# convert it to a 1D array for the plot
anomalies_close = anomalies_close.flatten()
sns.scatterplot(x=anomalies.index, 
                y=anomalies_close, 
                color=sns.color_palette()[3], 
                label='anomaly'
               )

plt.xticks(rotation=25) 
plt.legend()


# In[ ]:




