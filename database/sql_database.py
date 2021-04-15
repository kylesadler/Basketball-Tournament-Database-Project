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

    def generate_unique_id(self, table):
        _, ids = self.select(f'SELECT ID FROM {table};')
        return max([x[0] for x in ids]) + 1





# import sys
# import traceback
# import logging
# import python_db


# mysql_username = 'MYUSERNAME' # please change to your username
# mysql_password= 'MYMYSQLPASSWORD'  # please change to your MySQL password

# try:
#     python_db.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
#     res =python_db.executeSelect('SELECT * FROM ITEM;')
#     res=res.split('\n')# split the header and data for printing
#     print("<br/>"+ "Table ITEM before:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
#     for i in range(len(res)-2):
#         print(res[i+2]+"<br/>")
#     # insert into item tables by getting the values passed from PHP
#     id= '17' # ID is unique, it needs to be changed for every insert
#     name = sys.argv[1]
#     price_per_lb = sys.argv[2]
#     roasting = sys.argv[3]
#     val = id + ",'" + name + "','" + price_per_lb + "','" + roasting + "'"
#     python_db.insert("ITEM",val)
#     res = python_db.executeSelect('SELECT * FROM ITEM;')
#     res=res.split('\n')# split the header and data for printing
#     print("<br/>" + "<br/>")
#     print("<br/>"+ "Table ITEM after:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
#     for i in range(len(res)-2):
#         print(res[i+2]+"<br/>")
#     python_db.close() # close db    
# except Exception as e:
#         logging.error(traceback.format_exc())