from src.logger import logging
import pandas as pd
import os
import sys
from src.exception import CustomException


from src.components import gemini_script
from src.components.gemini import Gemini
from src.constants import *
from src.entity.config_entity import Mssql, Env




class TrainPipeline:
    def __init__(self):
        self.gemini = Env()
        self.mssql = Mssql()
        

   
    def gemini_model(self):
        logging.info("Started Gemini Model Initiation")
        
        try:
            logging.info("Saving model")
            Gemini_config = Gemini(
                google_api=self.gemini,
                mssql_config=self.mssql
            )
            # Initialize an empty list to store all DataFrames
            all_dfs = []

            # List of product table names
            product_table_name_list = ["urls"]
            #product_table_name_list = ["enhance_product_variants"]

            for product_table_name in product_table_name_list:
                # Hardcoded unique supplier IDs for the example
                unique_supplier_id = [1]

                logging.info(f"Processing table: {product_table_name} with supplier IDs: {unique_supplier_id}")

                for sup_id in unique_supplier_id:
                    # Retrieve DataFrame list
                    df_list = Gemini_config.initiate_data(table_name=product_table_name, supplier_id=str(sup_id))
                    # Extend the list of all DataFrames
                    all_dfs.extend(df_list)
                    logging.info(f"Data for table {product_table_name} and supplier ID {sup_id} saved successfully")

            # Concatenate all DataFrames into a single DataFrame
            concatenated_df = pd.concat(all_dfs, ignore_index=True)

            # Save the concatenated DataFrame to a CSV file
            concatenated_df.to_csv('all_data.csv', index=False)

            logging.info("Exited the gemini_model function from TrainPipeline class")
            

        except Exception as e:
            logging.error(f"Error in gemini_model: {e}")
            raise CustomException(e,sys)

    def run_pipeline(self) -> None:
        try:
            logging.info("Started Model")
            self.gemini_model()
        except Exception as e:
            logging.error(f"Error running pipeline: {e}")
            raise e