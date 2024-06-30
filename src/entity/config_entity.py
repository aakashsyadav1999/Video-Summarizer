from src.constants import *
from dataclasses import dataclass

@dataclass
class Mssql:

    def __init__ (self):

        self.mssql_product:str = PRODUCT_DB

@dataclass
class Env:

    def __init__ (self):

        self.container_name:str = CONTAINER_NAME

        self.server:str = SERVER

        self.user:str = USER

        self.password:str = PASSWORD

        self.gemini_api:str = API_KEY_GEMINI

        self.model_name:str = MODEL_NAME