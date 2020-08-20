'''Access kaggle database for medcab project'''

import pandas as pd
import os
import sqlite3

# Creating csv file
strains = pd.read_csv(r'C:\Users\kushnap\Desktop\Data-Science\cannabis.csv')

# Creating connection to sqlite and converting csv file to sql
connection = sqlite3.connect('strains')
strains.to_sql('strains', con=connection, if_exists='replace')
print("CONNECTION: ", connection)

# Creating a cursor object for strains
cursor = connection.cursor()
print("CURSOR: ", cursor)

# Querying to test that connection works
query = "SELECT count(*) as TotalRows FROM strains;"
result = cursor.execute(query).fetchall()
print("Total Rows RESULT: ", result)

query2 = "SELECT count(distinct strain) as total_num_strains FROM strains;"
result2 = cursor.execute(query2).fetchall()
print("Distinct Strains RESULT", result2)

query3 = "SELECT count(*) FROM strains WHERE strain == 'Green-Crack';"
result3 = cursor.execute(query3).fetchall()
print(result3)
