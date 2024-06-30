from src.constants import *
from dataclasses import dataclass

@dataclass
<<<<<<< HEAD
class Multithreading:

    def __init__ (self):
        
        self.cpu_count:int = CPU_COUNT

        self.multi_process:int = MULTI_PROCESS

        self.max_workers:int = MAX_WORKERS

        self.delay:int = DELAY

@dataclass
=======
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492
class Mssql:

    def __init__ (self):

<<<<<<< HEAD
        self.mssql_product:str = GEMINI_DATABASE

=======
        self.mssql_product:str = PRODUCT_DB
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492

@dataclass
class Env:

    def __init__ (self):

<<<<<<< HEAD
        self.local_host:str = HOST
=======
        self.container_name:str = CONTAINER_NAME

        self.server:str = SERVER
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492

        self.user:str = USER

        self.password:str = PASSWORD

        self.gemini_api:str = API_KEY_GEMINI

<<<<<<< HEAD
        self.model_name_vision_pro:str = MODEL_VISION_PRO

        self.model_name_pro:str = MODEL_PRO


@dataclass
class FetchingUrl:

    def __init__ (self):

        self.retry_connect:int = RETRY_CONNECT

        self.back_of_factor:int = BACK_OFF_FACTOR

        self.max_retries:int = MAX_RETRIES
=======
        self.model_name:str = MODEL_NAME
>>>>>>> e687f0fa7b4d2b77dead3e19683877fe8cbbe492
