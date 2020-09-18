import mysql.connector

class MyDataBase():
    '''For init and return target statistics'''
    
    def __init__(self,host,user,password,database):
        '''initialization'''
        self.db = mysql.connector.connect(host=host,user=user,password=password,database=database)

    def data(self):
        '''return user data'''
        my_cursor = self.db.cursor()
        my_cursor.execute("SELECT * FROM users")
        return my_cursor.fetchall()
