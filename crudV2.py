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
        # Create connection with Data Base
        self.con = sqlite3.connect(database)
        self.cursor = self.con.cursor()  # Create cursor

    def insert(self, obj):
        """ Insert into table
        """
        query = 'INSERT INTO currency VALUES ("{}", "{}", "{}")'.format(
            obj.id, obj.name, obj.symbol)
        self.cursor.execute(query)
        self.con.commit()

    def get(self, id):
        """ find object for code and return object
        """
        query = 'SELECT * FROM currency where id = {}'.format(id)
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        if not data:
            raise CurrencyDoesNotExists(
                'No existe moneda con el código {} '.format(id))
        return Currency(id=data[0], name=data[1], symbol=data[2])

    def filter(self, **kwargs):
        """ filter return list
        """
        id = kwargs.get('id')
        name = kwargs.get('name')
        symbol = kwargs.get('symbol')

        condition = ' WHERE '
        add_and = False
        add_condition = False

        if id:
            condition += 'id={} '.format(id)
            add_and = True
            add_condition = True
        if name:
            if add_and:
                condition += 'AND'
            condition += 'name={} '.format(name)
            add_and = True
            add_condition = True
        if symbol:
            if add_and:
                condition += 'AND'
            condition += 'symbol={} '.format(symbol)
            add_condition = True

        query = 'SELECT * FROM currency'

        if add_condition:
            query += condition

        self.cursor.execute(query)
        result = self.cursor.fetchall()

        currencies = []

        for data in result:
            currency = Currency(id=data[0], name=data[1], symbol=data[2])
            currencies.append[currency]

        return currencies


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
""" valueColombian = Currency(id='COL', name='Colombia', symbol='$')
valueUSA = Currency(id='USA', name='United States', symbol='US$')
valueVenezuela = Currency(id='VEN', name='Venezuela', symbol='BsF') """

""" Currency.objects.insert(valueColombian)
Currency.objects.insert(valueUSA)
Currency.objects.insert(valueVenezuela) """

print(Currency.objects.get(id='COL'))