#importing pandas library to implement DataFrame on Store Dataset
import pandas as pd
import numpy as np
data = pd.read_excel("C:/Users/Sweet Home/.spyder-py3/store-dataset.xlsx")


#Sorting the database chronologically
#dataq,dataq1=sorted_profit(2015,5)

year = 2015
mon = 5

def sorted_profit(year,mon):
    data = pd.read_excel("C:/Users/Sweet Home/.spyder-py3/store-dataset.xlsx")
    data = data.sort_values(by='Order Date')
    #Converting the Date field from string to Date object
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    data['Ship Date'] = pd.to_datetime(data['Ship Date'])
    
    d_product = []
    d_MRP = []
    d_inventory = []
    d_quantity = []
    d_profit = []
    year1 =0
    mon1 = 0
    if(mon == 1 or mon ==  2 or mon == 3):
        mon1= 10
        year1 = year-1
    else:
        mon1=mon-3
        year1=year
     
    data1 = pd.DataFrame()
    count=0
    
    while(count < 3): 
          
        a =  pd.DatetimeIndex(data['Order Date']).year == year1
        b =  pd.DatetimeIndex(data['Order Date']).month == mon1
    
        for i in range(len(data)):
            if(a[i]== True and b[i]==True):
        
                data1 = data1.append(data.iloc[i,:]) 
    
        mon1+=1
        count+=1        
            
        data1 = data1.reset_index(drop=True)
    
        
        
    
    for i in data['Product Name'].unique():
        d_product.append(i)
        d_MRP.append(data[data['Product Name']==i]['MRP per piece'].sum())
        d_inventory.append(data[data['Product Name']==i]['Factory Price per piece'].sum())
        d_quantity.append(data[data['Product Name']==i]['Quantity'].sum())
        d_profit.append(data[data['Product Name']==i]['Profit per piece'].sum())
    d_os = np.array([d_product,d_MRP,d_inventory,d_quantity,d_profit]).T
    d_os = pd.DataFrame(d_os,columns = ['d_product','d_MRP','d_inventory','d_quantity','d_profit'])
    d_os[['d_MRP','d_inventory','d_quantity','d_profit']] = d_os[['d_MRP','d_inventory','d_quantity','d_profit']].apply(pd.to_numeric)
    d_os = d_os.round(2)
    d_os=d_os.sort_values(['d_profit'],ascending=False)
    d_os = d_os.reset_index()
    
        
        
    d_product = []
    d_MRP = []
    d_inventory = []
    d_quantity = []
    d_profit = []   
    for i in data1['Product Name'].unique():
        d_product.append(i)
        d_MRP.append(data1[data1['Product Name']==i]['MRP per piece'].sum())
        d_inventory.append(data1[data1['Product Name']==i]['Factory Price per piece'].sum())
        d_quantity.append(data1[data1['Product Name']==i]['Quantity'].sum())
        d_profit.append(data1[data1['Product Name']==i]['Profit per piece'].sum())
    d_os1 = np.array([d_product,d_MRP,d_inventory,d_quantity,d_profit]).T
    d_os1 = pd.DataFrame(d_os1,columns = ['d_product','d_MRP','d_inventory','d_quantity','d_profit'])
    d_os1[['d_MRP','d_inventory','d_quantity','d_profit']] = d_os1[['d_MRP','d_inventory','d_quantity','d_profit']].apply(pd.to_numeric)
    d_os1 = d_os1.round(2)
    d_os1=d_os1.sort_values(['d_profit'],ascending=False)
    d_os1 = d_os1.reset_index()
    return d_os,d_os1
#Dividing the database with respect to Segment and then further dividing it 
#based on product categories
data_consumer = data[data['Segment']=='Consumer']
data_consumer_officeSupplies = data_consumer[data_consumer['Category']=='Office Supplies']
data_consumer_furniture = data_consumer[data_consumer['Category']=='Furniture']
data_consumer_technology = data_consumer[data_consumer['Category']=='Technology']

