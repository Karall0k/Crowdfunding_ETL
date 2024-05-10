# Crowdfunding_ETL

By Karesse Lockard, Medha Mallampati, and Christina Gabriel



# **Overview:**
The objective for this assignment is to take crowdsourcing data from two excel files, transform them into 4 dataframes and import these dataframes into a Postgres SQL database.



# **The following files were used:**

# **Initial Excel Files:**
crowdfunding.xlsx
contacts.xlsx


# **Created DataFrames exported to CSV:**
category.csv
subcategory.csv
campaign.csv
contacts.csv


# **Created Database Files:**
Crowdfunding_db_schema.sql
The ERD



# **Category and Subcategory DataFrames (Christina):**

* Set up dependencies. 
* Created new directory path. 
* Read "crowdfunding_info_df" file into a Pandas DataFrame.
* Created "category" column which only contains the category titles.
* Created "subcategory" column which only contains the subcategory titles.
* Counted number of values in categories and subcategories columns.
* Created sequential "category_id" list comprehension from cat1 to cat*n*.
* Created sequential "subcategory_id" list comprehension from subcat1 to subcat*n*.
* Created a dataframe for category and subcategory.
* Exported dataframes as CSV files.



# **Campaign DataFrame (Medha Mallampati):**

* Created a copy of "crowdfunding_info_df" dataframe and named it campaign_df.
* Renamed columns 'blurb' to 'description', 'launched_at' to 'launch_date', and 'deadline' to 'end_date'.
* Converted the goal and pledged columns to a `float` data type.
* Formatted the 'launch_date' and 'end_date' columns to datetime format.
* Merged "campaign_df" with the "category_df" on the "category" column.
* Merged "campaign_df" with the "subcategory_df" on the "category" column.
* Dropped the following columns from "campaign_df": 'staff_pick', 'spotlight', 'category & sub-category', 'category', 'subcategory'. 
* Exported dataframe as a CSV files.



# **Contacts DataFrame (Karesse Lockard):**

* Read "contact_info_df" into a Pandas DataFrame using the `header=3` parameter when reading in the data.
* Iterated through "contact_info_df" and converted each row to a dictionary.
* Created a "contact_info" DataFrame and added each list of values, i.e., each row to the 'contact_id', 'name', 'email' columns.
* Created a "first"name" and "last_name" column with the first and last names from the "name" column. 
* Dropped the "contact_name" column.
* Reorded the columns.
* Exported "contacts_df_clean" DataFrame as a CSV file. 

