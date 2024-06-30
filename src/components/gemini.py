import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from src.exception import NerException
from src.logger import logging
import tqdm
import time
import json
from src.entity.config_entity import  Mssql,Env

import google.generativeai as genai
import requests


@dataclass
class Gemini:

    def __init__(self,google_api: Env,mssql_config: Mssql):
        self.mssql_config = mssql_config
        

    def gemini_api(self):
        """
        Apply gemini api and call it later in prompt section with image input for response.
        """
        try:
            #define api key
            self.api_key = self.google_api.gemini_api
            
            #configure api key
            genai.configure(api_key=self.api_key)
            
            #Define which model we are going to use
            gemini_model = genai.GenerativeModel(self.google_api.model_name)
            logging.info(f"Gemini model configured: {gemini_model}")
            
            #return model
            return gemini_model
        
        except Exception as e:
            logging.error(f"Failed to configure Gemini API: {e}")
            
            NerException(e,sys)
        

    def read_sql(self):
        pass

    def query(self):
        pass

    def clean_data(self):
        pass

    def insert_data(self):
        pass

    def fetch_column_name(self):
        pass

    def initiate_data(self,table_name,supplier_id):

        try:
            # Call gemini API function to get the GEMINI model
            self.gemini_api_key()

            # Initialize an empty list to store DataFrame outputs
            df_list = []

            # Define the SQL query with dynamic table name and supplier ID
            query = f"""
                    SELECT TOP (500) * 
                    FROM {table_name} 
                    WHERE supplierId = '{supplier_id}' 
                    AND status = 1  AND isDeleted = 0 AND  ( geminiStatus = 0 or geminiStatus is NULL) AND isDuplicateBarcode = 0 AND isEnhanced = 1 AND uniqueId IS NOT NULL AND Parent_SKU NOT LIKE '-P'
                    """
            #print(query)

            # Read data from MSSQL and append it to the list
            df_data = self.read_data_from_mssql(query)
            df_list.append(df_data)
        except Exception as e:
            raise e
