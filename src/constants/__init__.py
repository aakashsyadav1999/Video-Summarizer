import os
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import time
from datetime import datetime

#Mssql parameter
PRODUCT_DB = "gemini"




TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

ARTIFACTS_DIR = os.path.join("artifacts")
LOGS_DIR = "logs"
LOGS_FILE_NAME = "SIDFC.log"

#Env

CONTAINER_NAME=os.getenv('ContainerName')
SERVER=os.getenv('MYSQL_HOST')
USER=os.getenv('MYSQL_USER')
PASSWORD=os.getenv('MYSQL_PASSWORD')
MODEL_NAME = "gemini-pro-vision"


#Gemini API 
API_KEY_GEMINI = os.getenv('API_KEY_GEMINI')