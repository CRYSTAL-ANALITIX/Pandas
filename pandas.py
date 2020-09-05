# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:33:03 2020

@author: hp
"""


'''Easy handling of missing data (represented as NaN) in floating point as 
well as non-floating point data

Size mutability: columns can be inserted and deleted from DataFrame and 
higher dimensional objects

Automatic and explicit data alignment: objects can be explicitly aligned to 
a set of labels, or the user can simply ignore the labels and let Series,
 DataFrame, etc. automatically align the data for you in computations

Powerful, flexible group by functionality to perform split-apply-combine 
operations on data sets, for both aggregating and transforming data

Make it easy to convert ragged, differently-indexed data in other Python and 
NumPy data structures into DataFrame objects

Intelligent label-based slicing, fancy indexing, and subsetting of 
large data sets

Intuitive merging and joining data sets

Flexible reshaping and pivoting of data sets

Hierarchical labeling of axes (possible to have multiple labels per tick)

Robust IO tools for loading data from flat files (CSV and delimited), 
Excel files, databases, and saving / loading data from the ultrafast 
HDF5 format

Time series-specific functionality: date range generation and frequency 
conversion, moving window statistics, date shifting and lagging.'''

#Pandas library has many tools which can help in analysing data

#it is divided into two parts 
#SERIES
#DATAFRAMES

#1.Series
'''Series is a one dimensional data structure'''

import pandas as pd
age = pd.Series([1,2,3,4])
print("the maximum age in the series is ",age.max())
print("the minimum age in the series is ",age.min())
print("the sum of ages in the series is ",age.sum())
print("the mean of ages in the series is ",age.mean())
print("the median of ages in the series is ",age.median())
print("number of ages in the series is ",age.count())

#we should not pass a dictionary to a series data structure

#2.Dataframes
'''Dataframe is a two dimensional data structure'''

import pandas as pd
data = {'Name':['Yatin','Sumpi','Rishu','Papa'],
        'Age':[30,31,32,57],
        'Occupation':['Student','CSE','CS','Senior Manager'],
        'Height':[5.7,5.10,5.8,5.7]}

Df = pd.DataFrame(data, columns=['Name','Age','Occupation','Height'])
print("Maximum age with in the data is ",Df['Age'].max())
#aggregate functions can be applied to any column
#aggregate functions can't be applied to more than one column
Df['Age','Name'].max()#this is key error

data2 = {'Name':['Mommy','Nikita'],
         'Age':[56,24],
         'Occupation':['Housewife', 'Student'],
         'Height':[5.4,5.6]}
Df2 = pd.DataFrame(data2, columns = ['Name','Age','Occupation','Height'])

#Concatenating two dataframes

result = pd.concat([Df,Df2])#we have to pass a list of dataframes here

#importing data
import pandas as pd
Movies = pd.read_excel("C:\\Users\\hp\\Desktop\\movies_metadata.xlsx")

#taking a specified column from the data namely belongs_to_collection
BtC = Movies['belongs_to_collection']
BtC = pd.DataFrame(BtC)
#Skimming the data as per requirement
BtCskimmed = BtC['belongs_to_collection'].astype(str).str.rsplit(",", expand = True)
#dropping null values
BtCskimmed.dropna(inplace = True)
#further skimming the data one by one
BtCskimmed1 = BtCskimmed[0].astype(str).str.rsplit(':',expand = True)
BtCskimmed1.info()
#taking column 0
BtCskimmed1[0].astype(str).str.replace('{','')
BtCskimmed1.rename(columns = {1:'id'}, inplace=True)
BtCskimmed1.drop([0], axis=1, inplace=True)
#taking column 1
BtCskimmed2 = BtCskimmed[1].astype(str).str.rsplit(':',expand = True)
BtCskimmed2.rename(columns = {1:'name'}, inplace=True)
BtCskimmed2.drop([0], axis=1, inplace=True)
#taking column 2
BtCskimmed3 = BtCskimmed[2].astype(str).str.rsplit(':',expand = True)
BtCskimmed3.rename(columns = {1:'posterpath'}, inplace=True)
BtCskimmed3.drop([0], axis=1, inplace=True)
#taking column 3
BtCskimmed4 = BtCskimmed[3].astype(str).str.rsplit(':',expand = True)
BtCskimmed4.rename(columns = {'posterpath':'backdroppath'}, inplace=True)
BtCskimmed4.drop([0], axis=1, inplace=True)
#finally combining skimmed data into final table with new columns
final = pd.concat([BtCskimmed1,BtCskimmed2,BtCskimmed3,BtCskimmed4], axis = 1)


#taking another column into consideration namely genres
import pandas as pd
Movies = pd.read_excel("C:\\Users\\hp\\Desktop\\movies_metadata.xlsx")
Genres = Movies['genres']
Genres = pd.DataFrame(Genres)
Genrestrim = Genres['genres'].astype(str).str.strip('[{}]').str.rsplit(',', expand = True)

#trimming column 1
Genrestrim1 = Genrestrim[0].astype(str).str.rsplit(':',expand = True)
Genrestrim1.rename(columns = {1:'id'}, inplace=True)
Genrestrim1.drop([0], axis=1, inplace=True)
#trimming column 2
Genrestrim2 = Genrestrim[1].astype(str).str.rsplit(':',expand = True)
Genrestrim2.rename(columns = {1:'name'}, inplace=True)
Genrestrim2.drop([0], axis=1, inplace=True)
#trimming column 3
Genrestrim3 = Genrestrim[2].astype(str).str.rsplit(':',expand = True)
Genrestrim3.rename(columns = {1:'id'}, inplace=True)
Genrestrim3.drop([0], axis=1, inplace=True)
#trimming column 4
Genrestrim4 = Genrestrim[3].astype(str).str.rsplit(':',expand = True)
Genrestrim4.rename(columns = {1:'id'}, inplace=True)
Genrestrim4.drop([0], axis=1, inplace=True)
#trimming column 5
Genrestrim5 = Genrestrim[4].astype(str).str.rsplit(':',expand = True)
Genrestrim5.rename(columns = {1:'id'}, inplace=True)
Genrestrim5.drop([0], axis=1, inplace=True)
#trimming column 6
Genrestrim6 = Genrestrim[5].astype(str).str.rsplit(':',expand = True)
Genrestrim6.rename(columns = {1:'id'}, inplace=True)
Genrestrim6.drop([0], axis=1, inplace=True)
#trimming column 7
Genrestrim7 = Genrestrim[6].astype(str).str.rsplit(':',expand = True)
Genrestrim7.rename(columns = {1:'id'}, inplace=True)
Genrestrim7.drop([0], axis=1, inplace=True)
#trimming column 8
Genrestrim8 = Genrestrim[7].astype(str).str.rsplit(':',expand = True)
Genrestrim8.rename(columns = {1:'id'}, inplace=True)
Genrestrim8.drop([0], axis=1, inplace=True)
#adjusting few columns
Genrestrim2['name']=Genrestrim2['name'].astype(str).str.strip("}")
Genrestrim4['id']=Genrestrim4['id'].astype(str).str.strip("}")
#finally concatenating to see them as a single table
final2 = pd.concat([Genrestrim1,Genrestrim2,Genrestrim3,Genrestrim4,
                    Genrestrim5,Genrestrim6,Genrestrim7,Genrestrim8], axis=1)

#taking another column into consideration namely production_companies
import pandas as pd
Movies = pd.read_excel("C:\\Users\\hp\\Desktop\\movies_metadata.xlsx")

p_c = Movies['production_companies']
p_c = pd.DataFrame(p_c)
p_ctrim = p_c['production_companies'].astype(str).str.strip('[{}]').str.rsplit(',', expand = True)
#taking column 0
p_ctrim1 = p_ctrim[0].astype(str).str.rsplit(':',expand = True)
p_ctrim1.rename(columns = {1:'name'}, inplace=True)
p_ctrim1.drop([0], axis=1, inplace=True)

#taking column 1
p_ctrim2 = p_ctrim[1].astype(str).str.rsplit(':',expand = True)
p_ctrim2.rename(columns = {1:'id'}, inplace=True)
p_ctrim2.drop([0], axis=1, inplace=True)

#taking column 2
p_ctrim3 = p_ctrim[2].astype(str).str.rsplit(':',expand = True)
p_ctrim3.rename(columns = {1:'name'}, inplace=True)
p_ctrim3.drop([0], axis=1, inplace=True)

#taking column 3
p_ctrim4 = p_ctrim[3].astype(str).str.rsplit(':',expand = True)
p_ctrim4.rename(columns = {1:'id'}, inplace=True)
p_ctrim4.drop([0], axis=1, inplace=True)

#taking column 4
p_ctrim5 = p_ctrim[4].astype(str).str.rsplit(':',expand = True)
p_ctrim5.rename(columns = {1:'name'}, inplace=True)
p_ctrim5.drop([0], axis=1, inplace=True)

#taking column 5
p_ctrim6 = p_ctrim[5].astype(str).str.rsplit(':',expand = True)
p_ctrim6.rename(columns = {1:'id'}, inplace=True)
p_ctrim6.drop([0], axis=1, inplace=True)

#taking column 6
p_ctrim7 = p_ctrim[6].astype(str).str.rsplit(':',expand = True)
p_ctrim7.rename(columns = {1:'name'}, inplace=True)
p_ctrim7.drop([0], axis=1, inplace=True)
#taking column 7
p_ctrim8 = p_ctrim[7].astype(str).str.rsplit(':',expand = True)
p_ctrim8.rename(columns = {1:'id'}, inplace=True)
p_ctrim8.drop([0], axis=1, inplace=True)

#taking column 8
p_ctrim9 = p_ctrim[8].astype(str).str.rsplit(':',expand = True)
p_ctrim9.rename(columns = {1:'name'}, inplace=True)
p_ctrim9.drop([0], axis=1, inplace=True)

#taking column 9
p_ctrim10 = p_ctrim[9].astype(str).str.rsplit(':',expand = True)
p_ctrim10.rename(columns = {1:'id'}, inplace=True)
p_ctrim10.drop([0], axis=1, inplace=True)

#taking column 10
p_ctrim11 = p_ctrim[10].astype(str).str.rsplit(':',expand = True)
p_ctrim11.rename(columns = {1:'name'}, inplace=True)
p_ctrim11.drop([0], axis=1, inplace=True)

#taking column 11
p_ctrim12 = p_ctrim[11].astype(str).str.rsplit(':',expand = True)
p_ctrim12.rename(columns = {1:'id'}, inplace=True)
p_ctrim12.drop([0], axis=1, inplace=True)

#taking column 12
p_ctrim13 = p_ctrim[12].astype(str).str.rsplit(':',expand = True)
p_ctrim13.rename(columns = {1:'name'}, inplace=True)
p_ctrim13.drop([0], axis=1, inplace=True)

#taking column 13
p_ctrim14 = p_ctrim[13].astype(str).str.rsplit(':',expand = True)
p_ctrim14.rename(columns = {1:'id'}, inplace=True)
p_ctrim14.drop([0], axis=1, inplace=True)
#taking row 28
p_ctrim28 = p_ctrim.iloc[28:29,:]
p_ctrim28 = p_ctrim28.transpose()
#bifurcating name and id
p_ctrim28n = p_ctrim28.iloc[::2]
p_ctrim28i = p_ctrim28.iloc[1::2]
#taking all names
p_ctrim28th = p_ctrim28n[28].astype(str).str.rsplit(':',expand = True)
p_ctrim28th.rename(columns = {1:'name'}, inplace=True)
p_ctrim28th.drop([0], axis=1, inplace=True)

#taking all ids
p_ctrim28thi = p_ctrim28i[28].astype(str).str.rsplit(':',expand = True)
p_ctrim28thi.rename(columns = {1:'id'}, inplace=True)
p_ctrim28thi.drop([0], axis=1, inplace=True)
#finally combining all
final3 = pd.concat([p_ctrim1,p_ctrim2,p_ctrim3,p_ctrim4,p_ctrim5,
                    p_ctrim6,p_ctrim7,p_ctrim8,p_ctrim9,p_ctrim10,
                    p_ctrim11,p_ctrim12,p_ctrim13,p_ctrim14,p_ctrim28th,
                    p_ctrim28thi], axis = 0)

#takina another column into consideration namely production_countries

import pandas as pd
Movies = pd.read_excel("C:\\Users\\hp\\Desktop\\movies_metadata.xlsx")

p_C = Movies['production_countries']
p_C = pd.DataFrame(p_C)


p_Ctrim = p_C['production_countries'].astype(str).str.strip('[{}]').str.rsplit(',', expand = True)

p_Ctrim.drop(29, inplace = True)
#taking column 0
p_Ctrim1 = p_Ctrim[0].astype(str).str.rsplit(':',expand = True)
p_Ctrim1.rename(columns = {1:'iso_3166_1'}, inplace=True)
p_Ctrim1.drop([0], axis=1, inplace=True)

#taking column 1
p_Ctrim2 = p_Ctrim[1].astype(str).str.rsplit(':',expand = True)
p_Ctrim2.rename(columns = {1:'name'}, inplace=True)
p_Ctrim2.drop([0], axis=1, inplace=True)

#taking column 2
p_Ctrim3 = p_Ctrim[2].astype(str).str.rsplit(':',expand = True)
p_Ctrim3.rename(columns = {1:'iso_3166_1'}, inplace=True)
p_Ctrim3.drop([0], axis=1, inplace=True)

#taking column 3
p_Ctrim4 = p_Ctrim[3].astype(str).str.rsplit(':',expand = True)
p_Ctrim4.rename(columns = {1:'name'}, inplace=True)
p_Ctrim4.drop([0], axis=1, inplace=True)


#taking column 4
p_Ctrim5 = p_Ctrim[4].astype(str).str.rsplit(':',expand = True)
p_Ctrim5.rename(columns = {1:'iso_3166_1'}, inplace=True)
p_Ctrim5.drop([0], axis=1, inplace=True) 

final4 = pd.concat([p_Ctrim1,p_Ctrim2,p_Ctrim3,p_Ctrim4,p_Ctrim5]) 

#taking another column into consideration namely spoken_languages

import pandas as pd
Movies = pd.read_excel("C:\\Users\\hp\\Desktop\\movies_metadata.xlsx")

s_c = Movies['spoken_languages']
s_c = pd.DataFrame(s_c)


s_ctrim = s_c['spoken_languages'].astype(str).str.strip('[{}]').str.rsplit(',', expand = True)

s_ctrim.drop(29, inplace = True)

#taking column 0
s_ctrim1 = s_ctrim[0].astype(str).str.rsplit(':',expand = True)
s_ctrim1.rename(columns = {1:'iso_639_1'}, inplace=True)
s_ctrim1.drop([0], axis=1, inplace=True)

#taking column 1
s_ctrim2 = s_ctrim[1].astype(str).str.rsplit(':',expand = True)
s_ctrim2.rename(columns = {1:'name'}, inplace=True)
s_ctrim2.drop([0], axis=1, inplace=True)

#taking column 2
s_ctrim3 = s_ctrim[2].astype(str).str.rsplit(':',expand = True)
s_ctrim3.rename(columns = {1:'iso_639_1'}, inplace=True)
s_ctrim3.drop([0], axis=1, inplace=True)

#taking column 3
s_ctrim4 = s_ctrim[3].astype(str).str.rsplit(':',expand = True)
s_ctrim4.rename(columns = {1:'name'}, inplace=True)
s_ctrim4.drop([0], axis=1, inplace=True) 
#finally concatenating all tables
finally5 = pd.concat([s_ctrim1,s_ctrim2,s_ctrim3,s_ctrim4])              