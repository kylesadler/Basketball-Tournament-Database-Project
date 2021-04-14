import mysql.connector

class SQLDatabase:
    def __init__(self, hostname, user_name, mysql_pw, database_name):
        """ opens database. defines conn and cursor global objects """
        self.connection = mysql.connector.connect(
            host=hostname, 
            user=user_name,  
            password=mysql_pw, 
            database=database_name 
        ) 
        self.cursor = self.connection.cursor() 

    # select and display query
    def select(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        headers = [ x[0] for x in self.cursor.description ]
        return headers, rows

    def insert(self, table, values):
        query ="INSERT into " + table + " values (" + values + ")" +';'
        self.cursor.execute(query)
        self.connection.commit()

    def update(self, query): # use this function for delete and update
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        try:
            self.cursor.close()
            self.connection.close()
        except (ImportError, ReferenceError): # mysql errors that we don't care about
            pass

    def __del__(self):
        self.close()