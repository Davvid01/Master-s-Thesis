import urllib
from sqlalchemy import create_engine, inspect

def get_connection_string():
    """
    Zwraca surowy connection string (do SQL Servera z Trusted_Connection).
    """
    return (
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=VICTUS\\SQLEXPRESS;"
        "Database=Baza_API;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

def create_db_engine():
    """
    Tworzy i zwraca SQLAlchemy Engine na podstawie ODBC connection string.
    """
    conn_str = urllib.parse.quote_plus(get_connection_string())
    return create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str}")

def print_table_names(engine):
    """
    Wypisuje listę dostępnych tabel w bazie danych.
    """
    inspector = inspect(engine)
    print("Dostępne tabele w bazie:", inspector.get_table_names())
