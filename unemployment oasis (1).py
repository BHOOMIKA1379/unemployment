#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


data=pd.read_csv("C:/Users/bhoomika tadala/Downloads/unemployment oasis.csv")


# In[13]:


print(data.describe)


# In[14]:


data.info


# In[3]:


print(data.head())


# In[6]:


print(data.isnull().sum())


# In[7]:


data.columns=["Region","Date","Frequency","Estimated Unemployment Rate (%)","Estimated Employed", "Estimated Labour Participation Rate (%)","Area"]


# In[8]:


print(data)


# In[9]:


plt.style.use("seaborn-whitegrid")
plt.figure(figsize=(12,10))
sns.heatmap(data.corr())
plt.show()


# In[15]:


plt.figure(figsize=(12,10))
plt.title("Indian Unemployement")
sns.histplot(x="Estimated Unemployment Rate (%)",hue="Region",data=data)
plt.show()


# In[10]:


data.columns=["Region","Date","Frequency","Estimated Unemployment Rate (%)","Estimated Employed", "Estimated Labour Participation Rate (%)","Area"]
plt.title("Indian unmeployment")
sns.histplot(x="Estimated Employed",hue="Region",data=data)
plt.show()


# In[12]:


un=data[["Region","Area","Estimated Unemployment Rate (%)"]]
print(un)


# In[ ]:





# In[ ]:





# In[ ]:




