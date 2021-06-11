import csv
import os
import pyodbc
from datetime import datetime

conn1 = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-D9AJQ7F\SQLEXPRESS;'
                      'Database=LOCAL;'
                      'Trusted_Connection=yes;')

conn2 = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-D9AJQ7F\SQLEXPRESS;'
                      'Database=LOCAL;'
                      'Trusted_Connection=yes;')

cursorwrite = conn2.cursor()
cursorpull = conn1.cursor()

cursorpull.execute("select * from dbo.dim_brands")
cursorwrite.execute("truncate table python.dim_brands")

for row in cursorpull:
    cursorwrite.execute("insert python.dim_brands (brandid, updated_dt) values(?, getdate())",row[0])
cursorwrite.commit()
