# Data-Representation-Big-Project
My project submission for the Data Representation module at GMIT 2020
John Dunne G00273895

## Contents of this repository

This repository contains:

* MySQL database containing a table of data. The commands used to create the database are contained in a file called initdb.sql in this repository.
* Python DAO file to connect to the MySQL database and retrieve data from the database.
* Python App server which should be run in a virtual environment.
* Static pages which server up the data to the user in a web browser and allow the user to perform CRUD operations on the data. 
* dbconfigtemplate.py is a file that should hold the log in credentials to be read by the Python DAO file to connect to the MySql database.
* requirements.txt contains the list of required packages that should be installed in a virtual environment in order for ths server to run.

## Virtual Environment 

This repository consists of a server which should be run in a virtual environment.

The command to  install a virtual environment on your machine for the first time are as follows:

1. python -m venv venv
2. .\venv\Scripts\activate.bat

To install the requires packages:

3. pip install flask
4. pip install mysql-connector-python

To run my server:

5. python server.py

To exit the virtual environment:

6. deactivate

## MySQL Database 

I have created a MySQL database called stockbullfinder which will contain details on stock bulls that are used in for breeding in the suckler beef breeding cattle system in Ireland. I have sourced the bulls details from the Irish Cattle Breeding Federation bull search - https://webapp.icbf.com/v2/app/bull-search. 

I have created a table called bulls in the database that contains some basic information about each bull. 

* The AI code of each bull which serves as the primary key. Every bull has a unique code.
* The name of each bull.
* The breed of each bull.
* The owner of each bull.

The commands that were used to create the database and table and insert data into the table are saved in the folder SQL in this repository in a file called initdb.sql

#### I have added below an image of the bulls table when the describe command is run in MySQL.

![describebulls](/images/describebulls.PNG)

#### I have added below an image of data contained in the bulls table:

![describebulls](/images/bulls.PNG)

I intend to add a second table to the database later.