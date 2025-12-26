# Spotify Data Pipeline Project

## Project Overview
This project implements an **incremental ETL pipeline** for the Spotify dataset using **Databricks**, **Azure Data Factory (ADF)**, and **Azure SQL Database**. The pipeline follows a **Bronze → Silver → Gold** architecture with **streaming**, **incremental loads**, and **CDC (Change Data Capture)**.  

Key features:
- Incremental data loading with **high watermark** logic
- Handling **backfill scenarios** in ADF
- Data stored in **Parquet format** in the Bronze layer
- **Unity Catalog** schemas for Silver and Gold layers
- Streaming reads in Silver, with modular transformations using **utils class**
- Dynamic SQL generation using **Jinja**
- CDC and **SCD Type 2** implementation in Gold layer using **Delta Live Tables**

---

## Data Pipeline Architecture

### **1. Bronze Layer**
The raw data from **Azure SQL DB** is loaded incrementally into the Bronze layer in **Parquet format**.

---

### **2. Silver Layer**
In the Silver layer:
- Data is read using **streaming**
- Basic transformations are applied via a **utils class**
- Transformed data is written into **Silver tables**

  ![Silver Layer]https://github.com/csamrit123-lang/azureproject/blob/main/adb_pipeline_3.png

---

### **3. Gold Layer**
The Gold layer applies:
- **CDC (Change Data Capture)**
- **SCD Type 2** for historical tracking using **Delta Live Tables**

![Gold Layer](https://github.com/csamrit123-lang/azureproject/blob/main/adb_gold_pipeline_4.png)

---

## Workflow with Azure Data Factory
- Multiple tables from Azure SQL DB are ingested
- **High watermark logic** ensures incremental loading
- **Backfill handling** is implemented for historical data
- ADF pipelines orchestrate the end-to-end flow

![ADF Pipeline](![Bronze Layer](https://github.com/csamrit123-lang/azureproject/blob/main/pipeline_1.png))
![ADF Pipeline](https://github.com/csamrit123-lang/azureproject/blob/main/pipeline_2.png)

---

