from src.constants import *
from dataclasses import dataclass

@dataclass
class Multithreading:

    def __init__ (self):
        
        self.cpu_count:int = CPU_COUNT

        self.multi_process:int = MULTI_PROCESS

        self.max_workers:int = MAX_WORKERS

        self.delay:int = DELAY

@dataclass
class Mssql:

    def __init__ (self):

        self.mssql_product:str = GEMINI_DATABASE


@dataclass
class Env:

    def __init__ (self):

        self.local_host:str = HOST

        self.user:str = USER

        self.password:str = PASSWORD

        self.gemini_api:str = API_KEY_GEMINI

        self.model_name_vision_pro:str = MODEL_VISION_PRO

        self.model_name_pro:str = MODEL_PRO


@dataclass
class FetchingUrl:

    def __init__ (self):

        self.retry_connect:int = RETRY_CONNECT

        self.back_of_factor:int = BACK_OFF_FACTOR

        self.max_retries:int = MAX_RETRIES