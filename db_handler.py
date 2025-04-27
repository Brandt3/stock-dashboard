import sqlite3
import os


def createDB():
    ''' Checks if files exist and removes it to have a fresh DB file
        If you want to keep the data and have it add up then remove these line'''
    # if os.path.exists("FinalProject.db"):
    #         os.remove('FinalProject.db')
    # Connect to SQLite database
    conn = sqlite3.connect('FinalProject.db')

    # Creating a cursor/object it perform query/creating...
    cursor = conn.cursor()

    # Create two tables
    cursor.executescript("""     
        CREATE TABLE IF NOT EXISTS Companies (
            Ticker_Symbol TEXT PRIMARY KEY,
            Last_Refreshed TEXT NOT NULL,
            Output_Size TEXT NOT NULL,
            Time_Zone TEXT NOT NULL
        );
                        
        CREATE TABLE IF NOT EXISTS Stocks (
            Ticker_Symbol TEXT,
            Date TEXT,
            Open_Price REAL NOT NULL,
            High_Price REAL NOT NULL,
            Low_Price REAL NOT NULL,
            Close_Price REAL NOT NULL,
            Volume INTEGER NOT NULL,
            PRIMARY KEY (Ticker_Symbol, Date),
            FOREIGN KEY (Ticker_Symbol) REFERENCES Companies (Ticker_Symbol)
        );
        
    """)
    conn.commit()

def insertStock(stock_data, company_data):
    # Connect to SQLite database
    conn = sqlite3.connect('FinalProject.db')
    # Creating a cursor/object it perform query/creating...
    cursor = conn.cursor()

    cursor.executescript("""     
    CREATE TABLE IF NOT EXISTS Companies (
        Ticker_Symbol TEXT PRIMARY KEY,
        Last_Refreshed TEXT NOT NULL,
        Output_Size TEXT NOT NULL,
        Time_Zone TEXT NOT NULL
    );
                     
    CREATE TABLE IF NOT EXISTS Stocks (
        Ticker_Symbol TEXT,
        Date TEXT,
        Open_Price REAL NOT NULL,
        High_Price REAL NOT NULL,
        Low_Price REAL NOT NULL,
        Close_Price REAL NOT NULL,
        Volume INTEGER NOT NULL,
        PRIMARY KEY (Ticker_Symbol, Date),
        FOREIGN KEY (Ticker_Symbol) REFERENCES Companies (Ticker_Symbol)
    );
    
    """)
    conn.commit()

    stock_insert = []
    # This will add a tuple of data for each object into a list so then I can just pass one list of tuples instead of 100 execute lines
    for item in stock_data:
        stock_insert.append((
            item.symbol, item.date, item.open, item.high, item.low, item.close, item.volume
        ))

    cursor.executemany("INSERT OR IGNORE INTO Stocks VALUES (?, ?, ?, ?, ?, ?, ?)", stock_insert)
    conn.commit()

    # This is fine because there is only one item in company_data so it will only run once
    for item in company_data:
        cursor.execute("INSERT OR IGNORE INTO Companies VALUES (?, ?, ?, ?)", (item.symbol, item.lastRefresh, item.outputSize, item.timeZone))
        conn.commit()
    conn.close

