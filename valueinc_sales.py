# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:42:26 2022

@author: easyb
"""

import pandas as pd
#file_name = pd.read_csv("file.csv") <--------- Format of read csv
#file_name = pd.read_csv("csv.file", sep=";") <----------Format of read with separation(;)

Data = pd.read_csv("transaction.csv")

Data = pd.read_csv("transaction.csv" ,sep=";")

#summary of the data

Data.info()
#playing around with the variables

var = "Hello World"

Var = 39

var = 2.5
#format List
Var = ["apple", "pear", "banana"]
#format tuple
Var = ("apple", "pear", "banana")
#format set
var = {"apple","pear","banana"}

var = range(10)

var = {"name":"Ismaeel","location":"Nigeria"}
#Bool format
var = True

print (8>9)

print(10 > 9)

#working with calculation
#Defining Variable

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

# Mathematical operation in Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = 21.11 * 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
sellingPerTransaction = NumberOfItemsPurchased * SellingPricePerItem

#CostPerTransaction Column Calculation
#CostPerTransaction = CostPerItem * NumberOfItemsPurchased
#variable = dataframe ('column_name')
CostPerItem = Data['CostPerItem']
NumberOfItemsPurchased = Data["NumberOfItemsPurchased"]
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding a new column to a dataframe

Data['CostPerTransaction'] = CostPerTransaction 

Data['CostPerTransaction'] = Data['CostPerItem'] * Data["NumberOfItemsPurchased"]

#sales per transaction

SalesPerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#adding a new column to dataframe called salespertransaction on two ways

Data['SalesPerTransaction'] = SalesPerTransaction

Data['SalesPerTransaction'] = Data['SellingPricePerItem'] * Data['NumberOfItemsPurchased']

#calculating profit per transaction

Data['ProfitPerTransaction'] = Data['SellingPricePerItem'] - Data['CostPerItem']
Data['ProfitPerTransaction'] = Data['ProfitPerTransaction'] * Data["NumberOfItemsPurchased"]

# markup calculation 

Data['MarkUp'] = (Data['SalesPerTransaction'] - Data['CostPerTransaction'])/Data['CostPerTransaction']

# or markup with formular

Data['MarkUp'] = (Data['ProfitPerTransaction'])/Data['CostPerTransaction']

# rounding up functions

Data['RoundMarkUp'] = round(Data['MarkUp'],2)

# combining datafield

MyDate = 'Day'+'-'+'Month'+'-'+'Year'

#conversion of int64 to str

print(Data['Day'].dtype)
Day = Data['Day'].astype(str)
Year = Data['Year'].astype(str)
print(Day.dtype)
print(Year.dtype)

MyDate = Day+'-'+Data['Month']+'-'+Year

Data['Date'] = MyDate

#using iloc to view specific column

Data.iloc[0]    #View the rows with index = [0]
Data.iloc[0:3]    #view the first 3 rows
Data.iloc[-5:]    #view the last 5 rows
Data.head(5)
Data.iloc[:,2]   #brings all in the 2nd column
Data.iloc[4,2]   # brings out 4 rows 2nd column


# using slit to slit words

split_col = Data['ClientKeywords'].str.split(',' , expand=True)

#creating a new column for client

Data['ClientAge'] = split_col[0]
Data['ClientBusinessClass'] = split_col[1]
Data['ClientYear'] = split_col[2]

#using the replace function

Data['ClientAge'] = Data['ClientAge'].str.replace('[' , '')
Data['ClientYear'] = Data['ClientYear'].str.replace(']' , '')

# using lower function to change item to lowercase
Data['ItemDescription'] = Data['ItemDescription'].str.lower()

# how to merge in a dataset

season = pd.read_csv('value_inc_seasons.csv' , sep=';')

#merging files

Data = pd.merge(Data, season, on='Month')

#dropping column/ remove

Data = Data.drop('ClientKeywords' , axis=1)
Data = Data.drop(['Year','Month','Day'] , axis=1)
# export into csv

Data.to_csv('ValueInc_cleaned.csv', index=False)

