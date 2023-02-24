#!/usr/bin/env python
# coding: utf-8

# In[200]:


import pandas as pd
import numpy as np


# # 1. Read the demand transaction file and print the first 15 rows and dtypes

# In[201]:


demand_transaction = pd.read_csv("https://raw.githubusercontent.com/Laxminarayen/Inceptez-DS-Batch20/main/12.%20Preprocessing/Demand_txn_updated.csv")


# In[202]:


demand_transaction.shape


# In[203]:


demand_transaction.head(15)


# # 2. Convert the transaction date column to a date column using pd.to_datetime function

# In[135]:


demand_transaction['Transaction_Date'] = pd.to_datetime(demand_transaction ['Transaction_Date']).dt.date


# In[136]:


demand_transaction.head(15)


# In[137]:


demand_transaction_cpy = demand_transaction.copy()


# In[138]:


demand_transaction_cpy.head(15)


# # 3. Subset the dataframe for transaction date greater than '2016-08-01'

# In[139]:


demand_transaction_cpy ['Transaction_Date'].subset = ('Transaction_Date'>'2016-08-01',True)


# In[140]:


demand_transaction_cpy.head(15)


# # 4. Look for unique values in Mapped_Sales_Type

# In[141]:


demand_transaction_cpy['Mapped_Sales_Type'].unique()


# # 5. Subset the entire dataframe, based on the below condition, to a new dataframe and work
# on the following questions
# a. Condition: Avg_Discount_Percent_On_Discounted_Items should be less than 1.0
# b. Check for sanity if the new dataframe contains
# Avg_Discount_Percent_On_Discounted_Items greater than or equal to 1.0
# 

# In[142]:


demand_transaction_dis = demand_transaction_cpy [demand_transaction_cpy['Avg_Discount_Percent_On_Discounted_Items']<1.0]


# In[143]:


demand_transaction_dis


# In[144]:


demand_transaction_dis.shape


# In[145]:


demand_transaction_dis1 =demand_transaction_cpy [demand_transaction_cpy['Avg_Discount_Percent_On_Discounted_Items']>=1.0]


# In[146]:


demand_transaction_dis1


# In[147]:


demand_transaction_dis1.shape


# # 6. Groupby 'City', 'Mapped_Sales_Type', 'Mapped_Item_Code', 'Transaction_Date' and
# perform following aggregate operations on respective columns as mentioned (note: Only
# one groupby to do all the below aggregations)
# a. Quantity_Sold – sum
# b. Median_Price – median
# c. Effective_Price – median
# 

# In[148]:


demand_transaction.groupby(['City','Mapped_Sales_Type','Mapped_Item_Code','Transaction_Date']).aggregate ({'Quantity_Sold':'sum','Median_Price':'median','Effective_Price':'median'})


# # 7. Display the data for Effective_Price = not null and just print the last 5 rows (hint: use .notnull
# function)
# 

# In[156]:


demand_transaction_effective = demand_transaction[demand_transaction['Effective_Price'].notnull()].tail(5)


# In[157]:


demand_transaction_effective


# # 8. Display the data for city = Chennai AND Mapped_Sales_Type = Delivery and print top 5
# records (hint use loc function to subset, then “&” operator to filter both the above cities)
# 

# In[164]:


demand_transaction 


# In[169]:


demand_transaction_chennai =demand_transaction[(demand_transaction['City']=='Chennai') & (demand_transaction['Mapped_Sales_Type']=='Delivery')]


# In[170]:


demand_transaction_chennai


# # 9. Display the data for the column “Day” with values Mon, Tue and Wed (hint: use .isin
# function)
# 

# In[178]:


demand_transaction_day = demand_transaction[(demand_transaction['Day'].isin(['Mon','Tue','Wed']))]


# In[179]:


demand_transaction_day


# # 10. Display the data for Percent_Quantity_With_Discount not equal to 0.0 (hint: loc function
# with != operator)
# 

# In[183]:


demand_transaction_percent = demand_transaction[demand_transaction['Percent_Quantity_With_Discount']!=0]


# In[184]:


demand_transaction_percent


# # 11. Add a column “Range” to the existing dataframe for below condition
# a. 1 for Effective_Price > 500
# b. 0.5 otherwise
# 

# In[205]:


counter = 0
for i in demand_transaction['Effective_Price']:
    if i>500:
        demand_transaction.loc[counter,'range'] =1
    else:
        demand_transaction.loc[counter,'range'] = 0.5    
            
        counter = counter +1


# In[206]:


demand_transaction[['Effective_Price', 'range']]


# In[ ]:




