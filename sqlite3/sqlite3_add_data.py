#!/Python34/python
#!/usr/bin/python

import sqlite3

# Connecting to the database file
## it will create the database if not exist
conn = sqlite3.connect( 'mytest.db' ) 

# A cursor is what to use to move around the database, execute SQL statement, and get data.
cursor = conn.cursor()

print( "Let's input some students!" )

while True:
    name = input( "Student's name: ")
    username = input( "Student's username: " )
    id_num = input( "Student's id number: " )
    sql = """INSERT INTO students
    (name, username, id)
    VALUES
    (:st_name, :st_username, :id_num)
    """
    cursor.execute( sql, {'st_name':name, 'st_username':username, 'id_num':id_num} )

    # Committing changes to the database file
    conn.commit() ## Not sure if this necessary ??

    cont = input( "Another student? ")
    if cont[0].lower() == 'n': break

# Closing the connection to the database file
cursor.close()


##-----------------------------------------------------------------------------
## NOTES:
"""
CREATE TABLE
    cursor.execute("CREATE TABLE IF NOT EXISTS students (name, username, id);")
"""

##-----------------------------------------------------------------------------
"""
Resource :
 - http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
 - https://github.com/rasbt/python_reference/blob/master/tutorials/sqlite3_howto/code/create_new_db.py
"""