data_corporate = data[data['Segment']=='Corporate']
data_corporate_officeSupplies = data_corporate[data_corporate['Category']=='Office Supplies']
data_corporate_furniture = data_corporate[data_corporate['Category']=='Furniture']
data_corporate_technology = data_corporate[data_corporate['Category']=='Technology']

data_homeOffice = data[data['Segment']=='Home Office']
data_homeOffice_officeSupplies = data_homeOffice[data_homeOffice['Category']=='Office Supplies']
data_homeOffice_furniture = data_homeOffice[data_homeOffice['Category']=='Furniture']
data_homeOffice_technology = data_homeOffice[data_homeOffice['Category']=='Technology']

d_cons_os_product = []
d_cons_os_MRP = []
d_cons_os_inventory = []
d_cons_os_quantity = []
d_cons_os_profit = []
for i in data_consumer_officeSupplies['Product Name'].unique():
    d_cons_os_product.append(i)
    d_cons_os_MRP.append(data_consumer_officeSupplies[data_consumer_officeSupplies['Product Name']==i]['MRP per piece'].sum())
    d_cons_os_inventory.append(data_consumer_officeSupplies[data_consumer_officeSupplies['Product Name']==i]['Factory Price per piece'].sum())
    d_cons_os_quantity.append(data_consumer_officeSupplies[data_consumer_officeSupplies['Product Name']==i]['Quantity'].sum())
    d_cons_os_profit.append(data_consumer_officeSupplies[data_consumer_officeSupplies['Product Name']==i]['Profit per piece'].sum())
d_cons_os = np.array([d_cons_os_product,d_cons_os_MRP,d_cons_os_inventory,d_cons_os_quantity,d_cons_os_profit]).T
d_cons_os = pd.DataFrame(d_cons_os,columns = ['d_cons_os_product','d_cons_os_MRP','d_cons_os_inventory','d_cons_os_quantity','d_cons_os_profit'])
d_cons_os[['d_cons_os_MRP','d_cons_os_inventory','d_cons_os_quantity','d_cons_os_profit']] = d_cons_os[['d_cons_os_MRP','d_cons_os_inventory','d_cons_os_quantity','d_cons_os_profit']].apply(pd.to_numeric)
d_cons_os = d_cons_os.round(2)
d_cons_os=d_cons_os.sort_values(['d_cons_os_profit'],ascending=False)

d_cons_fur_product = []
d_cons_fur_MRP = []
d_cons_fur_inventory = []
d_cons_fur_quantity = []
d_cons_fur_profit = []
for i in data_consumer_furniture['Product Name'].unique():
    d_cons_fur_product.append(i)
    d_cons_fur_MRP.append(data_consumer_furniture[data_consumer_furniture['Product Name']==i]['MRP per piece'].sum())
    d_cons_fur_inventory.append(data_consumer_furniture[data_consumer_furniture['Product Name']==i]['Factory Price per piece'].sum())
    d_cons_fur_quantity.append(data_consumer_furniture[data_consumer_furniture['Product Name']==i]['Quantity'].sum())
    d_cons_fur_profit.append(data_consumer_furniture[data_consumer_furniture['Product Name']==i]['Profit per piece'].sum())
d_cons_fur = np.array([d_cons_fur_product,d_cons_fur_MRP,d_cons_fur_inventory,d_cons_fur_quantity,d_cons_fur_profit]).T
d_cons_fur = pd.DataFrame(d_cons_fur,columns = ['d_cons_fur_product','d_cons_fur_MRP','d_cons_fur_inventory','d_cons_fur_quantity','d_cons_fur_profit'])
d_cons_fur[['d_cons_fur_MRP','d_cons_fur_inventory','d_cons_fur_quantity','d_cons_fur_profit']] = d_cons_fur[['d_cons_fur_MRP','d_cons_fur_inventory','d_cons_fur_quantity','d_cons_fur_profit']].apply(pd.to_numeric)
d_cons_fur = d_cons_fur.round(2)
d_cons_fur=d_cons_fur.sort_values(['d_cons_fur_profit'],ascending=False)

