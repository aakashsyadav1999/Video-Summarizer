<<<<<<< HEAD
import re
import os
import sys
from src.logger import logging
from src.exception import NerException
from dataclasses import dataclass
import pandas as pd
from tqdm import tqdm
import time
import PIL.Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from PIL import Image, UnidentifiedImageError
from dotenv import load_dotenv
import google.generativeai as genai
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from io import BytesIO
from urllib.parse import urlparse
from src.entity.config_entity import Multithreading, Mssql, Env,FetchingUrl
from src.utils.common import MssqlDB
import json
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from youtube_transcript_api import YouTubeTranscriptApi
from google.api_core.exceptions import InternalServerError
from urllib.parse import urlparse, parse_qs



load_dotenv()

@dataclass
class Gemini:

    def __init__(
                
                self,
                google_api: Env,
                mssql_config: Mssql,
                fetching_url_config: FetchingUrl,
                multithreading_config: Multithreading
                
                ):
                
        self.google_api = google_api
        self.mssql_config = mssql_config
        self.multithreading_config = multithreading_config
        self.fetching_url_config = fetching_url_config
        self.db_name = self.mssql_config.mssql_product
        self.db = MssqlDB(self.mssql_config.mssql_product)
    
    def gemini_api_vision_pro(self):
=======
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
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492
        """
        Apply gemini api and call it later in prompt section with image input for response.
        """
        try:
            #define api key
            self.api_key = self.google_api.gemini_api
            
            #configure api key
            genai.configure(api_key=self.api_key)
            
            #Define which model we are going to use
<<<<<<< HEAD
            gemini_model = genai.GenerativeModel(self.google_api.model_name_vision_pro)
=======
            gemini_model = genai.GenerativeModel(self.google_api.model_name)
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492
            logging.info(f"Gemini model configured: {gemini_model}")
            
            #return model
            return gemini_model
