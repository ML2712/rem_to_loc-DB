import pyodbc
from urllib.error import URLError
import urllib.request
import time


# Check internet connection
def is_internet_available():
    try:
        urllib.request.urlopen('https://www.google.com/', timeout=1)
        return True
    except URLError as err:
        return False


# Switch between online and offline databases based on internet availability
def switch_database():
    while True:
        if is_internet_available():
            print('Internet connection available, switching to online database...')
            print('Connected to online database.')
            # time.sleep(60)
            break

        else:
            print('Internet connection not available, switching to offline database...')

            # setup connection
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=MININT-BDIHI4H;'
                                  'Database=NORTHWND;'
                                  'Trusted_Connection=yes;')

            cursor = conn.cursor()

            # fetching queries
            cursor.execute('SELECT top(5) * FROM dbo.Customers')
            for i in cursor:
                print(i)
            print('\n')

            print('Connected to offline database.')
            time.sleep(60)
            cursor.close()
            conn.close()


# Start the script
switch_database()
