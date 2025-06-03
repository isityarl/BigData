# Big Data things

## Overview

`BigData/`, contains a big data processing, analysis, and technologies. Each subdirectory represents a distinct area of work or a specific task.

One of the key projects included is the **New York City Taxi Trip Analysis**, primarily located within the `NYtaxi/` subdirectory. Other areas of exploration include work with `hbase`, `spark`, and `streaming` technologies.

## Data Sources

**To run and explore, you need to download data files from:**

* **Green Taxi Data (`green.csv`) for NYC Taxi Analysis:**
    * Download Link: `https://drive.google.com/uc?export=download&id=13fSdj3d8BiXLcuDy6OJ2OOboXP1SnZ0n`
    * Description: `https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_green.pdf`

* **Yellow Taxi Data (`yellow.csv`) for NYC Taxi Analysis:**
    * Download Link: `https://drive.google.com/uc?export=download&id=1Prcm3duikQgXbbdmZrdn8-LSCL8whYcY`
    * Description: `https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf`

* **Trip Data (`2008.csv` `airports-data.csv` - used in Spark subdirectory):**
    * Download Link: `https://drive.google.com/uc?export=download&id=1eQhJwxwpIoCX7NyefkQPg_2NK13Ow1TR`, `https://drive.google.com/uc?export=download&id=1Vwk0hHqkSnydFdnYQIlJgv0phbhlUxfL`
    * Description: `flight and airport informations`
     
* **Trip Data (`book.txt` - used in Streaming/PirateMapper.py):**
    * Download Link: `https://drive.google.com/uc?export=download&id=1Q3B_ocKCLI9h5VjrkrXDvywIw-uG3j3F`
    * Description: `large text for applying pirate slangs`
 
* **`for other streamings data has been lost`**  

Please ensure files are placed in the correct locations as specified for the analysis scripts and notebooks to function correctly.

## About

The `BigData/` directory is organized into the following key subdirectories:

* **`NYtaxi/`**
    * This subdirectory contains the **New York City Taxi Trip Analysis**.
    * `Overall analysis: preprocessing(cleaning), EDA, noting insights, predicting(LinReg, RanForestReg)`   

* **`hbase/`**
    * `Selecting and counting requests in the selected hour, using HBase, HDFS`

* **`spark/`**
    * `Frequency analysis and flight data aggregation using both PySpark RDD and DataFrame APIs. To compare them.`

* **`streaming/`**
    * month/ `MapReduce: Job 1: Counts updates per month; Job 2: Counts and ranks activity by hour`
    * TrendingWordcount/ `Built a three MapReduce steps that filters and counts clean tweet words by day, then computes each word’s daily usage as a percentage of its total usage across the dataset`
    * vectors/ `two MapReduce steps: the first mapper and reducer calculated the product of values per key, then use of sum aggregation to get total`
    * PirateMapper.py `Convertion of some words and endings into “pirate speak” using a dictionary and random slang replacements, then outputs the transformed pirate-style text`

