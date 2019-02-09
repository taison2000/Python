#!/Python34/python
#!/usr/bin/python


import sqlite3


# Connecting to the database file
## it will create the database if not exist
conn = sqlite3.connect( 'mytest.db' ) 

# A cursor is what to use to move around the database, execute SQL statement, and get data.
cursor = conn.cursor()

# SQL statement
# sql = """CREATE TABLE students (
sql = """CREATE TABLE IF NOT EXISTS students (
  name text,
  username text,
  id int
)"""

# execute the SQL statement
cursor.execute( sql )


# Committing changes to the database file
conn.commit() ## Not sure if this necessary ??

# Closing the connection to the database file
cursor.close()


##-----------------------------------------------------------------------------
"""
Resource :
 - http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
 - https://github.com/rasbt/python_reference/blob/master/tutorials/sqlite3_howto/code/create_new_db.py
"""

