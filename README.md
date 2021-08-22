# shopify-data-syncing-system

This project integrates live Shopify data into our PostgreSQL instance, allowing us to consolidate all of our data into a single location.
Each e-commerce store has suppliers, product categories/collections, orders, and courier/shipping components. For the web stores developed through the Shopify platform, these data are stored in the RestAPI of the Shopify server. Firstly, the RestAPI is accessed externally through our code after authorization from Shopify with the generation of a key for the API of that particular store. After being authorized to access the API, we extract the data of our requirement from there. After the extraction of the data, a new database is generated in our own server or local device. PostgreSQL is implemented for the completion of this task.

Steps to run this:
1. Clone the repository
2. In main.py:\
   (a) In the variables, JSON_count and Jsondata, add the username, password, and API version from your Shopify account\
   (b) Add the username, password, hostname, and database name from your PostgreSQL account
3. Run main.py
