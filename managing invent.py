# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 16:36:27 2018
@author: user
"""

import pandas as pd
import numpy as np
from karthikcode import sorted_profit

# loading dataset
dataset = pd.read_excel("C:/Users/Sweet Home/.spyder-py3/store-dataset.xlsx")

# sorting from lowest to highest date
dataset1 = dataset.sort_values('Order Date')

# resetting index
dataset1 = dataset1.reset_index(drop=True)


# selecting desired sales data for a given period of time
x=int(input("Enter year"))
y=int(input("Enter month "))
a = pd.DatetimeIndex(dataset1['Order Date']).year ==  x
b = pd.DatetimeIndex(dataset1['Order Date']).month ==  y

dataset2 = pd.DataFrame()
for i in range(len(dataset1)):
    if(a[i]== True and b[i]==True):
    
        dataset2 = dataset2.append(dataset1.iloc[i,:])    
        
dataset2 = dataset2.reset_index(drop=True)

# setting inventory size    
l = list(dataset2['Product Name'].unique())
inv_dict = {}
for i in l:
    inv_dict[i] = 500

# sold, remaining % sold, adding inventory
sold_percent = {}   
data,data1= sorted_profit(x,y)

for i in range(len(dataset2)):
    # percentage of sales for each product
    sold_percent[dataset2['Product Name'][i]] = (((((inv_dict[dataset2['Product Name'][i]])-(inv_dict[dataset2['Product Name'][i]]-int(dataset2['Quantity'][i])))/inv_dict[dataset2['Product Name'][i]])*100),dataset2['Quantity'][i])
    # updating inventory
    temp = inv_dict[dataset2['Product Name'][i]]
    inv_dict[dataset2['Product Name'][i]] -= int(dataset2['Quantity'][i])
    # updating inventory for next month/quarter/year
    if(sold_percent[dataset2['Product Name'][i]][1] >= 10.0):
        
        
        
            
        #dfb = data[data['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]  
                
        
        #for j in dataset2['Product Name']:

        try:
            
            count=0     
            dfb = data[data1['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]   
        except:
            
            count =1
            pass 

        if(count==1):
            dfb = data[data['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]
            
           
                
                
            if(dfb < 0.2*(len(data))):
                
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.8*temp
            
            if(dfb >= 0.2*(len(data))):
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.5*temp
        else:
            if(dfb < 0.2*(len(data1))):
                
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.8*temp
            
            if(dfb >= 0.2*(len(data1))):
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.5*temp
        
        
    if(sold_percent[dataset2['Product Name'][i]][1] <= 10.0 and sold_percent[dataset2['Product Name'][i]][1] >= 5.0  ):
        
         
        #for j in dataset2['Product Name']:
        #dfb = data[data['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]   
        
        try:
            
            count=0     
            dfb = data[data1['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]   
        except:
            
            count =1
            pass 
        if(count==1):
            dfb = data[data['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]

        
            if(dfb < 0.2*(len(data))):
                
                
                   
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.8*temp
            
            if(dfb > 0.2*(len(data)and dfb < 0.8*(len(data)))):
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.5*temp    
            
            if(dfb >= 0.8*(len(data))):
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.2*temp

        else:
            if(dfb < 0.2*(len(data1))):
                
                
                   
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.8*temp
            
            if(dfb > 0.2*(len(data1)and dfb < 0.8*(len(data1)))):
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.5*temp    
            
            if(dfb >= 0.8*(len(data1))):
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.2*temp
            
            
    if(sold_percent[dataset2['Product Name'][i]][1] <= 5.0  ):
        
        #for j in dataset2['Product Name']:
        #dfb = data[data['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]   
        try:
            count=0     
            dfb = data[data1['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]   
        except:
            count =1
            pass 
        
        if(count==1):
            dfb = data[data['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]


        
            if(dfb < 0.2*(len(data))):
                   
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.5*temp
            
            if(dfb > 0.2*(len(data)and dfb < 0.8*(len(data)))):
                   
                   
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.5*temp    
            
            if(dfb >= 0.8*(len(data))):
                   
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.0*temp

        else:
              if(dfb < 0.2*(len(data1))):
                   
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.5*temp
            
              if(dfb > 0.2*(len(data1)and dfb < 0.8*(len(data1)))):
                   
                   
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.5*temp    
            
              if(dfb >= 0.8*(len(data1))):
                   
                
                print(dataset2['Product Name'][i])
                inv_dict[dataset2['Product Name'][i]] += 0.0*temp