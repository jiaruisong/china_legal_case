# Setup.ipynb
load necessary package and mount storage from azure blob and datalake gen2.

# filtering & sampling
filter out drug_related, fraud, theft, and traffic_accident cases. Then sample 1% of each categories. store them in datalake gen 2.

# location_extraction
use pyahocorasick and chinese_province_city_area_mapper to extract the location from 'court' column in the dataset

# drug_type_amount_extraction
use LLM to extract the drug type and amount involved in the cases. following these steps:
1. **Trim to Relevant Part**, to isolate relevant case sections for better results and lower cost; 
2. **Post Request and Fetch Claude Response**, to extract data using AI. Here we use json to make sure LLM's response is formatted; 
3. **Read CSV and Extract Drug Type and Amount in Bunk**, run the above two functions and apply them to all files in bunk.

# penalty_extraction
apply a similar method to drug_type_amount_extraction, extract the penalty information from judgments.

# data cleaning for drug type, amount and penalty
as the drug type, amount and penalty are extracted using LLMs, there could be issues with edge cases, therefore, data cleaning is needed.

# future development
1. extract lawyer representation
2. introducing RAG

