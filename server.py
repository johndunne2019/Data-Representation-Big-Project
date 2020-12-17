# Data Representation big project
# John Dunne G00273895
# application server to be run in virtual environment 

# import flask and dependencies 
from flask import Flask, jsonify, request, abort, session
# import a new instance of the bullDAO class from the BullDAO file
from bullDAO import bullDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')
app.secret_key = 'MyS3cr£tk€y'
#app = Flask(__name__)

#curl "http://127.0.0.1:5000"
@app.route("/")
def index():
    count=0
    count+=1

    if not 'counter' in session:
        session['counter'] =0
        print("new session")

    sessionCount=session['counter']
    sessionCount+=1
    session['counter']=sessionCount

    

    pageContent="<h1>counts</h1>" +\
        "session Count ="+str(sessionCount) +\
        "<br/>this Count ="+str(count)
    
    return pageContent

# function to clear the session counter
@app.route('/clear')
def clear():
    #session.clear()
    session.pop('counter',None)   

    return "done" 

# get all
#curl "http://127.0.0.1:5000/bulls"
@app.route('/bulls')
def getAll():
    #print("in getall")
    results = bullDAO.getAll()
    return jsonify(results)

# find by id
#curl "http://127.0.0.1:5000/bulls/2"
@app.route('/bulls/<int:id>')
def findById(id):
    foundBull = bullDAO.findByID(id)

    return jsonify(foundBull)

# create a new bull should be id 8
#curl  -i -H "Content-Type:application/json" -X POST -d "{\"code\":\"hello\",\"name\":\"someone\",\"breed\":\"someone\",\"owner\":\"someone\"}" http://127.0.0.1:5000/bulls
@app.route('/bulls', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    bulls = {
        "code": request.json['code'],
        "name": request.json['name'],
        "breed": request.json['breed'],
        "owner": request.json['owner'],
    }
    values =(bulls['code'],bulls['name'],bulls['breed'], bulls['owner'])
    newId = bullDAO.create(values)
    bulls['id'] = newId
    return jsonify(bulls)

# update bull 8 added to database
#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"code\":\"update\",\"name\":\"update\",\"breed\":\"update\",\"owner\":\"update\"}" http://127.0.0.1:5000/bulls/8
@app.route('/bulls/<int:id>', methods=['PUT'])
def update(id):
    foundBull = bullDAO.findByID(id)
    # error handling if no bull found by the specified id
    if not foundBull:
        abort(404)
    # if not a json request 
    if not request.json:
        abort(400)
    reqJson = request.json
   # if 'Price' in reqJson and type(reqJson['Price']) is not int:
        #abort(400)

    if 'code' in reqJson:
        foundBull['code'] = reqJson['code']
    if 'name' in reqJson:
        foundBull['name'] = reqJson['name']
    if 'breed' in reqJson:
        foundBull['breed'] = reqJson['breed']
    if 'owner' in reqJson:
        foundBull['owner'] = reqJson['owner']
    values = (foundBull['code'],foundBull['name'],foundBull['breed'],foundBull['owner'], foundBull['id'])
    bullDAO.update(values)
    return jsonify(foundBull)
    
# delete the newly created bull 8 
# CURL -X DELETE http://127.0.0.1:5000/bulls/8
# should add some error handling for a case where a bull is not in the database 
@app.route('/bulls/<int:id>' , methods=['DELETE'])
def delete(id):
    bullDAO.delete(id)
    return jsonify({"done":True})

# run the app when script is run from command line
if __name__ == '__main__' :
    app.run(debug= True)