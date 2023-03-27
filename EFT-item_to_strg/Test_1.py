################################################################################################################################
#Test_1


import pandas as pd
import numpy as np
import webbrowser
import os
 
 
os.startfile(r"G:\Python\pandas\pandasdocu.pdf")
webbrowser.open_new_tab(r"https://pypi.org/project/pyoo/")
webbrowser.open_new_tab(r"https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html")
 
 
 
# create a DataFrame with "pd.DataFrame("dictionary")" index by default is 0  till n
# to make your own index use pd.DataFrame("dictionary", index = [])
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
 
# create a Series with "pd.Series("list")"
# to make a Series with an index and an name use "pd.Series([30, 35, 40], index=[], name="name")"
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
 
# read csv File
# pd.read_csv("path")
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")
 
# converts pd.Series to a python list
ds1 = pd.Series([2, 4, 6, 8, 10])
a = ds1.tolist() 
 
# DataFrame.sum(axis = 0, skipna = None)
# axis = 0 is index , axis = 1 is columns
# skipna = True skips Na values
descriptor_counts = n_trop = wine_reviews.description.map(lambda desc: "tropical" in desc).sum() # adds all counts of the word "tropical" in description
 
 
# use the shape attribute to check how large your data is
# give number of rows and columns
wine_reviews.shape
 
# get info about dataset
wine_reviews.info()
 
# take a given column as index from csv File
#index_col
 
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
 
#save a File as csv
# to.csv("name.csv")
wine_reviews.to_csv("wine_revs.csv")
 
 
# acces a property of a csv file as an attribute
reviews = pd.read_csv(r"F:\Python\pandas\winemag-data-130k-v2.csv")
reviews.country
 
# acces values with indexing like a python list
# more clear than the methode above
reviews['country']
 
# if an value has a subvalue use double indexing
reviews['country'][0] 
 
# Index-based selection
# iloc has the rule:row-first, column-second
# instead of ":" you can also use a list
# negative numbers count from the end 
reviews.iloc[:, 1] # show all rows from sec column
 
# Label-based selection
# loc uses the data index value
reviews.loc[0, 'country']
 
# set_index()
# takes an attribute and uses it as index
reviews.set_index("title")
 
# Conditional selection
 
# outputs True or False
reviews.country == 'Italy'
# show all true results from the data
 
reviews.loc[reviews.country == 'Italy']
# with "&" you can add another condition
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
# with "|" you can make an or condition
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
 
# isin
# lets you select data whose value "is in" a list of values
# shows all rows where Italy or France occurs in country
reviews.loc[reviews.country.isin(['Italy', 'France'])]
 
# isnull
# let you highlight values which are (or are not) empty (NaN)
reviews.loc[reviews.price.notnull()]
 
# Assigning data
 
# assign a constant value
reviews['critic'] = 'everyone'
# assign an iterable of values
reviews['index_backwards'] = range(len(reviews), 0, -1)
 
#summary functions
 
 
# describe() 
# gives a summary of all attributes from the selected column
reviews.points.describe()
 
# mean()
# give information about the mean value in the selected column
# muste be numbers
reviews.points.mean()
 
# meadian()
# give information about the median value in the selected column
reviews.points.median()
 
# unique()
# shows all unique values or names in the selected column
reviews.taster_name.unique()
 
# value_counts()
# shows all unique values or names in the selected column and how often they occur
reviews.taster_name.value_counts()
 
# idxmax(axis = 0, skipna = True)
# 0 or ‘index’ for row-wise, 1 or ‘columns’ for column-wise
# skipna bool, default True: skips Na/null values
# Return maximum value in selected row or column
centered_price = reviews.points.idxmax()
 
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title'] + "-" + str(bargain_idx)
# this example shows the wine with the best price - points ration and combines the results in one string
 
#maps
# works like a mathematical function
 
# map()
# simpler fomr of maps()
# basic operation of p - review_points_mean
# returns a new Series where all the values have been transformed by your function
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)
 
# apply()
# equal to map() if we want to transform a whole DataFrame by calling a "custom method" on each row
def remean_points(row):
    row.points = row.points - review_points_mean
    return row
 
reviews.apply(remean_points, axis='columns') # instead of  axis='columns' we also can use  axis='index'
                                             # then we have to give a function to transform each row
# note that map() and apply() return new Series and DataFrames the origin is not changed
 
 
# working with operators like "+", "-" and        
 
