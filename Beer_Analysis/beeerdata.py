# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 09:31:03 2018

@author: user
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from scipy.stats.stats import pearsonr 
import xlrd
import matplotlib.pyplot as plt
Excelfilename = 'yyy.xlsx'
workbook = xlrd.open_workbook(Excelfilename)
worksheet = workbook.sheet_by_name("Data")
num_rows = worksheet.nrows
num_cols = worksheet.ncols

result_data =[]

for curr_row in range(1,53,1):
    row_data = []
    
    for curr_col in range(1,6,2):
        data = worksheet.cell_value(curr_row,curr_col)
        
        row_data.append(data)
    
    result_data.append(row_data)
    
a12pk=[]
a18pk =[]
a30pk =[]
week=[]
for curr_row in range(len(result_data)):
    print(result_data[curr_row])
    a12pk.append(result_data[curr_row][0])
    a18pk.append(result_data[curr_row][1])
    a30pk.append(result_data[curr_row][2])
    week.append(curr_row)
    
print(a12pk)

mean12p = np.mean(a12pk)
mean18p = np.mean(a18pk)
mean30p = np.mean(a30pk)


    

    







result_data1 =[]


for curr_row in range(1,53,1):
    row_data = []
    
    for curr_col in range(8,13,2):
        data = worksheet.cell_value(curr_row,curr_col)
        
        row_data.append(data)
    
    result_data1.append(row_data)
    
a12pkc=[]
a18pkc =[]
a30pkc =[]
week1=[]
for curr_row in range(len(result_data1)):
    #print(result_data[curr_row])
    a12pkc.append(result_data1[curr_row][0]) 
    a18pkc.append(result_data1[curr_row][1])
    a30pkc.append(result_data1[curr_row][2])
    week1.append(curr_row)
    
#print(a12pk)
mean12c = np.mean(a12pkc)
mean18c = np.mean(a18pkc)
mean30c = np.mean(a30pkc)
co12 =0
cc12=0
# =============================================================================
# =============================================================================
# for curr_row in range(len(a12pk)):    
#     
#     co12 = ((a12pk[curr_row]-mean12p)*(a12pkc[curr_row]-mean12c))+co12
#     cc12 =((a12pk[curr_row]-mean12p)**2)+cc12
#     
# co12c = mean12c-((co12/cc12)*mean12p)    
# 
#   
# print(co12/cc12,co12c)   
print(pearsonr(a12pk,a12pkc))
print(pearsonr(a18pk,a18pkc))
print(pearsonr(a30pk,a30pkc))
regr =LinearRegression()
regr.fit(a12pk,a12pkc)
pred = regr.predict(a12pk)
print(pred)
regr.coef_()
np.corrcoef(a12pk,a12pkc)   



#plt.matshow(data.corr())


#12pk
plt.plot(week, a12pk,color = 'red')
plt.plot(week1, a12pkc,color ='orange')
plt.show()
plt.plot(a12pk, a12pkc,'b^')

plt.show()

#18pk

plt.plot(week, a18pk,color='blue')
plt.plot(week1, a18pkc,color='red')
plt.show()
plt.plot(a18pk, a18pkc,'g^')
plt.show()

#30pk

plt.plot(week, a30pk,color='green')

plt.plot(week1, a30pkc,color='red')
plt.show()
plt.plot(a30pk, a30pkc,'b^')
plt.show()


plt.plot(week, a12pk,color='red')
plt.plot(week, a18pk,color='blue')
plt.plot(week, a30pk,color='green')
plt.show()

plt.plot(week1, a12pkc,color='red')
plt.plot(week1, a18pkc,color='blue')
plt.plot(week1, a30pkc,color='green')
print()
plt.show()

    
#print(result_data)    