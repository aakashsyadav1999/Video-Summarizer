from src.logger import logging
import pandas as pd
import os
import sys
<<<<<<< HEAD
from src.exception import NerException
from dataclasses import dataclass

from src.components import gemini
from src.components.gemini import Gemini
from src.constants import *
from src.entity.config_entity import Mssql, Multithreading, Env, FetchingUrl

@dataclass
=======
from src.exception import CustomException


from src.components import gemini_script
from src.components.gemini import Gemini
from src.constants import *
from src.entity.config_entity import Mssql, Env




>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492
class TrainPipeline:
    def __init__(self):
        self.gemini = Env()
        self.mssql = Mssql()
<<<<<<< HEAD
        self.multithreading = Multithreading()
        self.fetching_url_config = FetchingUrl()

    def gemini_model(self):
        logging.info("Started Gemini Model Initiation")
=======
        

   
    def gemini_model(self):
        logging.info("Started Gemini Model Initiation")
        
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492
        try:
            logging.info("Saving model")
            Gemini_config = Gemini(
                google_api=self.gemini,
<<<<<<< HEAD
                mssql_config=self.mssql,
                multithreading_config=self.multithreading,
                fetching_url_config= self.fetching_url_config
=======
                mssql_config=self.mssql
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492
            )
            # Initialize an empty list to store all DataFrames
            all_dfs = []

            # List of product table names
<<<<<<< HEAD
            product_table_name_list = ["raw_urls_data"]
=======
            product_table_name_list = ["urls"]
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492
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

<<<<<<< HEAD
            # # Concatenate all DataFrames into a single DataFrame
            # concatenated_df = pd.concat(all_dfs, ignore_index=True)

            # # Save the concatenated DataFrame to a CSV file
            # concatenated_df.to_csv('all_data.csv', index=False)
=======
            # Concatenate all DataFrames into a single DataFrame
            concatenated_df = pd.concat(all_dfs, ignore_index=True)

            # Save the concatenated DataFrame to a CSV file
            concatenated_df.to_csv('all_data.csv', index=False)
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492

            logging.info("Exited the gemini_model function from TrainPipeline class")
            

        except Exception as e:
            logging.error(f"Error in gemini_model: {e}")
<<<<<<< HEAD
            raise NerException(e,sys)
=======
            raise CustomException(e,sys)
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492

    def run_pipeline(self) -> None:
        try:
            logging.info("Started Model")
            self.gemini_model()
        except Exception as e:
            logging.error(f"Error running pipeline: {e}")
<<<<<<< HEAD
            raise e


=======
            raise e
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492
