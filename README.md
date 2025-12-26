# Azure Data Engineer Project:


In this project, I worked with the Spotify dataset and implemented an incremental data loading pipeline using Azure Data Factory (ADF). The source system was Azure SQL Database, which contained multiple tables. I leveraged high watermark concepts to handle incremental loads and also implemented logic to manage backfill scenarios in ADF.

The data from the source was loaded into the Bronze layer in Parquet format, and I used Unity Catalog to create structured schemas for the Silver and Gold layers. In the Silver layer, I processed the data using streaming reads. A separate utils class was created to perform basic transformations, which was then called in the main notebook to maintain modularity. After transformations, the data was written into the Silver tables.

To automate query generation, I used the Jinja library, enabling dynamic SQL queries without manual intervention. In the Gold layer, I implemented CDC (Change Data Capture) using Delta Live Tables, and applied SCD Type 2 methodology for historical tracking and data versioning.

Overall, this project demonstrates an end-to-end ETL/ELT pipeline on Databricks with incremental loads, streaming processing, modular transformations, and CDC implementation, following bronze-silver-gold architecture.
