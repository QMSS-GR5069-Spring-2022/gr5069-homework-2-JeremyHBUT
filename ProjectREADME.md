Data Wrangling
============================

The objective of this assignment is to wrangle a data set and produce some summary statistics for binge drinking prevalence and poverty in U.S. States. 

## Data

The data we want to use are the [U.S. Chronic Disease Indicators (CDI)](https://data.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators-CDI-/g4ie-h725). Download the data in .csv format (use `read_csv()` in pandas). Also, please exclude that data file from uploading to your Github repository by [adding it to your `.gitignore file`](https://caltechlibrary.github.io/git-desktop/05-ignore/).

## Selection of Data and Reshaping the Data

The data contains lots of indicators and is in a long format format. 

1. Remove all columns you do not need for the analysis (All done in Python, of course. No Excel acrobatics.). We are interested in two sets of variables. Select the following variables and remove all others:  
    a) **Binge Drinking**:
    _Binge drinking prevalence among adults aged >= 18 years_, Crude Prevalence in Percent. 
    We would like to obtain this variable for the overall population, as well separately for _females_ and _males_.  
    b) **Poverty**:
    _Poverty, Crude Prevalence in Percent_. We only want the overall poverty prevalence to make things a bit easier.

2. Convert the dataset to a wide format data set using the commands from the `pandas` package.

3. Rename the variables to follow the format below.

    Your dataset should now be in a wide state-year format with the following variables:  
      - `state`: Name of the State  
      - `stateabb`: State Abbreviation  
      - `year`: year of observation  
      - `binge_all`: Binge drinking prevalence among _all_ adults aged >= 18 years  
      - `binge_male`: Binge drinking prevalence among _male_ adults aged >= 18 years  
      - `binge_female`: Binge drinking prevalence among _female_ adults aged >= 18 years  
      - `poverty`: Poverty, Crude Prevalence in Percent  
    
    Provide an overview of the dataset by printing its size (using the `shape` command) and some summary statistics (using the `describe` command).
      
    Save the cleaned dataset as `binge_clean.csv`. That file should be included in the uploaded files for your homework submission.

## Data Transformation and Summary Results

4. Produce a table that shows the overall, female, and male binge drinking prevalences across U.S. States in the most recent year of data for the Top 10 binge drinking states (i.e. the ones with the highest prevalence in the overall population). Use the relevant `pandas` commands to select the right variables, sort the data, and filter the data frame.

5. Calculate the average annual growth rates (in percent) of overall binge drinking across states for the years the data is available. One way to get these growth rates, is to group the data by state (`groupby`) and use the `first()` and `last()` commands to get the first and last non-NA percentage followed by dividing the calculated percentage increase by the number of years data is available for. Alternatively, you could use the `pct_change` function to help you out. Provide a table of the _5 states with the largest increases_ and the _5 states with the largest decreases_ in binge drinking prevalence over the time period. 


## Submission

Please follow the [instructions](/Exercises/homework_submission_instructions.md) to submit your homework. The homework is due on Wedndesday, October 6 at 5pm.

To reiterate, please do **not** include the original full data set in your submission. Add the file to your `.gitignore` file or in  the Gitkraken App right-click on the data file and choose "ignore" to prevent the data from being uploaded. Do include the cleaned dataset `binge_clean.csv` however.