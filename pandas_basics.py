import pandas as pd

s1=pd.Series([1,2,3,4,5])
print(s1)

print("\nchanging index::::")
s2=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s2)

print("\nseries object from dictionary::::")
l1=pd.Series({'a':1 ,'b':2,'c':3,'d':4,'e':5})#instead of changing index outside, we can use a dictionary . the key's will store index.
print(l1)

print("\nchanging the index position::::")
l2=pd.Series({'a':1,'b':2,'c':3,'d':4},index=['e','d','a','b','c'])#here e index is not declared so it automatically print " NaN "
print(l2)

print("\nextracting elements::::")
l3=pd.Series([1,2,3,4,5])

print("\nextracting single elements::::")
print(l3[3])#will  print the element at index 3

print("\nextracting elements in series::::")
print(l3[:3])#normal slicing, same as list
print(l3[-2:])

print("\nBasic math operations::::")
i=l3+2#it adds 2 in every element
print(i)

print("\nadding two series::::")
a=pd.Series([1,2,3,4,5])
b=pd.Series([6,7,8,9,10])
c=a+b#it adds values of both series, of same index.
print(c)

print("\nsubtracting with number::::")
h=a-4
print(h)

print("\nsubtracting two series::::")
f=a-b
print(f)

print("\nmultiplying two series::::")
g=a*b
print(g)

print("\nmultiplying with numbers::::")
j=a*2
print(j)

print("\ndata frame::::")
_data_frame=pd.DataFrame({"Name":['taran','jashan','pallu'],"Roll_no.":['20','21','22']})
#data frame is used to make multiple columns,in "" we will write column's key name and in '' we write the data
print(_data_frame)

print("\nquick information of dataframe::::")
print(_data_frame.info())#give information which contains datatype , non-null values , rows and columns etc.

print("\nfind missing values::::")
print(_data_frame.isnull().sum())#it finds how many missing values are there in columns.

print("\ngroupby::::")
print(_data_frame.groupby('Name').mean(numeric_only=True))# it follows the three steps process , 1. it groups the data in some criteria ,2.apply a function on it , 3. combine it and give result.

print("\noperations on csv file::::")
csv_file=pd.read_csv(r"C:\Users\ji873\Downloads\phpB0xrNj.csv~\phpB0xrNj.csv")

print("\nto get first five records in data::::")
print(csv_file.head())#this will print first five records in datasets

print("\nlast five records::::")
print(csv_file.tail())#this print the last five records of dataset

print("\nto get the shape of dataset::::")
print(csv_file.shape)#it will tell how many rows and columns are present in dataset,in format of (rows,column)

print("\ndescribe function::::")
print(csv_file.describe())#describe function is used to get statistical summary

print("\nto extract some specific data from dataset::::")
print(csv_file.iloc[0:3,0:1])# iloc function is used to extract data using index method ,format is [rows,column].

print("\nto extract data with column name::::")
print(csv_file.loc[0:3,('f1','f2')])#it is same as iloc function ,but we have freedom to get column by its name. rows will be defined same as iloc.
# for loc function , the last index in given will also be included. 0:3, so there 3rd index will also be included . it is only for loc function

print("\ndropping columns::::")
print(csv_file.drop('f1',axis=1))#drop is used to exclude any particular column or row. here axis=1 means column, axis=0 means rows

print("\ndropping rows::::")
print(csv_file.drop([1,2,3],axis=0))# here in [] we will pass rows that we want to exclude.

print("\npandas statistical functions::::")

print("\nmean::::")
print(csv_file.mean(numeric_only=True))# here we use numeric_only=True because in dataset we have string values and if we don't use this so it will cause an error.

print("\nmedian::::")
print(csv_file.median(numeric_only=True))#same as in mean.

print("\nmin::::")
print(csv_file.min())#min and max also are used for maths, but it can also be used on strings.

print("\nmax::::")
print(csv_file.max())

print("\nto apply a function on dataset::::")

def half(s):
    return s/2
print(csv_file[['f1','f2']].apply(half))#it will apply any function on specific columns.

print("\n to sort data according to any column::::")
print(csv_file.sort_values(by='f1'))#it will sort the data according to ascending order of f1.

print("\n to get how many times a value re-appear::::")
print(csv_file['f1'].value_counts())# here we get how many times a f1 columns value re-appears.
 
