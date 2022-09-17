#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv("All_India_Index_july2019_20Aug2020.csv")


# In[3]:


data.head()


# In[4]:


data=data.drop(['Housing'], axis=1)


# In[5]:


data_rural=data[data['Sector']=='Rural']
data_urban=data[data['Sector']=='Urban']


# In[6]:


data_urban=data_urban.dropna()
data_rural=data_rural.dropna()


# In[7]:


fig = plt.figure(figsize=(10,10))
plt.rcParams.update({'font.size': 14})
plt.scatter(data_urban["Fuel and light"],data_urban["General index"])
plt.scatter(data_urban["Fuel and light"],data_urban["Transport and communication"],marker ="^")
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("fuel and light prices")
plt.ylabel("pricing index")
plt.title("co-relation between fuel and pricing index (Urban)")
plt.legend(["General pricing index", "transport and communication index"], loc ="upper left")


# In[8]:


fig = plt.figure(figsize=(15,15))
plt.rcParams.update({'font.size': 14})
plt.scatter(data_urban["General index"],data_urban["Vegetables"],marker ="^")
plt.scatter(data_urban["General index"],data_urban["Fruits"])
plt.scatter(data_urban["General index"],data_urban["Cereals and products"], marker="s")
plt.gca().set_aspect('equal', adjustable='box')
plt.ylabel("commodity price index")
plt.xlabel("General consumer pricing index")
plt.title("co-relation between vegetables and general pricing index (Urban)")
plt.legend(["vegetables", "fruits","cereals and products"], loc ="upper left")


# In[9]:


fig = plt.figure(figsize=(10,10))
plt.rcParams.update({'font.size': 14})
plt.scatter(data_urban["General index"],data_urban["Sugar and Confectionery"])
plt.scatter(data_urban["General index"],data_urban["Prepared meals, snacks, sweets etc."],marker ="^")
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("General index")
plt.ylabel("pricing index")
plt.title("co-relation between general pricing index and commodity (Urban)")
plt.legend(["Sugar and Confectionery", "Prepared meals, snacks, sweets etc"], loc ="upper left")


# In[10]:


data_urban.head()


# In[11]:


data_urban_2017=data_urban[data_urban['Year']==2017]
months=data_urban_2017["Month"]

data_rural_2017=data_rural[data_rural['Year']==2017]


# In[12]:


temp_data=data_urban_2017.drop(['Sector',"Year","Month"], axis=1)
labels=temp_data.columns
np_urban_2017=temp_data.to_numpy()

temp_data=data_urban_2017.drop(['Sector',"Year","Month"], axis=1)
np_rural_2017=temp_data.to_numpy()


# In[13]:


fig = plt.figure(figsize =(12, 8))
plt.boxplot(np_rural_2017)
x = np.arange(1,27,1)
plt.xticks(x,labels,rotation ='vertical')
#plt.xlabel("commodities")
plt.ylabel("pricing index")
plt.title("variation in pricing index of commodities over the year(Rural)")
plt.show()


# In[14]:


fig = plt.figure(figsize =(12, 8))
plt.boxplot(np_urban_2017)
x = np.arange(1,27,1)
plt.xticks(x,labels,rotation ='vertical')
#plt.xlabel=("commodities")
plt.ylabel("pricing index")
plt.title("variation in pricing index of commodities over the year(Urban)")
plt.show()


# In[15]:


barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
Rural = np_rural_2017[1]
Urban= np_urban_2017[1]
 
# Set position of bar on X axis
br1 = np.arange(len(Rural))
br2 = [x + barWidth for x in br1]
 
# Make the plot
plt.bar(br1, Rural, color ='y', width = barWidth,
        edgecolor ='grey', label ='Rural')
plt.bar(br2, Urban, color ='b', width = barWidth,
        edgecolor ='grey', label ='Urban')
plt.ylim(ymin=100)
# Adding Xticks
plt.ylabel('price index', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Rural))], labels, rotation="vertical")

plt.title("price index of various commodity in rural vs urban")
plt.legend()
plt.show()


# In[17]:


barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
Rural = np_rural_2017[:,25]
Urban= np_urban_2017[:,25]
 
# Set position of bar on X axis
br1 = np.arange(len(Rural))
br2 = [x + barWidth for x in br1]
 
# Make the plot
plt.bar(br1, Rural, color ='y', width = barWidth,
        edgecolor ='grey', label ='Rural')
plt.bar(br2, Urban, color ='b', width = barWidth,
        edgecolor ='grey', label ='Urban')
plt.ylim(ymin=100)
# Adding Xticks
plt.ylabel('general price index', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Rural))], months, rotation="vertical")

plt.title("price index of various commodity in rural vs urban")
plt.legend()
plt.show()


# In[ ]:




