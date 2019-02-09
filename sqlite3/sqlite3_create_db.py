#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# Sebastian Raschka, 2014
# Creating a new SQLite database

import sqlite3

sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
table_name1 = 'my_table_1'	# name of the table to be created
table_name2 = 'my_table_2'	# name of the table to be created
new_field = 'my_1st_column' # name of the column
field_type = 'INTEGER'  # column data type

## Connecting to the database file
# A new database file will be created automatically the first time
# when try to connect to the database.
conn = sqlite3.connect( sqlite_file )
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name1, nf=new_field, ft=field_type))

# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_name2, nf=new_field, ft=field_type))

c.execute("INSERT INTO {table} ({field}) VALUES ('1ST Entry')".format(table=table_name1, field=new_field))

# Committing changes and closing the connection to the database file
conn.commit()

sel = c.execute("SELECT * FROM {table}".format(table=table_name1))
# sel.arraysize sel.close sel.connection sel.description sel.execute sel.executemany sel.executescript 
# sel.fetchall sel.fetchmany sel.fetchone sel.lastrowid sel.row_factory sel.rowcount sel.setinputsize
# sel.setoutputsize
data = sel.fetchall()

print(data)

#conn.close()


##-----------------------------------------------------------------------------
"""
Resource :
 - http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
 - https://github.com/rasbt/python_reference/blob/master/tutorials/sqlite3_howto/code/create_new_db.py
"""

