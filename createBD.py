import sqlite3
import os.path as path


def crearDataBase():
    if (path.exists('DataBaseCRUD.db')):
        print('Data Base Found....')
        return

    # Make a connection with data base
    conn = sqlite3.connect('DataBaseCRUD.db')
    print("Connection is established.....")

    # Make a cursor with object
    cursorObj = conn.cursor()

    # Create a table
    cursorObj.execute('CREATE TABLE currency (ID text, NAME text, SYMBOL text)')
    print("Table created success!!!!! ")

    # Insert items to table currency
    """    cursorObj.execute('INSERT INTO currency VALUES(1, "Colombia", "$")')
    cursorObj.execute('INSERT INTO currency VALUES(2, "Venezuela", "BsF")')
    cursorObj.execute('INSERT INTO currency VALUES(3, "Dolar", "USD")') """

    # Query for all data of table myDataBase
    #query = 'SELECT * FROM currency'

    # search result
    #data = cursorObj.execute(query).fetchall()
    #print(data)

    # Save changes
    #conn.commit()

crearDataBase()