import streamlit 
import pandas as pd
import requests
import snowflake.connector
import json

streamlit.title("This application is to ingest the data into SNOWFLAKE")
streamlit.header('Click on the button to trigger data loading')

request_api=requests.get('https://api.senticrypt.com/v1/history/index.json')
data=request_api.text
data=json.loads(data)

streamlit.dataframe(data)
