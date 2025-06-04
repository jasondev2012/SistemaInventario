import pyodbc

class DataBase:
    def get_connection():
        return pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost\SQLEXPRESS;DATABASE=dbInventario;'
            'UID=user;PWD=123456'
        )
