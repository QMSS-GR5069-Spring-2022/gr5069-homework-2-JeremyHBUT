setwd('/Users/liuyadong/Desktop/APAN/semester_2/5205/final_project')

rawdata <- read.csv(file = 'rawdata.csv',stringsAsFactors = F)

library(dplyr)
glimpse(rawdata)

#Drop columns of artists, id, name
data = subset(rawdata, select = -c(artists, id, name))

#Keep the decimals of column energy, liveness, loudness, instrumentalness, speechiness, liveness, tempo
data$energy = round(data$energy, digits=5)
data$liveness = round(data$liveness, digits=5)
data$loudness = round(data$loudness, digits=5)
data$instrumentalness = round(data$instrumentalness, digits=5)
data$speechiness = round(data$speechiness, digits=5)
data$liveness = round(data$liveness, digits=5)
data$tempo = round(data$tempo, digits=5)

#change the data type of column year
data$year = as.integer(data$year)

#separate years
data_1921to1930 <- data %>% filter(year >= 1921 & year <= 1930)
data_1931to1940 <- data %>% filter(year >= 1931 & year <= 1940)
data_1941to1950 <- data %>% filter(year >= 1941 & year <= 1950)
data_1951to1960 <- data %>% filter(year >= 1951 & year <= 1960)
data_1961to1970 <- data %>% filter(year >= 1961 & year <= 1970)
data_1971to1980 <- data %>% filter(year >= 1971 & year <= 1980)
data_1981to1990 <- data %>% filter(year >= 1981 & year <= 1990)
data_1991to2000 <- data %>% filter(year >= 1991 & year <= 2000)
data_2001to2010 <- data %>% filter(year >= 2001 & year <= 2010)
data_2011to2020 <- data %>% filter(year >= 2011 & year <= 2020)

# generate new cleaned data files
install.packages('openxlsx')
install.packages('writexl')
library(xlsx)
require(openxlsx)
library(writexl)
CleanedData <- list("data_1921to1930" = data_1921to1930, "data_1931to1940" = data_1931to1940,
                    "data_1941to1950" = data_1941to1950, "data_1951to1960" = data_1951to1960,
                    "data_1961to1970" = data_1961to1970, "data_1971to1980" = data_1971to1980,
                    "data_1981to1990" = data_1981to1990, "data_1991to2000" = data_1991to2000,
                    "data_2001to2010" = data_2001to2010, "data_2011to2020" = data_2011to2020)
write.xlsx(CleanedData, file="CleanedData.xlsx", rowNames=FALSE)


















