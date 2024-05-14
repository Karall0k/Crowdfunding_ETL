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


## **SQL**

  ### **Created Database**
  * Create a database from the four exported dataframes: campaign.csv, category.csv, contacts.csv, subcategory.csv.


  ### **Created Schema**
  * Created tables in this specific order: "category", "subcategory", "contacts", then "campaign".


  ### **Created Queries**
  * Created the queries in SQL:
    * Query 1: ![category_query](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/ec31afdb-f9b6-4b08-99b4-fe782d38a937)

      ![category_table](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/3aee9f2e-c555-46ef-99ec-14212b70f777)


    * Query 2:
      ![subcat_query](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/4261bb99-2925-46f9-bab4-d0df96439d13)

      ![subcat_table1](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/68b124f2-43bd-4f5c-ada6-5119336c4ffa)

      ...
    
      ![subcat_table2](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/320837cd-1723-4543-8c04-7cd40d8c6686)


    * Query 3:
      ![contacts_query](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/17acfbb0-1971-4a21-8dbd-b4b3315b5415)

      ![contact_table1](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/15b6b80f-7384-4ffc-a779-e2fdbfa74422)

      ...
    
      ![contact_table2](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/ce330821-9f4c-46ce-bb86-01a3cfb3c326)


    * Query 4:
      ![campaign_query](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/318f362b-2593-47c4-b8f1-a363b1300770)

      ![camp_table1](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/2c9c1bd9-a597-4c92-8d02-d110594d5fe4)

      ...

      ![camp_table2](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/49241bed-ecf9-4aa7-947d-c56316e242e1)

      
    * Query 5: Created the merged queries.

      ![created_merge_query](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/2fe856e1-a6d9-452f-be49-42918b5d6335)

      ![created_merge_table](https://github.com/Karall0k/Crowdfunding_ETL/assets/159741444/4ed929fe-8e6d-4778-b603-479ae8da20c5)


