# Databricks notebook source
# MAGIC %md
# MAGIC # clean drug type

# COMMAND ----------

# MAGIC %md
# MAGIC ## inspect unique value

# COMMAND ----------

import os
import pandas as pd


def align_dataframe(base_path, cause):
    # Using dbutils.fs.ls to list directories/files
    files = dbutils.fs.ls(base_path)

    # Initialize a list to collect all unique values across files
    unique_values = []
    i = 0

    for sub_file in files:
        if sub_file.name.endswith(".csv"):
            # Reading CSV file into DataFrame
            # Convert to local file path if necessary
            file_path = sub_file.path.replace("dbfs:", "/dbfs")
            df = pd.read_csv(file_path, on_bad_lines='skip')

            i += 1
            
            for x in ['a', 'b']:
                try:
                    # Get unique values from the dataframe
                    unique_drug_values = df[f'drug_{x}'].unique()
                    # Store them in the list
                    unique_values.extend(unique_drug_values)
                    print(f"{i}, Unique values for drug_{x} in {file_path}: {unique_drug_values}")
                except KeyError:
                    print("key error", x, "in file path:", file_path)
                    continue
    
    # Find overall unique values across all files
    overall_unique_values = set(unique_values)
    print("Overall unique values across all files:", overall_unique_values)


base_path = "mnt/processed_data_criminal_case_analysis/drug_related_DrugTypeAmount_Penalty_Location_DataframeAlignment_March_20"

causes_of_action = ["drug_related"]

for cause in causes_of_action:
    align_dataframe(base_path, cause)

