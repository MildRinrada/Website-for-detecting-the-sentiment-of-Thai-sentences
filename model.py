# Import libraries
import mysql.connector
from decimal import Decimal

# ทำโมเดล+เขียนคำสั่ง SQL
class DataModel:
    def __init__(self, input_id, input):
        self.input_id = input_id
        self.input = input

    @staticmethod
    def connector():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ppgdmild",
            database="emotionthaidb"
        )
        return connection

    # insertแถวลงในDatabase
    def insert(self, result):
        # เชื่อมต่อฐานข้อมูล
        connection = DataModel.connector()
        cursor = connection.cursor()
        query = "INSERT INTO emotionthaitb (input) VALUES (%s)"
        try: 
            values = (self.input, result)
            cursor.execute(query, values)
            connection.commit()
            return cursor.lastrowid
        except Exception as e: #กรณีที่ insert แล้วเกิด error
            print(f"Error: {e}")
            return None