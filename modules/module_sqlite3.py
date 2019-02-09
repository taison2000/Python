#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# Sebastian Raschka, 2014
# Creating a new SQLite database

import sqlite3

def add_column():
    # http://stackoverflow.com/questions/4253804/insert-new-column-into-table-in-sqlite
    # ALTER TABLE {tableName} ADD COLUMN newColumnName {type};
    # ALTER TABLE {tableName} RENAME TO TempOldTable;
    # CREATE TABLE {tableName} (name TEXT, COLNew {type} DEFAULT {defaultValue}, qty INTEGER, rate REAL);
    pass

def insert_column_in_between():
    ## Original table has columns : name, quantity, rate
    ## want to insert a coumun 'newColumnName' between 'name' and 'quantity'
    
    # rename table
    ALTER TABLE {tableName} RENAME TO tempTable;
    # create new table with column need to be inserted along with original columns
    CREATE TABLE {tableName} (name TEXT, newColumnName {type} DEFAULT {defaultValue}, quantity INTEGER, rate REAL);
    # copy data from original table to new table
    INSERT INTO {tableName} (name, quantity, rate) SELECT name, quantity, rate FROM tempTable;
    # then delete old table
    DROP TABLE tempTable;
    

    c.execute('CREATE TABLE {tableName} ({nameField} {fieldType} PRIMARY KEY)'\
        .format(tableName="table_cost", nameField="Sell_Price", fieldType='INTEGER'))
        
sqlite_file = 'acc2_log.sqlite'    # name of the sqlite database file
table_name1 = 'my_table_1'	# name of the table to be created
table_name2 = 'my_table_2'	# name of the table to be created
date_field = 'Date'     # Date name of the column
time_field = 'Time'     # Time name of the column
date_field_type = 'INTEGER'  # column data type
field_type = 'INTEGER'  # column data type

## Connecting to the database file
# A new database file will be created automatically the first time
# when try to connect to the database.
conn = sqlite3.connect( sqlite_file )
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name1, nf=date_field, ft=field_type))

# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_name2, nf=date_field, ft=field_type))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()


##-----------------------------------------------------------------------------
"""
Resource :
 - http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
 - https://github.com/rasbt/python_reference/blob/master/tutorials/sqlite3_howto/code/create_new_db.py
 - https://github.com/rasbt/python_reference/tree/master/tutorials/sqlite3_howto
"""

