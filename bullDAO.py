# import the mysql connector module
import mysql.connector
# import the dbconfig.py file which contains my credentials to log into mysql
import dbconfig as cfg

# bull class defined
class BullDAO:
    db=""

    # function to connect to the database, connection pooling added
    def initConnectToDB(self):
        db = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['user'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database'],
            pool_name='my_connection_pool',
            pool_size=10
        )
        return db
        # testing
        #print("connection made")

    # acquire a connection from the connection pool and close when finished 
    def getConnection(self):
        db = mysql.connector.connect(
            pool_name='my_connection_pool'
        )
        return db

    # initial connection to the database when a new instance of the class is created
    def __init__(self): 
        db = self.initConnectToDB()
        db.close()
            
    # function to create new bulls in the database table
    def create(self, values):
        db = self.getConnection()
        cursor = db.cursor()
        sql="insert into bulls (code, name, breed, owner) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)

        db.commit()
        lastRowId=cursor.lastrowid
        db.close()
        return lastRowId

    # function to retrieve all bulls from the bull table in the database
    def getAll(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql="select * from bulls"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        colnames=['id','code','name', "breed", "owner"]
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result, colnames))
        db.close()
        return returnArray

        # function to retrieve all bulls from the bull table in the database
    def getAllDetails(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql="select * from bulldetails"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        colnames=['code','sire','dam', 'calving', 'id']
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result, colnames))
        db.close()
        return returnArray

    # function to find specific bull by id
    def findByID(self, id):
        db = self.getConnection()
        cursor = db.cursor()
        sql="select * from bulls where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        bull=self.convertToDictionary(result)
        db.close()
        return bull

    # function to update existing bulls in the db
    def update(self, values):
        db = self.getConnection()
        cursor = db.cursor()
        sql="update bulls set code= %s,name=%s, breed=%s, owner=%s  where id = %s"
        cursor.execute(sql, values)
        db.commit()
        db.close()

    # function to delete bulls from the db
    def delete(self, id):
        db = self.getConnection()
        cursor = db.cursor()
        sql="delete from bulls where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        db.commit()
        db.close()
        #print("delete done")

    # function that converts the data from the database to JSON
    # this function is called within the find by id and get all functions to convert the data retrieved from the db
    def convertToDictionary(self, result, colnames):
       # colnames=['id','code','name', "breed", "owner"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
# new instance of the bull DAO class called 
bullDAO = BullDAO()
