#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"C:\Users\shaik\OneDrive\Desktop\Pyton Class\Data set\Customer segmentation\train.csv")


# In[3]:


df.head()


# In[4]:


df.isnull().sum()


# In[5]:


df['Ever_Married'].unique()


# In[6]:


df['Ever_Married'].fillna('No',inplace=True)


# In[7]:


df['Graduated'].unique()


# In[8]:


df['Graduated'].fillna('No',inplace=True)


# In[9]:


df['Profession'].unique()


# In[10]:


df['Profession'].fillna('NA',inplace=True)


# In[11]:


df['Work_Experience'].unique()


# In[12]:


df['Work_Experience'].mean()


# In[13]:


df['Work_Experience'].median()


# In[14]:


df['Work_Experience'].fillna(1,inplace=True)


# In[15]:


df['Family_Size'].unique()


# In[16]:


df['Family_Size'].fillna(1,inplace=True)


# In[17]:


df.isnull().sum()


# In[18]:


df['Var_1'].unique()


# In[19]:


df['Var_1'].mode()


# In[20]:


df['Var_1'].fillna('Cat_6',inplace=True)


# In[21]:


df.drop(['ID','Segmentation'],inplace=True,axis=1)


# In[22]:


data = pd.get_dummies(df,drop_first=True)


# In[23]:


data.head()


# In[24]:


n_clusters = [2,3,4,5,6,7,8,9,10]
inertia = []
sil_score = []
for n in n_clusters:
    model = KMeans(n_clusters=n)
    model.fit(data)
    labels = model.predict(data)
    
    inertia.append(model.inertia_)
    score = silhouette_score(data,labels)
    sil_score.append(score)


# In[25]:


sns.lineplot(x=n_clusters,y=inertia)
plt.title('Elbow Curve')
plt.show()


# In[26]:


sns.lineplot(x=n_clusters,y=sil_score)
plt.title('Elbow Curve')
plt.show()


# In[27]:


model = KMeans(n_clusters=4)
model.fit(data)


# In[28]:


labels = model.predict(data)


# In[29]:


labels


# In[30]:


df['Segment']= labels


# In[31]:


sns.scatterplot(df,x='Age',y='Work_Experience',hue='Segment')


# In[32]:


x = df.groupby(['Gender','Segment']).Age.count()
x.reset_index()


# In[33]:


x = pd.pivot_table(df,index='Gender',columns='Segment',values='Age',aggfunc='count')

x


# In[54]:


x = pd.pivot_table(df,index=['Spending_Score'],columns='Segment',values='Age',aggfunc='count')

sns.heatmap(x,annot=True,fmt='g')


# In[34]:


x = pd.pivot_table(df,index=['Spending_Score','Gender'],columns='Segment',values='Age',aggfunc='count')

sns.heatmap(x*100/len(df),annot=True,fmt='g')


# In[ ]:





# In[ ]:




