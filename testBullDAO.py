# import the new instance of the bookDao class from the bookDAO file
from BullDAO import bullDao

bull1 = {
    'code': "test",
    'name': "update",
    'breed' : 'update',
    'owner' : 'update'
}

# create a new bull in the bulls database table
returnValue = bullDao.create(bull1)
print(returnValue)

# get all bulls in the database 
returnValue = bullDao.getAll()
print(returnValue)

# find by Id
returnValue = bullDao.findById(bull1['code'])
print(returnValue)

# update
returnValue = bullDao.update(bull1)
print(returnValue)

# find by Id
returnValue = bullDao.findById(bull1['code'])
print(returnValue)

# delete
returnValue = bullDao.delete(bull1['code'])
print(returnValue)