# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:03:04 2018

@author: user
"""
#String problem
import re
a = ([['Rhia',10,20,30,40,50],
           ['Alan',75,80,75,85,100],
           ['Smith',80,80,80,90,95]])

for i in range(3):
    print(a[i][:2])
    
a[2]= ['Sam',82,79,88,97,99]
print(a[2])
a[0][4] = 95
print(a[0])
a.append([67,56,45])
print(a)

#palindrome
line = "#Python is an interpreted high level programming language for general-purpose programming*."
print(line)

line = re.sub('[^A-Za-z0-9]',' ',line)
print(line)

words = line.split()
print(words)
count = {}
for word in words:
    if word not in count:
        count[word] = 0
        
    count[word] += 1
    
print(count) 

for word in words:
    if word == word[::-1]:
        print("The string is a palindrome",word)
        

#sets problem
A = {5, 3, 8, 6, 1}
B = {1, 5, 3, 4, 2} 
print(min(A))
print(max(A))      
print(min(B))
print(max(B))    
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))


# prime numbers
for i in range(901,1001,2):
    flag=0
    for j in range(2,int((i/2)+1)):
        if i%j == 0:
            flag=1
    if(flag==0):
        print(i)
            
            
            
        
    
        
       
