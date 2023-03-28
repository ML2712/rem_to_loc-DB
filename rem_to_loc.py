import pyodbc
import time
import urllib.request
from urllib.error import URLError


# Check internet connection
def is_internet_available():
    try:
        urllib.request.urlopen('https://www.google.com/', timeout=1)
        return True
    except URLError as err:
        return False


# check
def switch_database():
    while True:
        if is_internet_available():
            print('Internet connection available, switching to online database...')
            time.sleep(50)

        else:
            print('Internet connection not available, switching to offline database...')
            time.sleep(50)


switch_database()
