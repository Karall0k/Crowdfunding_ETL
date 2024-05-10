#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import dependencies
import pandas as pd
import numpy as np
pd.set_option('max_colwidth', 400)


# In[2]:


import os

# Specify the new directory path
new_directory = "C:\\Users\\chris\\OneDrive\\Documents\\Data Science Bootcamp\\Project 2\\Starter_Files\\Starter_Files"

# Change the current working directory
os.chdir(new_directory)

# Print the new current working directory
print("New Current Working Directory:", os.getcwd())


# In[3]:


pwd


# ### Extract the crowdfunding.xlsx Data

# In[4]:


# Read the data into a Pandas DataFrame
crowdfunding_info_df = pd.read_excel('Resources/crowdfunding.xlsx')
crowdfunding_info_df.head()


# In[5]:


# Get a brief summary of the crowdfunding_info DataFrame.
crowdfunding_info_df.info()


# ### Create the Category and Subcategory DataFrames
# ---
# **Create a Category DataFrame that has the following columns:**
# - A "category_id" column that is numbered sequential form 1 to the length of the number of unique categories.
# - A "category" column that has only the categories.
# 
# Export the DataFrame as a `category.csv` CSV file.
# 
# **Create a SubCategory DataFrame that has the following columns:**
# - A "subcategory_id" column that is numbered sequential form 1 to the length of the number of unique subcategories.
# - A "subcategory" column that has only the subcategories. 
# 
# Export the DataFrame as a `subcategory.csv` CSV file.

# In[6]:


# Get the crowdfunding_info_df columns.
crowdfunding_info_df.columns


# In[7]:


# Assign the category and subcategory values to category and subcategory columns.
crowdfunding_info_df[['category', 'subcategory']] = crowdfunding_info_df['category & sub-category'].str.split('/', n=1, expand=True)


# In[8]:


# Get the unique categories and subcategories in separate lists.
categories = crowdfunding_info_df['category'].unique().tolist()
subcategories = crowdfunding_info_df['subcategory'].unique().tolist()

print(categories)
print(subcategories)


# In[9]:


# Get the number of distinct values in the categories and subcategories lists.
print(len(categories))
print(len(subcategories))


# In[10]:


# Create numpy arrays from 1-9 for the categories and 1-24 for the subcategories.
category_ids = np.arange(1, 10)
subcategory_ids = np.arange(1, 25)

print(category_ids)
print(subcategory_ids)


# In[11]:


# Use a list comprehension to add "cat" to each category_id. 
category_ids = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

cat_ids = ['cat' + category_id for category_id in category_ids]

print(cat_ids)


# In[12]:


# Use a list comprehension to add "subcat" to each subcategory_id.    
subcategory_ids = ['1',  '2',  '3',  '4',  '5',  '6',  '7',  '8',  '9', '10', '11', '12', 
                   '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

scat_ids = ['subcat' + subcategory_id for subcategory_id in subcategory_ids]

print(scat_ids)


# In[13]:


# Create a category DataFrame with the category_id array as the category_id and categories list as the category name.
category_id = ['cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8', 'cat9']  


categories = ['food', 'music', 'technology', 'theater', 'film & video', 'publishing', 'games', 'photography', 'journalism']  


category_df = pd.DataFrame({
    "category_id": category_id,
    "category": categories
})


# In[14]:


# Create a category DataFrame with the subcategory_id array as the subcategory_id and subcategories list as the subcategory name. 
subcategory_id = ['subcat1', 'subcat2', 'subcat3', 'subcat4', 'subcat5', 'subcat6', 'subcat7', 'subcat8', 'subcat9', 'subcat10', 'subcat11', 
                  'subcat12', 'subcat13', 'subcat14', 'subcat15', 'subcat16', 'subcat17', 'subcat18', 'subcat19', 
                  'subcat20', 'subcat21', 'subcat22', 'subcat23', 'subcat24']  


subcategories = ['food trucks', 'rock', 'web', 'plays', 'documentary', 'electric music', 'drama', 'indie rock', 'wearables', 'nonfiction', 'animation', 
              'video games', 'shorts', 'fiction', 'photography books', 'radio & podcasts', 'metal', 'jazz', 'translations', 
              'television', 'mobile games', 'world music', 'science fiction', 'audio']  


subcategory_df = pd.DataFrame({
    "subcategory_id": subcategory_id,
    "subcategory": subcategories
})


# In[15]:


category_df


# In[16]:


subcategory_df


# In[17]:


# Export categories_df and subcategories_df as CSV files.
category_df.to_csv("Resources/category.csv", index=False)

subcategory_df.to_csv("Resources/subcategory.csv", index=False)

