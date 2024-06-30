import os
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
from src.entity.config_entity import Mssql
import mysql.connector
from src.logger import logging


load_dotenv()


class MssqlDB:
    def __init__(self, dbname):

        self.dbname = dbname

    def execute_one_query(self, query):
        try:
            with ThreadPoolExecutor() as executor:
                future = executor.submit(self._execute_query, query)
                data = future.result()
            return data
        except Exception as e:
            return str(e)
        
    def execute_one_query_1(self, query, params=None):
        try:
            with ThreadPoolExecutor() as executor:
                future = executor.submit(self._execute_query_1, query, params)
                data = future.result()
            return data
        except Exception as e:
            return str(e)
            
    def execute_one_query_2(self, query, params=None):
        try:
            with ThreadPoolExecutor() as executor:
                future = executor.submit(self._execute_query_2  , query, params)
                data = future.result()
            return data
        except Exception as e:
            return str(e)
    
    def execute_one_query_3(self, query, params=None):
        try:
            with ThreadPoolExecutor() as executor:
                future = executor.submit(self._execute_query_3  , query, params)
                data = future.result()
            return data
        except Exception as e:
            return str(e)

    def insert_query(self, query):
        try:
            with ThreadPoolExecutor() as executor:
                future = executor.submit(self._execute_insert, query)
                result = future.result()
            return result
        except Exception as e:
            return str(e)
        
    def insert_query_2(self, query, params):
        try:
            with ThreadPoolExecutor() as executor:
                future = executor.submit(self._execute_insert_2, query, params)
                result = future.result()
            return result
        except Exception as e:
            return str(e)
        
    def insert_query_3(self, query, params):
        try:
            with ThreadPoolExecutor() as executor:
                future = executor.submit(self._execute_insert_3, query, params)
                result = future.result()
            return result
        except Exception as e:
            return str(e)

    def insert_many_query(self, query, value):
        try:
            with ThreadPoolExecutor() as executor:
                future = executor.submit(self._execute_insert_many, query, value)
                result = future.result()
            return result
        except Exception as e:
            return str(e)
        
    def execute_insert_4(self, query, value):
        try:
            with ThreadPoolExecutor() as executor:
                future = executor.submit(self._execute_insert_4, query, value)
                result = future.result()
            return result
        except Exception as e:
            return str(e)

    def execute_many_query(self, query, value):
        try:
            with ThreadPoolExecutor() as executor:
                future = executor.submit(self._execute_many, query, value)
                data = future.result()
            return data
        except Exception as e:
            return str(e)
        

    def check_data_exists(self, query):
        try:
            with ThreadPoolExecutor() as executor:
                future = executor.submit(self._execute_check_data_exists, query)
                result = future.result()
            return result
        except Exception as e:
            return str(e)

    def _execute_query(self, query):
        data = []
        conn = None
        cursor = None
        try:
            # Connect to the MySQL database using environment variables for security
            conn = mysql.connector.connect(
                host=os.environ["MYSQL_HOST"],
                user=os.environ["MYSQL_USER"],
                password=os.environ["MYSQL_PASSWORD"],
                database=self.dbname
            )

            cursor = conn.cursor()
            cursor.execute(query)

            column_names = [desc[0] for desc in cursor.description]

            for row in cursor.fetchall():
                data.append(dict(zip(column_names, row)))

        except mysql.connector.Error as err:
            print("Error fetching data:", err)  # Log or handle the error appropriately

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return data
    def _execute_query_1(self, query, params=None):
        data = []
        conn = None
        cursor = None
        try:
            conn = pymssql.connect(server=os.environ["server"],
                                user=os.environ["user"],
                                password=os.environ["password"],
                                database=self.dbname)
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            for each_data in cursor:
                data.append(each_data)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return data
    
    def _execute_query_2(self, query, params=None):
        data = []
        conn = None
        cursor = None
        try:
            conn = pymssql.connect(server=os.environ["server"],
                                user=os.environ["user"],
                                password=os.environ["password"],
                                database=self.dbname)
            cursor = conn.cursor()
            cursor.execute(query, params)
            for each_data in cursor:
                data.append(each_data)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return data
    
    def _execute_insert(self, query):
        conn = None
        cursor = None
        try:
            conn = pymssql.connect(server=os.environ["server"],
                                   user=os.environ["user"],
                                   password=os.environ["password"],
                                   database=self.dbname)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return "INSERTION SUCCESSFUL"
    
    def _execute_insert_2(self, query, params):
        conn = None
        cursor = None
        try:
            conn = pymssql.connect(server=os.environ["server"],
                                   user=os.environ["user"],
                                   password=os.environ["password"],
                                   database=self.dbname)
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return "INSERTION SUCCESSFUL"

    def _execute_insert_3(self, query, values):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
        except Exception as e:
            self.connection.rollback()
            raise

    def _execute_insert_many(self, query, value):
        conn = None
        cursor = None
        try:
            conn = pymssql.connect(server=os.environ["server"],
                                   user=os.environ["user"],
                                   password=os.environ["password"],
                                   database=self.dbname)
            cursor = conn.cursor()
            cursor.executemany(query, value)
            conn.commit()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return "ALL DATA INSERTION SUCCESSFUL"
    

    def _execute_many(self, query, value):
        data = []
        conn = None
        cursor = None
        try:
            conn = pymssql.connect(server=os.environ["server"],
                                   user=os.environ["user"],
                                   password=os.environ["password"],
                                   database=self.dbname)
            cursor = conn.cursor()
            cursor.executemany(query, value)
            for each_data in cursor:
                data.append(each_data)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return data

    def _execute_check_data_exists(self, query):
        conn = None
        cursor = None
        try:
            conn = pymssql.connect(server=os.environ["server"],
                                   user=os.environ["user"],
                                   password=os.environ["password"],
                                   database=self.dbname)
            cursor = conn.cursor()
            cursor.execute(query)
            value_exists = cursor.fetchone() is not None
            return value_exists
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()