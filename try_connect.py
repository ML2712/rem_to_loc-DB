import pyodbc
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MININT-BDIHI4H;'
                      'Database=NORTHWND;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT TOP(5) CompanyId FROM dbo.Customers')

for i in cursor:
    print(i)

cursor.close()
conn.close()
