#!/usr/bin/env python
# coding: utf-8

# #  Tech Layoffs

# ### Source: https://www.kaggle.com/datasets/theakhilb/layoffs-data-2022
# #### Data is updated weekly. This was Pulled off March 19th 2023.
# 
# ### Continue to Explore on the Tableau Public Dashboard: 
# #### https://public.tableau.com/app/profile/grant.hakanson/viz/TechLayoofsProject/GlobalTechLayoffs

# ## Load and Explore the Data

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# Load CSV
lf_data = pd.read_csv('/Users/granthakason/Downloads/layoffs_data.csv')


# In[3]:


# A Head view
lf_data.head(4)


# In[4]:


#use .info() to identify potential Null Values in fields.
lf_data.info()


# In[5]:


# Value Counts Summary
for col in lf_data.columns:
    vc = lf_data[col].value_counts()
    print(f"{col}:")
    print(vc)


# In[6]:


#Removing records and fields with unnesessary data. 
lf_data = lf_data.loc[lf_data['Date'].notnull()]
lf_data = lf_data.drop('List_of_Employees_Laid_Off', axis=1)
lf_data.tail(3)


# # Statistics Information
# #### Note the median will be used to sub in for values that are null. Although it is not the optimum approach it is the best way to adjust data to display data visualization skill one we get to the Tableau stage. 

# In[7]:


# Statistics Information
lf_data.describe()


# ### Filling in Null Values

# In[8]:


# fill null values in 'Laid_Off_Count' column with median value
lf_data['Laid_Off_Count'].fillna(lf_data['Laid_Off_Count'].median(), inplace=True)

# fill null values in 'Percentage' column with value .17
lf_data['Percentage'].fillna(.17, inplace=True)

# fill null values in 'Funds_Raised' column with value 157
lf_data['Funds_Raised'].fillna(157, inplace=True)


# ### Handling Outliers

# #### Laid_Off_Count Outliers

# In[9]:


# Making things easier to digest visually.
stage_plots = lf_data.loc[lf_data['Stage'].isin(['Series F','Post-IPO','Acquired', 'Series C', 'Series B', 'Series A', 'Series E', 'Series D'])]
stage_plotz = lf_data.loc[lf_data['Stage'].isin(['Series H', 'Series G', 'Subsidiary', 'Series G', 'Seed', 'Private Equity', 'Series J', 'Series I'])]  


# In[10]:


# Observing the distribution of the value being explored.
sns.kdeplot(lf_data['Laid_Off_Count'])


# In[11]:


# Box Plot Analysis 1
plt.figure(figsize=(16,10))
plt.legend(loc=0)
sns.boxplot(x='Stage',y='Laid_Off_Count', data=stage_plots,)


# In[12]:


# Box Plot Analysis 2
plt.figure(figsize=(16,10))
plt.legend(loc=0)
sns.boxplot(x='Stage',y='Laid_Off_Count', data=stage_plotz, hue='Stage')


# #### Removing the Laid_Off_Count Outliers.

# In[13]:


cln_lf_data = lf_data.loc[(lf_data['Laid_Off_Count'] <= 500) & (lf_data['Laid_Off_Count'] >= 10)]


# In[16]:


cln_lf_data.to_csv('Tech_Layoffs_Project.csv', index=False)


# # Continue to Explore on the Tableau Public Dashboard: 
# ### https://public.tableau.com/app/profile/grant.hakanson/viz/TechLayoofsProject/GlobalTechLayoffs
