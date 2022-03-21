#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Import necessry functions
import pandas as pd
import numpy as np


# ### Data

# #### Load the data from https://chronicdata.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators-CDI-/g4ie-h725

# In[14]:


CDI = pd.read_csv('data/U.S._Chronic_Disease_Indicators__CDI_.csv')


# In[15]:


CDI.head()


# In[17]:


### get summary of the dataset
CDI.describe()


# ## Selection of data and Reshaping the data
# #### 1. remove all columns that are not needed for the analysis
# 
# Here, I will filter the data so it will only have information on
#     a) **Binge Drinking**:
#     _Binge drinking prevalence among adults aged >= 18 years_, Crude Prevalence in Percent. 
#     For _overall_ population, _females_ only, and _males_ only.  
#     b) **Poverty**:
#     _Poverty, Crude Prevalence in Percent_ only for overall population.

# In[22]:


CDI1 = CDI.query('(Question == "Binge drinking prevalence among adults aged >= 18 years" & DataValueType == "Crude Prevalence" & StratificationCategoryID1 in ["OVERALL","GENDER"]) | (Question == "Poverty" & DataValueType == "Crude Prevalence" & StratificationCategoryID1 == "OVERALL")')


# In[23]:


CDI1.head()


# In[25]:


CDI2 = CDI1.iloc[:,[0,2,3,6,10,17]]
CDI2.head()


# #### 2. Convert the dataset to a wide format data set using the commands from the pandas package.

# In[26]:


CDI2_wide = CDI2.pivot(index = ['LocationDesc','LocationAbbr','YearStart'],columns = ['Question','Stratification1'],values = ['DataValue'])
CDI2_wide.head()


# #### 3. Rename the variables to follow the format below. Provide an overview of the dataset by printing its size (using the shape command) and some summary statistics (using the describe command). Save the cleaned dataset as binge_clean.csv. That file should be included in the uploaded files for your homework submission.
# 

# In[27]:


binge_clean = CDI2_wide.reset_index()
list = ['state','stateabb','year','poverty','binge_female','binge_male','binge_all']
binge_clean.columns = list
binge_clean.head()


# In[28]:


binge_clean[['binge_female','binge_male','binge_all','poverty']] = binge_clean[['binge_female','binge_male','binge_all','poverty']].astype(float)

### Summary of new cleaned data
binge_clean.describe()


# In[29]:


### Save the cleaned data
binge_clean.csv = binge_clean.to_csv('Data/binge_clean.csv',index = False)


# ## Data Transformation and Summary Results
# #### 4. Produce a table that shows the overall, female, and male binge drinking prevalences across U.S. States in the most recent year of data for the Top 10 binge drinking states (i.e. the ones with the highest prevalence in the overall population). Use the relevant pandas commands to select the right variables, sort the data, and filter the data frame.

# Since we don't need the poverty column, just remove that column

# In[30]:


binge_clean['binge_all'] = binge_clean['binge_all'].astype(float)


# In[31]:


binge_clean_1 = binge_clean.drop('poverty', axis = 1)
binge_clean_1.head()


# We know from the describe function above, the most recent year is 2019 so I will filter the data to 2019 only first and select the variables of interest. Then, using `nlargest` to sort and select the top 10 states

# In[32]:


top_states_year = binge_clean_1.loc[binge_clean_1.groupby('state')['year'].idxmax()]
top_states_10 = top_states_year.sort_values('binge_all',ascending = False).head(10)
top_states_10                                                                     


# #### 5. Calculate the average annual growth rates (in percent) of overall binge drinking across states for the years the data is available. One way to get these growth rates, is to group the data by state (groupby) and use the first() and last() commands to get the first and last non-NA percentage followed by dividing the calculated percentage increase by the number of years data is available for. Alternatively, you could use the pct_change function to help you out. Provide a table of the 5 states with the largest increases and the 5 states with the largest decreases in binge drinking prevalence over the time period.

# In[52]:


binge_clean_change = binge_clean[['state','year','binge_all']]
binge_clean_change


# In[53]:


binge_clean_change['binge_all'] = binge_clean_change['binge_all'].astype(float)


# In[66]:


binge_clean_change['changes'] = binge_clean_change['binge_all'].pct_change()


# In[68]:


AvgGrowth = pd.DataFrame(binge_clean_change.groupby('state')['changes'].mean().reset_index(name = 'AverageGrowth'))
AvgGrowth.head()


# #### This is the table of _5 states with the largest annual increases_

# In[69]:


LargestInc5 = AvgGrowth.sort_values('AverageGrowth',ascending = False).head(5)
LargestInc5


# #### This is the table of _5 states with the largest annual decreases_

# In[71]:


LargestDec5 = AvgGrowth.sort_values('AverageGrowth').head(5)
LargestDec5

