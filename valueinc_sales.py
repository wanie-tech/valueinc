# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 10:51:03 2022
@author: User
"""

import pandas as pd

data = pd.read_csv('transaction.csv', sep=';')

# summary of the data
data.info()

#ProfitPerItem = SellingPricePerItem-CostPerItem
#ProfitPerTransaction = NumberofItemPurchased * ProfitPerItem
#CostPerTransaction = CostPerItem * NumberofItemPurchased
#SellingPricePerTransaction = SellingPricePerItem * NumberofItemPurchased

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased 

#adding a new column to a dataframe
data['CostPerTransaction'] = CostPerTransaction 

# sales per transaction 
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Calculation = Sales - Cost
data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#markup = sales - cost/ cost
data['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction'] ) / data['CostPerTransaction']

######################################################################################

#rounding marking
roundmarkup = round(data['Markup'], 2)
data['Markup'] = round(data['Markup'], 2)

#checking columns data type
print(data['Day'].dtype)

#to change data to string
day = data['Day'].astype(str)
year = data['Year'].astype(str)

#checking day datatype column - make sure at console is object
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

#add new column
data['date'] = my_date

###############################################################################

#using split to split client keywords field
split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new columns for the split columns in Client Keywords
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract']=split_col[2]

#using replace function
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_now, on = 'key')
data = pd.merge(data, seasons, on = 'Month')

#dropping columns. axis 1 means column, 0 means row
data = data.drop('ClientKeywords', axis=1)
data = data.drop('Day', axis=1)
data = data.drop(['Month', 'Year'], axis=1)

#export into csv
data.to_csv('ValueInc_Cleaned.csv', index = False)
