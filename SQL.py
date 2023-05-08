import sqlite3
import pandas as pd

# David White
# 2023/05/08
# CIS-2532
# Instructor: Mohammad Morovati
# Assignment: Execise 17.2
# Description:
# When you use a sqlite3 Cursor's execute method to prerform a query, 
# the query's results are stored in the Cursor object. The Cursor attribute
# description contains metadat about the results stored as a tuple of
# tuples Each nested tuple's first value is a column name in the query
# results. Cursor method fetchall lreturns the query result's dat as a
# list of tuples. Investigate the description attribute and fetchall
# method. Open the books database and use Cursor method execute to select 
# all the data in the titles table then use description and fetchall to 
# display the data in tabular format.

# load db
db = sqlite3.connect('books.db')

# create cursor
cursor = db.cursor()

# select all data from titles table
cursor = cursor.execute('SELECT * FROM titles')

#cursor.fetchall()

# list to hold columns
cols = []

# get columns
for i in cursor.description:
    cols.append(i[0])

df = pd.DataFrame(data=cursor, columns=cols)
print(df)