d_cons_tech_product = []
d_cons_tech_MRP = []
d_cons_tech_inventory = []
d_cons_tech_quantity = []
d_cons_tech_profit = []
for i in data_consumer_technology['Product Name'].unique():
    d_cons_tech_product.append(i)
    d_cons_tech_MRP.append(data_consumer_technology[data_consumer_technology['Product Name']==i]['MRP per piece'].sum())
    d_cons_tech_inventory.append(data_consumer_technology[data_consumer_technology['Product Name']==i]['Factory Price per piece'].sum())
    d_cons_tech_quantity.append(data_consumer_technology[data_consumer_technology['Product Name']==i]['Quantity'].sum())
    d_cons_tech_profit.append(data_consumer_technology[data_consumer_technology['Product Name']==i]['Profit per piece'].sum())
d_cons_tech = np.array([d_cons_tech_product,d_cons_tech_MRP,d_cons_tech_inventory,d_cons_tech_quantity,d_cons_tech_profit]).T
d_cons_tech = pd.DataFrame(d_cons_tech,columns = ['d_cons_tech_product','d_cons_tech_MRP','d_cons_tech_inventory','d_cons_tech_quantity','d_cons_tech_profit'])
d_cons_tech[['d_cons_tech_MRP','d_cons_tech_inventory','d_cons_tech_quantity','d_cons_tech_profit']] = d_cons_tech[['d_cons_tech_MRP','d_cons_tech_inventory','d_cons_tech_quantity','d_cons_tech_profit']].apply(pd.to_numeric)
d_cons_tech = d_cons_tech.round(2)
d_cons_tech=d_cons_tech.sort_values(['d_cons_tech_profit'],ascending=False)

d_cor_os_product = []
d_cor_os_MRP = []
d_cor_os_inventory = []
d_cor_os_quantity = []
d_cor_os_profit = []
for i in data_corporate_officeSupplies['Product Name'].unique():
    d_cor_os_product.append(i)
    d_cor_os_MRP.append(data_corporate_officeSupplies[data_corporate_officeSupplies['Product Name']==i]['MRP per piece'].sum())
    d_cor_os_inventory.append(data_corporate_officeSupplies[data_corporate_officeSupplies['Product Name']==i]['Factory Price per piece'].sum())
    d_cor_os_quantity.append(data_corporate_officeSupplies[data_corporate_officeSupplies['Product Name']==i]['Quantity'].sum())
    d_cor_os_profit.append(data_corporate_officeSupplies[data_corporate_officeSupplies['Product Name']==i]['Profit per piece'].sum())
d_cor_os = np.array([d_cor_os_product,d_cor_os_MRP,d_cor_os_inventory,d_cor_os_quantity,d_cor_os_profit]).T
d_cor_os = pd.DataFrame(d_cor_os,columns = ['d_cor_os_product','d_cor_os_MRP','d_cor_os_inventory','d_cor_os_quantity','d_cor_os_profit'])
d_cor_os[['d_cor_os_MRP','d_cor_os_inventory','d_cor_os_quantity','d_cor_os_profit']] = d_cor_os[['d_cor_os_MRP','d_cor_os_inventory','d_cor_os_quantity','d_cor_os_profit']].apply(pd.to_numeric)
d_cor_os = d_cor_os.round(2)
d_cor_os=d_cor_os.sort_values(['d_cor_os_profit'],ascending=False)

d_cor_fur_product = []
d_cor_fur_MRP = []
d_cor_fur_inventory = []
d_cor_fur_quantity = []
d_cor_fur_profit = []
for i in data_corporate_furniture['Product Name'].unique():
    d_cor_fur_product.append(i)
    d_cor_fur_MRP.append(data_corporate_furniture[data_corporate_furniture['Product Name']==i]['MRP per piece'].sum())
    d_cor_fur_inventory.append(data_corporate_furniture[data_corporate_furniture['Product Name']==i]['Factory Price per piece'].sum())
    d_cor_fur_quantity.append(data_corporate_furniture[data_corporate_furniture['Product Name']==i]['Quantity'].sum())
    d_cor_fur_profit.append(data_corporate_furniture[data_corporate_furniture['Product Name']==i]['Profit per piece'].sum())
d_cor_fur = np.array([d_cor_fur_product,d_cor_fur_MRP,d_cor_fur_inventory,d_cor_fur_quantity,d_cor_fur_profit]).T
d_cor_fur = pd.DataFrame(d_cor_fur,columns = ['d_cor_fur_product','d_cor_fur_MRP','d_cor_fur_inventory','d_cor_fur_quantity','d_cor_fur_profit'])
d_cor_fur[['d_cor_fur_MRP','d_cor_fur_inventory','d_cor_fur_quantity','d_cor_fur_profit']] = d_cor_fur[['d_cor_fur_MRP','d_cor_fur_inventory','d_cor_fur_quantity','d_cor_fur_profit']].apply(pd.to_numeric)
d_cor_fur = d_cor_fur.round(2)
d_cor_fur=d_cor_fur.sort_values(['d_cor_fur_profit'],ascending=False)

d_cor_tech_product = []
d_cor_tech_MRP = []
d_cor_tech_inventory = []
d_cor_tech_quantity = []
d_cor_tech_profit = []
for i in data_corporate_technology['Product Name'].unique():
    d_cor_tech_product.append(i)
    d_cor_tech_MRP.append(data_corporate_technology[data_corporate_technology['Product Name']==i]['MRP per piece'].sum())
    d_cor_tech_inventory.append(data_corporate_technology[data_corporate_technology['Product Name']==i]['Factory Price per piece'].sum())
    d_cor_tech_quantity.append(data_corporate_technology[data_corporate_technology['Product Name']==i]['Quantity'].sum())
    d_cor_tech_profit.append(data_corporate_technology[data_corporate_technology['Product Name']==i]['Profit per piece'].sum())
d_cor_tech = np.array([d_cor_tech_product,d_cor_tech_MRP,d_cor_tech_inventory,d_cor_tech_quantity,d_cor_tech_profit]).T
d_cor_tech = pd.DataFrame(d_cor_tech,columns = ['d_cor_tech_product','d_cor_tech_MRP','d_cor_tech_inventory','d_cor_tech_quantity','d_cor_tech_profit'])
d_cor_tech[['d_cor_tech_MRP','d_cor_tech_inventory','d_cor_tech_quantity','d_cor_tech_profit']] = d_cor_tech[['d_cor_tech_MRP','d_cor_tech_inventory','d_cor_tech_quantity','d_cor_tech_profit']].apply(pd.to_numeric)
d_cor_tech = d_cor_tech.round(2)
d_cor_tech=d_cor_tech.sort_values(['d_cor_tech_profit'],ascending=False)

d_hof_os_product = []
d_hof_os_MRP = []
d_hof_os_inventory = []
d_hof_os_quantity = []
d_hof_os_profit = []
for i in data_homeOffice_officeSupplies['Product Name'].unique():
    d_hof_os_product.append(i)
    d_hof_os_MRP.append(data_homeOffice_officeSupplies[data_homeOffice_officeSupplies['Product Name']==i]['MRP per piece'].sum())
    d_hof_os_inventory.append(data_homeOffice_officeSupplies[data_homeOffice_officeSupplies['Product Name']==i]['Factory Price per piece'].sum())
    d_hof_os_quantity.append(data_homeOffice_officeSupplies[data_homeOffice_officeSupplies['Product Name']==i]['Quantity'].sum())
    d_hof_os_profit.append(data_homeOffice_officeSupplies[data_homeOffice_officeSupplies['Product Name']==i]['Profit per piece'].sum())