<<<<<<< HEAD
        except Exception as e:
            logging.error(f"Failed to configure Gemini API: {e}")
            
            Exception(e,sys)

    def gemini_api_pro(self):
        """
        Apply gemini api and call it later in prompt section with image input for response.
        """
        try:
            #define api key
            self.api_key = self.google_api.gemini_api
            
            #configure api key
            genai.configure(api_key=self.api_key)
            
            #Define which model we are going to use
            gemini_model = genai.GenerativeModel(self.google_api.model_name_pro)
            logging.info(f"Gemini model configured: {gemini_model}")
            
            #return model
            return gemini_model
        except Exception as e:
            logging.error(f"Failed to configure Gemini API: {e}")
            
            Exception(e,sys)

    def read_data(self, query: str) -> pd.DataFrame:
        """
        Reads data from MSSQL database using the provided query and returns it as a pandas DataFrame.
        """
        try:
            # Execute the query
            result = self.db.execute_one_query(query)
            
            # Log the raw result for debugging
            logging.info(f"Raw result from MSSQL: {result}")

            # Convert the result to a DataFrame
            df = self.convert_to_dataframe(result)
            
            # Log the fetched data for debugging
            logging.info(f"Fetched data from MSSQL: {df.head()}")
            
            return df
        except Exception as e:
            logging.error(f"Error reading data from MSSQL: {e}")
            raise e

    def convert_to_dataframe(self, result) -> pd.DataFrame:
        """
        Converts query result to a pandas DataFrame.
        """
        if isinstance(result, list) and all(isinstance(row, dict) for row in result):
            # Convert list of dictionaries to DataFrame
            df = pd.DataFrame(result)
        elif isinstance(result, list) and all(isinstance(row, (list, tuple)) for row in result):
            # Convert list of lists/tuples to DataFrame
            df = pd.DataFrame(result)
        else:
            logging.error("Query result is not in a recognizable format")
            raise ValueError("Query result is not in a recognizable format")
        
        return df


    def fetch_prompt(self,supplier_id: str) -> str:
        """
        We fetch prompt from table where clients have entered there custom prompt

        """

        try:
            query = f"SELECT custom_prompt FROM gemini.prompt WHERE id = '{supplier_id}'"
            result = self.db.execute_one_query_1(query)
            logging.info(f"Raw result from integration database: {result}")
            if isinstance(result, list) and result:
                prompt_text = result[0][0]
                logging.info(f"Fetched prompt from integration database: {prompt_text}")
                return prompt_text
            else:
                raise ValueError(f"No prompt found for supplier_id: {supplier_id}")
        except Exception as e:
            logging.error(f"Error fetching prompt from integration database: {e}")
            raise Exception(e, sys)


    def _fetch_urls(self, urls, max_retries=None):
        if max_retries is None:
            max_retries = self.fetching_url_config.max_retries
        
        session = requests.Session()
        retry = Retry(
            connect=self.fetching_url_config.retry_connect, 
            backoff_factor=self.fetching_url_config.back_of_factor
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        for _ in range(max_retries):
            try:
                response = session.get(urls)
                response.raise_for_status()  # Raise an exception for any HTTP errors
                
                # Check if the URL ends with a common image file extension
                if any(urls.lower().endswith(ext) for ext in ('.jpg', '.jpeg', '.png', '.gif')):
                    # Validate image using PIL
                    img = Image.open(BytesIO(response.content))
                    img.verify()  # Verify image integrity
                
                return response  # Return the response if no exceptions occurred
            except (UnidentifiedImageError, IOError) as e:
                logging.warning(f"Error fetching or validating from URL: {urls} - Retrying... ({e})")
            except requests.exceptions.RequestException as e:
                logging.warning(f"Error fetching from URL: {urls} - Retrying... ({e})")
        
        raise Exception(f"Failed to fetch from URL after {max_retries} retries: {urls}")
        
    def is_image_url(self,url):
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
        parsed = urlparse(url)
        path = parsed.path
        ext = os.path.splitext(path)[1].lower()
        return any(ext.endswith(image_ext) for image_ext in image_extensions)
        
    def get_content_type(self,url):
        # Example implementation to determine content type based on URL
        if 'youtube.com' in url:
            return 'video/youtube'
        elif 'example.com/article' in url:
            return 'text/html'
        # Add more conditions as needed for different content types
        else:
            return url

    def fetch_image(self,url):
        response = requests.get(url)
        response.raise_for_status()
        return response

    def fetch_content(self,url, content_type):
        headers = {'Accept': content_type}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response
    
    def get_video_transcripts(self,video_id):
        try:
            transcription_list = YouTubeTranscriptApi.get_transcript(video_id)
            transcription = " ".join([transcript["text"] for transcript in transcription_list])
            return transcription

        except Exception as e:
            raise e
        
    def extract_video_id(self,youtube_url):
        """
        Extracts the video ID from a YouTube URL.
        """
        parsed_url = urlparse(youtube_url)
        
        # Check if the video ID is in the path (for short URLs)
        if parsed_url.path.startswith('/'):
            video_id = parsed_url.path.split('/')[-1]
            return video_id
        
        # Check if the video ID is in the query parameters (for standard URLs)
        query_params = parse_qs(parsed_url.query)
        video_id = query_params.get('v', [None])[0]
        
        if video_id:
            return video_id
        else:
            raise ValueError("Video ID not found in URL")
        
    def query(self, urls,supplier_id, prompt, table_name, row):
        """
        Processes various URLs, generates content using Gemini API, and handles retries.
        """
        max_retries = 5
        backoff_factor = 1
        content_type = None
        content_parts = None

        try:
            for url in urls:
                parsed_url = urlparse(url)
                if not parsed_url.scheme:
                    url = "https://" + url

                if self.is_image_url(url):
                    model = self.gemini_api_pro()

                    try:
                        response = self.fetch_image(url)

                        img = Image.open(BytesIO(response.content))
                        img.load()

                        content_parts = [
                            {'text': prompt},
                            {'inline_data': {'mime_type': 'image/jpeg', 'data': response.content}}
                        ]
                        # Verify content_parts before sending to the model
                        if not content_parts or not isinstance(content_parts, list):
                            raise ValueError("content_parts is not a valid list or is empty")
                        
                        #Generate response
                        generate_request = {
                            'contents': [{'parts': content_parts}],
                            'stream': True,
                            'safety_settings': [
                                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
                            ]
                        }

                        #call generate method
                        response = model.generate_content(**generate_request)
                        #call response resolve
                        response.resolve()
                        #final_response
                        final_response = response.text
                        #print(f"This is the response {final_response}")
                        logging.info(f"{final_response}")

                    except requests.exceptions.RequestException as e:
                        logging.error(f"Error fetching image from URL: {url} - {e}")
                        continue
                    except UnidentifiedImageError:
                        logging.error(f"Failed to identify and load image from URL: {url}")
                        continue
                    except Exception as e:
                        logging.error(f"An unexpected error occurred: {e}")
                        continue
                else:
                    model = self.gemini_api_pro()

                    try:
                        url_id = self.extract_video_id(url)
                        content_type = self.get_video_transcripts(url_id)
                        logging.info(f"This is URL_ID {url_id}")
                        #print(f"This is the content Type {content_type}")
                    except requests.exceptions.RequestException as e:
                        logging.error(f"Error fetching content from URL: {url} - {e}")
                        raise e
                    except Exception as e:
                        logging.error(f"An unexpected error occurred: {e}")
                        raise e

                for attempt in range(max_retries):
                        
                        try:
                            x = [prompt,content_type]
                            response = model.generate_content(x,stream=True)
                            logging.info(f"This is response object: {response}")
                            response.resolve()
                            final_response = response.text

                            logging.info(f"This is final response: {final_response}")

                            # Assuming you want to do something with final_response here
                            # self.insert_or_update_extracted_values(final_response, table_name, supplier_id, row, prompt)

                            # Exit retry loop if successful
                            break  
                        except requests.exceptions.Timeout:
                            logging.error(f"Timeout occurred on attempt {attempt + 1} for URL: {url}")
                            if attempt < max_retries - 1:
                                time.sleep(backoff_factor * (2 ** attempt))
                            else:
                                logging.error(f"Exceeded max retries for URL: {url}")
                                raise
                        except InternalServerError as e:
                            logging.error(f"Internal Server Error on attempt {attempt + 1} for URL: {url}")
                            if attempt < max_retries - 1:
                                time.sleep(backoff_factor * (2 ** attempt))
                            else:
                                logging.error(f"Exceeded max retries for URL: {url}")
                                raise e
                        except Exception as e:
                            logging.error(f"An unexpected error occurred on attempt {attempt + 1} for URL: {url}: {e}")
                            raise e

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            raise e
            
=======
        
        except Exception as e:
            logging.error(f"Failed to configure Gemini API: {e}")
            
            NerException(e,sys)
        

    def read_sql(self):
        pass

    def query(self):
        pass
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492

    def clean_data(self):
        pass

<<<<<<< HEAD
    def insert_or_update_extracted_values(self):
        pass
    
    def fetch_data_exitst_or_not(self):
        pass

    def initiate_data(self,table_name,supplier_id) -> pd.DataFrame:

        
        try:
            # Call gemini API function to get the GEMINI model
            self.gemini_api_vision_pro()
            self.gemini_api_pro()
=======
    def insert_data(self):
        pass

    def fetch_column_name(self):
        pass

    def initiate_data(self,table_name,supplier_id):

        try:
            # Call gemini API function to get the GEMINI model
            self.gemini_api_key()
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492

            # Initialize an empty list to store DataFrame outputs
            df_list = []

            # Define the SQL query with dynamic table name and supplier ID
            query = f"""
<<<<<<< HEAD
                    SELECT * FROM {self.db_name}.{table_name} where id = {supplier_id};
                    """
            print(query)

            # Read data from MSSQL and append it to the list
            df_data = self.read_data(query)
            df_list.append(df_data)
            #print(df_list)

            prompt = self.fetch_prompt(supplier_id)
        
            # Fetch prompt from prompt_table
            prompt = self.fetch_prompt(supplier_id)  # Example method to fetch prompt from prompt_table

            #save prompt with urls in another column
            df_data['prompt'] = prompt

            df_data.apply(lambda row: self.process_row(row, prompt, table_name),axis=1)

            print(df_data)
            #return df_data
            return df_data  # Return the modified DataFrame
            # Return the list of DataFrames
        except Exception as e:
            raise e

    def process_row(self, row, prompt, table_name):
        """
        Processes a single row of the DataFrame.
        """
        try:
            product_data = row.to_dict()
            
            for key, value in product_data.items():
                if isinstance(value, bytes):
                    product_data[key] = value.decode('utf-8', errors='ignore')  # Ignore errors during decoding

            supplier_id = row.get('id')  # Get supplierId from the row

            # Determine image URLs based on the table name
            urls = row.get('urls')

            # Ensure urls is a list
            if isinstance(urls, str):  # Single URL case
                urls = [urls]
            elif pd.isna(urls):  # NaN or missing value case
                urls = []
            elif not isinstance(urls, list):  # Ensure urls is a list
                urls = []

            if urls:
                self.query(urls, supplier_id, prompt, table_name, row)
                logging.info(f"Processed row")
            else:
                logging.warning(f"No valid URLs for row")

        except Exception as e:
            raise e

    
=======
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
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492
