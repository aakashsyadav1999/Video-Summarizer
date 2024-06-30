import os 
import datetime
from dotenv import load_dotenv, find_dotenv
import time
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import time
from datetime import datetime

#Mssql parameter
PRODUCT_DB = "gemini"





#Name of log-file
LOGS_DIR = "logs"
LOGS_FILE_NAME = "SIDFC.log"

#Timestamp
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

<<<<<<< HEAD

# Load environment variables
load_dotenv(find_dotenv())


#database
GEMINI_DATABASE = 'gemini'


#Mutithreading prameters
CPU_COUNT = 20
MULTI_PROCESS = True
MAX_WORKERS = 8
DELAY = 90


#databse credentials
HOST = os.getenv('LOCAL_HOST')
USER=os.getenv('USER')
PASSWORD=os.getenv('PASSWORD')
MODEL_VISION_PRO = "gemini-pro-vision"
MODEL_PRO = "gemini-pro"


#Gemini API 
API_KEY_GEMINI = os.getenv('API_KEY_GEMINI')



#Fetching urls
RETRY_CONNECT = 3
BACK_OFF_FACTOR = 0.5
MAX_RETRIES = 3

#TIME
TIME_SLEEP = 2
=======
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
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492