d_hof_os = np.array([d_hof_os_product,d_hof_os_MRP,d_hof_os_inventory,d_hof_os_quantity,d_hof_os_profit]).T
d_hof_os = pd.DataFrame(d_hof_os,columns = ['d_hof_os_product','d_hof_os_MRP','d_hof_os_inventory','d_hof_os_quantity','d_hof_os_profit'])
d_hof_os[['d_hof_os_MRP','d_hof_os_inventory','d_hof_os_quantity','d_hof_os_profit']] = d_hof_os[['d_hof_os_MRP','d_hof_os_inventory','d_hof_os_quantity','d_hof_os_profit']].apply(pd.to_numeric)
d_hof_os = d_hof_os.round(2)
d_hof_os=d_hof_os.sort_values(['d_hof_os_profit'],ascending=False)

d_hof_fur_product = []
d_hof_fur_MRP = []
d_hof_fur_inventory = []
d_hof_fur_quantity = []
d_hof_fur_profit = []
for i in data_homeOffice_furniture['Product Name'].unique():
    d_hof_fur_product.append(i)
    d_hof_fur_MRP.append(data_homeOffice_furniture[data_homeOffice_furniture['Product Name']==i]['MRP per piece'].sum())
    d_hof_fur_inventory.append(data_homeOffice_furniture[data_homeOffice_furniture['Product Name']==i]['Factory Price per piece'].sum())
    d_hof_fur_quantity.append(data_homeOffice_furniture[data_homeOffice_furniture['Product Name']==i]['Quantity'].sum())
    d_hof_fur_profit.append(data_homeOffice_furniture[data_homeOffice_furniture['Product Name']==i]['Profit per piece'].sum())
d_hof_fur = np.array([d_hof_fur_product,d_hof_fur_MRP,d_hof_fur_inventory,d_hof_fur_quantity,d_hof_fur_profit]).T
d_hof_fur = pd.DataFrame(d_hof_fur,columns = ['d_hof_fur_product','d_hof_fur_MRP','d_hof_fur_inventory','d_hof_fur_quantity','d_hof_fur_profit'])
d_hof_fur[['d_hof_fur_MRP','d_hof_fur_inventory','d_hof_fur_quantity','d_hof_fur_profit']] = d_hof_fur[['d_hof_fur_MRP','d_hof_fur_inventory','d_hof_fur_quantity','d_hof_fur_profit']].apply(pd.to_numeric)
d_hof_fur = d_hof_fur.round(2)
d_hof_fur=d_hof_fur.sort_values(['d_hof_fur_profit'],ascending=False)

d_hof_tech_product = []
d_hof_tech_MRP = []
d_hof_tech_inventory = []
d_hof_tech_quantity = []
d_hof_tech_profit = []
for i in data_homeOffice_technology['Product Name'].unique():
    d_hof_tech_product.append(i)
    d_hof_tech_MRP.append(data_homeOffice_technology[data_homeOffice_technology['Product Name']==i]['MRP per piece'].sum())
    d_hof_tech_inventory.append(data_homeOffice_technology[data_homeOffice_technology['Product Name']==i]['Factory Price per piece'].sum())
    d_hof_tech_quantity.append(data_homeOffice_technology[data_homeOffice_technology['Product Name']==i]['Quantity'].sum())
    d_hof_tech_profit.append(data_homeOffice_technology[data_homeOffice_technology['Product Name']==i]['Profit per piece'].sum())
d_hof_tech = np.array([d_hof_tech_product,d_hof_tech_MRP,d_hof_tech_inventory,d_hof_tech_quantity,d_hof_tech_profit]).T
d_hof_tech = pd.DataFrame(d_hof_tech,columns = ['d_hof_tech_product','d_hof_tech_MRP','d_hof_tech_inventory','d_hof_tech_quantity','d_hof_tech_profit'])
d_hof_tech[['d_hof_tech_MRP','d_hof_tech_inventory','d_hof_tech_quantity','d_hof_tech_profit']] = d_hof_tech[['d_hof_tech_MRP','d_hof_tech_inventory','d_hof_tech_quantity','d_hof_tech_profit']].apply(pd.to_numeric)
d_hof_tech = d_hof_tech.round(2)
d_hof_tech=d_hof_tech.sort_values(['d_hof_tech_profit'],ascending=False)