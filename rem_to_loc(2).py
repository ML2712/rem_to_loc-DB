import pyodbc
import urllib.request
import time
from urllib.error import URLError


# Set up connection strings for the online and offline databases
online_conn_string = 'DRIVER={SQL Server};SERVER=online_server;DATABASE=online_db;UID=username;PWD=password'
offline_conn_string = 'DRIVER={SQL Server};SERVER=offline_server;DATABASE=offline_db;UID=username;PWD=password'


# Check internet connection
def is_internet_available():
    try:
        urllib.request.urlopen('https://www.google.com/', timeout=1)
        return True
    except URLError as err:
        return False


# Transfer data from offline to online database
def transfer_data():
    offline_conn = pyodbc.connect(offline_conn_string)
    online_conn = pyodbc.connect(online_conn_string)
    cursor = offline_conn.cursor()

    # Retrieve data from offline database
    cursor.execute('SELECT * FROM table_name')
    data = cursor.fetchall()

    # Insert data into online database
    online_cursor = online_conn.cursor()
    for row in data:
        online_cursor.execute('INSERT INTO table_name VALUES (?, ?, ?)', row)

    online_conn.commit()
    online_conn.close()
    offline_conn.close()


# Switch between online and offline databases based on internet availability
def switch_database():
    while True:
        if is_internet_available():
            print('Internet connection available, switching to online database...')
            conn = pyodbc.connect(online_conn_string)
            print('Connected to online database.')

            # Transfer data from offline to online database
            transfer_data()

            time.sleep(60)
        else:
            print('Internet connection not available, switching to offline database...')
            conn = pyodbc.connect(offline_conn_string)
            print('Connected to offline database.')
            time.sleep(60)


# Start the script
switch_database()