review_points_mean = reviews.points.mean()
reviews.points - review_points_mean
 
#or 
reviews.country + " - " + reviews.region_1 # this code combines the country and region informations
# output exapml. Italy - Etna
 
 
 
 

import pandas as pd
import numpy as np
import webbrowser
import os


os.startfile(r"G:\Python\pandas\pandasdocu.pdf")
webbrowser.open_new_tab(r"https://pypi.org/project/pyoo/")
webbrowser.open_new_tab(r"https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html")



# create a DataFrame with "pd.DataFrame("dictionary")" index by default is 0  till n
# to make your own index use pd.DataFrame("dictionary", index = [])
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

# create a Series with "pd.Series("list")"
# to make a Series with an index and an name use "pd.Series([30, 35, 40], index=[], name="name")"
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

# read csv File
# pd.read_csv("path")
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")

# converts pd.Series to a python list
ds1 = pd.Series([2, 4, 6, 8, 10])
a = ds1.tolist() 

# DataFrame.sum(axis = 0, skipna = None)
# axis = 0 is index , axis = 1 is columns
# skipna = True skips Na values
descriptor_counts = n_trop = wine_reviews.description.map(lambda desc: "tropical" in desc).sum() # adds all counts of the word "tropical" in description


# use the shape attribute to check how large your data is
# give number of rows and columns
wine_reviews.shape

# get info about dataset
wine_reviews.info()

# take a given column as index from csv File
#index_col

wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#save a File as csv
# to.csv("name.csv")
wine_reviews.to_csv("wine_revs.csv")


# acces a property of a csv file as an attribute
reviews = pd.read_csv(r"F:\Python\pandas\winemag-data-130k-v2.csv")
reviews.country

# acces values with indexing like a python list
# more clear than the methode above
reviews['country']

# if an value has a subvalue use double indexing
reviews['country'][0] 

# Index-based selection
# iloc has the rule:row-first, column-second
# instead of ":" you can also use a list
# negative numbers count from the end 
reviews.iloc[:, 1] # show all rows from sec column

# Label-based selection
# loc uses the data index value
reviews.loc[0, 'country']

# set_index()
# takes an attribute and uses it as index
reviews.set_index("title")

# Conditional selection

# outputs True or False
reviews.country == 'Italy'
# show all true results from the data

reviews.loc[reviews.country == 'Italy']
# with "&" you can add another condition
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
# with "|" you can make an or condition
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

# isin
# lets you select data whose value "is in" a list of values
# shows all rows where Italy or France occurs in country
reviews.loc[reviews.country.isin(['Italy', 'France'])]

# isnull
# let you highlight values which are (or are not) empty (NaN)
reviews.loc[reviews.price.notnull()]

# Assigning data

# assign a constant value
reviews['critic'] = 'everyone'
# assign an iterable of values
reviews['index_backwards'] = range(len(reviews), 0, -1)

#summary functions


# describe() 
# gives a summary of all attributes from the selected column
reviews.points.describe()

# mean()
# give information about the mean value in the selected column
# muste be numbers
reviews.points.mean()

# meadian()
# give information about the median value in the selected column
reviews.points.median()

# unique()
# shows all unique values or names in the selected column
reviews.taster_name.unique()

# value_counts()
# shows all unique values or names in the selected column and how often they occur
reviews.taster_name.value_counts()

# idxmax(axis = 0, skipna = True)
# 0 or ‘index’ for row-wise, 1 or ‘columns’ for column-wise
# skipna bool, default True: skips Na/null values
# Return maximum value in selected row or column
centered_price = reviews.points.idxmax()

bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title'] + "-" + str(bargain_idx)
# this example shows the wine with the best price - points ration and combines the results in one string

#maps
# works like a mathematical function

# map()
# simpler fomr of maps()
# basic operation of p - review_points_mean
# returns a new Series where all the values have been transformed by your function
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

# apply()
# equal to map() if we want to transform a whole DataFrame by calling a "custom method" on each row
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns') # instead of  axis='columns' we also can use  axis='index'
                                             # then we have to give a function to transform each row
# note that map() and apply() return new Series and DataFrames the origin is not changed


# working with operators like "+", "-" and        

review_points_mean = reviews.points.mean()
reviews.points - review_points_mean

#or 
reviews.country + " - " + reviews.region_1 # this code combines the country and region informations
# output exapml. Italy - Etna
                                        
                            

