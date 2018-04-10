# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:34:05 2018

@author: user
"""

marks ={}
for i in range(0,4):
    name=input()
    sub1,sub2,sub3,sub4=map(int,input().split())
    marks[name]=[sub1,sub2,sub3,sub4]
print(marks)    
print(sub1)
s =[]
j =0

for i in marks:
    print(i, marks[i])
    s.append([i,sum(marks[i])])
    print(max(marks[i]))
    
print(max(s))