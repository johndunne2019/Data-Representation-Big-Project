# Adapted from Week 10 lectures on walkthrough of project type A

# import the mysql connector to connect to database
import mysql.connector 

# create a class containing the functions to perform CRUD operations
class BullDAO:
    # db variable to store the database connection
    db  = ""
    # function that initialises the  connection to db
    def __init__(self):
        # should be read from a configuration file in production environment 
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'stockbullfinder'
        )
        print("connection made")

    # function to create data in the database table
    # function takes in book which is a a JSON object
    def create(self, bulls):
        cursor = self.db.cursor()
        # if using an auto increment id this code will be different, look at student files
        sql = "insert into bulls (code, name, breed, owner) values (%s, %s, %s, %s)"
        values = [
                bulls['code'],
                bulls['name'],
                bulls['breed'],
                bulls['owner']
                ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    # function to return all bulls from the database table
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from bulls'
        cursor.execute(sql)
        # fetch all returns the data in tuples 
        results = cursor.fetchall()
        returnArray = []
        # output printed as a tuple
        #print(results)
        # we need to return as dict objects that can be converted to JSON objects
        # convertToDict function used to do this
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        # array of dict objects should be returned
        return returnArray

    # function to return just one bull from the database
    def findById(self, code):
        cursor = self.db.cursor()
        sql="select * from bulls where code = %s"
        values = [code]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        # return to dict object
        return self.convertToDict(result)

    # function to update data in the bulls table
    def update(self, bulls):
        cursor = self.db.cursor()
        sql = "update bulls set name = %s, breed = %s, owner = %s where code = %s"
        # values in array below must be in same order as sql command above
        values = [
                bulls['name'],
                bulls['breed'],
                bulls['owner'],
                bulls['code']
                ]
        cursor.execute(sql, values)
        self.db.commit()
        return bulls

    # function to delete from database table
    def delete(self, code):
        cursor = self.db.cursor()
        sql="delete from bulls where code = %s"
        values = [code]
        cursor.execute(sql, values)
      
        return {}

    # function to convert tuple to dict for getAll, meaning the output can be sent straight to html file later on
    def convertToDict(self,result):
        # columns names should be in same order as they appear in database table 
        colnames = ['code', 'name', 'breed', 'owner']
        bull = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                bull[colName] = value 
        return bull


# make a new instance of the Book DAO class to be imported to the test BookDAO file
bullDao = BullDAO()