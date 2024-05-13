# Crowdfunding_ETL


# **Overview:**
The objective for this assignment is to take crowdsourcing data from two excel files, transform them into 4 dataframes and import these dataframes into a Postgres SQL database.



# **The following files were used:**

## **Initial Excel Files:**
crowdfunding.xlsx

contacts.xlsx

-----

# **Created DataFrames exported to CSV:**
## **Category and Subcategory DataFrames:**

* Read "crowdfunding_info_df" file into a Pandas DataFrame.
  ![crowdfunding_info_df](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/306843c0-8cca-4f3e-afc2-79f2ee0bb8d1)
  
* Created a cleaned dataframe for category.
  
  ![category_df](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/70939c6e-3e5f-44aa-99ee-5c3996b16991)

* Created a cleaned dataframe for subcategory.
  
  ![subcategory_df](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/ec587ebf-24e5-4404-8215-df26b4b74a02)

* Exported dataframes as CSV files.


## **Campaign DataFrame:**

* Created a copy of "crowdfunding_info_df" dataframe and named it campaign_df.
* Merged "campaign_df" with the "category_df" on the "category" column.
* Merged "campaign_df" with the "subcategory_df" on the "category" column.
* Cleaned up campaign dataframe.
  ![campaign_df](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/33307302-b2cf-43ed-85b1-87f0361f947d)

* Exported dataframe as a CSV files.


## **Contacts DataFrame:**

* Read "contact_info_df" into a Pandas DataFrame using the `header=3` parameter when reading in the data.

  ![contact_info_df](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/38571ec7-eb03-4158-b6ba-9849e03eff76)
  
* Created a cleaned contacts dataframe.
  
  ![contacts_df](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/66e055ae-fdac-43b3-b9c3-94b63e8c2a84)

* Exported "contacts_df_clean" DataFrame as a CSV file. 

# **Created Database Files:**
## **The ERD**

![ETL_ERD](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/738caf47-0c60-433a-a40e-1d26fde7c509)

