import sqlite3

DB_PATH = 'DataBaseCRUD.db'


class CurrentManager(object):
    """ Class manager. Insert, update, delete, update into BD
    """
    def __init__(self, database=None):
        """ Initialize Data Base
        """
        if not database:
            database = ':memory'
        self.con = sqlite3.connect(database) #Create connection with Data Base
        self.cursor = self.con.cursor()  #Create cursor

    def insert(self, obj):
        """ Insert into table
        """
        query = 'INSERT INTO currency VALUES ("{}", "{}", "{}")'.format(obj.id, obj.name, obj.symbol)
        self.cursor.execute(query)
        self.con.commit()


class Currency(object):
    """ Class model
    """
    objects = CurrentManager(DB_PATH)

    def __init__(self, id, name, symbol):
        """
        """
        self.id = id
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        """
        """
        return u"{}".format(self.name)

# Create instances
valueColombian = Currency(id='COL', name='Colombia', symbol='$')
valueUSA = Currency(id='USA', name='United States', symbol='US$')
valueVenezuela = Currency(id='VEN', name='Venezuela', symbol='BsF')

Currency.objects.insert(valueColombian)
Currency.objects.insert(valueUSA)
Currency.objects.insert(valueVenezuela)
