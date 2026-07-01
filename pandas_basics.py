import pandas as pd

s1=pd.Series([1,2,3,4,5])
print(s1)

print("changing index::::")
s2=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s2)

print("series object from dictionary::::")
l1=pd.Series({'a':1 ,'b':2,'c':3,'d':4,'e':5})#instead of changing index outside, we can use a dictionary . the key's will store index.
print(l1)

print("changing the index position::::")
l2=pd.Series({'a':1,'b':2,'c':3,'d':4},index=['e','d','a','b','c'])#here e index is not declared so it automatically print " NaN "
print(l2)

print("extracting elements::::")
l3=pd.Series([1,2,3,4,5])

print("extracting single elements::::")
print(l3[3])#will  print the element at index 3

print("extracting elements in series::::")
print(l3[:3])#normal slicing, same as list
print(l3[-2:])

print("Basic math operations::::")
i=l3+2#it adds 2 in every element
print(i)

print("adding two series::::")
a=pd.Series([1,2,3,4,5])
b=pd.Series([6,7,8,9,10])
c=a+b#it adds values of both series, of same index.
print(c)

print("subtracting with number::::")
h=a-4
print(h)

print("subtracting two series::::")
f=a-b
print(f)

print("multiplying two series::::")
g=a*b
print(g)

print("multiplying with numbers::::")
j=a*2
print(j)