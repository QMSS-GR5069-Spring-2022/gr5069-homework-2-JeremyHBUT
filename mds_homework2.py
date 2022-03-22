# -*- coding: utf-8 -*-
"""MDS homework2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KfB7yzik0d3g5THb8uox040F6QwHEJHi
"""

"""### import 
import pandas as pd
import numpy as np

CDI = pd.read_csv('data/U.S._Chronic_Disease_Indicators__CDI_.csv')

CDI.head()

CDI.shape

CDI.describe()

"""## Selection of data and Reshaping the data
#### 1. remove all columns that are not needed for the analysis
"""

CDI1 = CDI.query('(Question == "Binge drinking prevalence among adults aged >= 18 years" \
& DataValueType == "Crude Prevalence" \
& StratificationCategoryID1 in ["OVERALL","GENDER"]) \
| (Question == "Poverty" \
& DataValueType == "Crude Prevalence" \
& StratificationCategoryID1 == "OVERALL")')

CDI1.head()

CDI1.shape

CDI2 = CDI1.iloc[:,[0,2,3,6,10,17]]
CDI2.head()

"""#### 2. Convert the dataset to a wide format data set using the commands from the pandas package."""

CDI2_wide = CDI2.pivot(index = ['LocationDesc','LocationAbbr','YearStart'],columns = ['Question','Stratification1'],values = ['DataValue'])
CDI2_wide.head()

"""#### 3. Rename the variables to follow the format below. Provide an overview of the dataset by printing its size (using the shape command) and some summary statistics (using the describe command). Save the cleaned dataset as binge_clean.csv. That file should be included in the uploaded files for your homework submission.

"""

binge_clean = CDI2_wide.reset_index()
list = ['state','stateabb','year','poverty','binge_female','binge_male','binge_all']
binge_clean.columns = list
binge_clean.head()

binge_clean[['binge_female','binge_male','binge_all','poverty']] = binge_clean[['binge_female','binge_male','binge_all','poverty']].astype(float)
binge_clean.describe()

binge_clean.csv = binge_clean.to_csv('Data/binge_clean.csv',index = False)

"""## Data Transformation and Summary Results
#### 4. Produce a table that shows the overall, female, and male binge drinking prevalences across U.S. States in the most recent year of data for the Top 10 binge drinking states (i.e. the ones with the highest prevalence in the overall population). Use the relevant pandas commands to select the right variables, sort the data, and filter the data frame.

Since we don't need the poverty column, just remove that column
"""

binge_clean['binge_all'] = binge_clean['binge_all'].astype(float)

binge_clean_1 = binge_clean.drop('poverty', axis = 1)
binge_clean_1.head()

top_states_year = binge_clean_1.loc[binge_clean_1.groupby('state')['year'].idxmax()]
top_states_10 = top_states_year.sort_values('binge_all',ascending = False).head(10)
top_states_10

"""#### 5. Calculate the average annual growth rates (in percent) of overall binge drinking across states for the years the data is available. One way to get these growth rates, is to group the data by state (groupby) and use the first() and last() commands to get the first and last non-NA percentage followed by dividing the calculated percentage increase by the number of years data is available for. Alternatively, you could use the pct_change function to help you out. Provide a table of the 5 states with the largest increases and the 5 states with the largest decreases in binge drinking prevalence over the time period."""

binge_clean_change = binge_clean[['state','year','binge_all']]
binge_clean_change

binge_clean_change['binge_all'] = binge_clean_change['binge_all'].astype(float)

binge_clean_change['changes'] = binge_clean_change['binge_all'].pct_change()

AvgGrowth = pd.DataFrame(binge_clean_change.groupby('state')['changes'].mean().reset_index(name = 'AverageGrowth'))
AvgGrowth.head()

LargestInc5 = AvgGrowth.sort_values('AverageGrowth',ascending = False).head(5)
LargestInc5

LargestDec5 = AvgGrowth.sort_values('AverageGrowth').head(5)
LargestDec5
