# Data-Representation-Big-Project
My project submission for the Data Representation module at GMIT 2020
John Dunne G00273895

My project is based on retrieving data from a MySQL database called bullfinder. Within this database there are two tables of data which are linked by foreign key reference, further details later in this Readme file.

## Python Anywhere

This project is hosted on Python Anywhere at the below links:

http://johndunne1.pythonanywhere.com/

#### Web Pages:

Login : http://johndunne1.pythonanywhere.com/Login.html

BullViewer: http://johndunne1.pythonanywhere.com/BullViewer.html

Bull Details: http://johndunne1.pythonanywhere.com/BullDetails.html

#### Data retrieved from the MySQL database:

http://johndunne1.pythonanywhere.com/bulls

http://johndunne1.pythonanywhere.com/bulldetails

## Contents of this repository

This repository contains:

* The commands used to create the database and tables in MySQL are contained in a file called initdb.sql in this repository.
* Python DAO file to connect to the MySQL database and retrieve data from the database.
* Python App server which should be run in a virtual environment.
* Static pages which serve up the data to the user in a web browser and allow the user to perform CRUD operations on the data. 
    * Login.html which allows the user to enter log in credentials. I only have basic handling of logging in and any credentials entered in the correct format will bring the user to the main page which is BullViewer.html
    * BullViewer.html - the main page which contains the data retrieved from the bulls table in the bullfinder database. The user can perform CRUD operations on the data through the BullViewer.html page. 
    * BullDetails.html - A second webpage allowing the user to view the contents of the second table of data bull details. The user cannot perform CRUD operations on this data. 
* dbconfigtemplate.py is a file that should hold the log in credentials to be read by the Python DAO file to connect to the MySql database.
* requirements.txt contains the list of required packages that should be installed in a virtual environment in order for this server to run.
* gitignore file which disregards the virtual environment on my machine and my own dbconfig file when pushing my project to Github.
* Project Description pdf file contains the specification for this project. 

## Virtual Environment 

This repository consists of a server which should be run in a virtual environment.

#### Running a VM for the first time on your machine

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

#### If you already have a VM installed on your machine

1. Pull my project from Github and navigate to the folder location.

2. .\venv\Scripts\activate.bat

3. python server.py

To exit the virtual environment:
4. deactivate

## How to clone this repository

1. Go to GitHub.
2. Go to my repository: https://github.com/johndunne2019/Fundamentals-of-Data-Analysis-Project-2019
3. Click the Code button which is colored green.
4. Click on HTTPS and copy the link that is shown. 
5. Open the command line on your machine, navigate to the directory where you would like to clone the repository down to.
6. Enter the command: git clone followed by the URL of the repository.
7. The repository will be cloned down to your current working directory. 
8. You will need to navigate to this folder location on the command line in order to run the program.
9. Details on how to view my jupyter notebook are described in the next section below.

## MySQL Database 

I have created a MySQL database called bullfinder which will contain details on stock bulls that are used in for breeding in the suckler beef breeding cattle system in Ireland. I have sourced the bulls details from the Irish Cattle Breeding Federation bull search - https://webapp.icbf.com/v2/app/bull-search. 

I have created two tables of data one called bulls and a second called bull details. They are linked by foreign key reference on the id field in each table.

The commands that were used to create the database and table and insert data into the table are saved in the folder SQL in this repository in a file called initdb.sql

#### bulls table - served to BullViewer.html
* The id of each bull which is auo incremented and serves as the primary key. 
* The AI code of each bull.
* The name of each bull.
* The breed of each bull.
* The owner of each bull.

#### bulldetails table - served to BullDetails.html
* The AI code of the bull which is unique and serves as the primary key.
* The sire (father) of each bull.
* The dam (mother) of each bull.
* The star rating out of 5.
* The star value which is a euro value assigned to each bull.
* The index reliability which is a % measure of how reliable their star rating and value is.
* id which is the foreign key reference between the bulls and bull details tables in the database.

#### I have added below an image of the bulls table when the describe command is run in MySQL.

![describebulls](/images/describebulls.PNG)

#### I have added below an image of data contained in the bulls table:

![describebulls](/images/bulls.PNG)

#### I have added below an image of the bull details table when the describe command is run in MySQL.
![describebulls](/images/describebulldetails.PNG)

#### I have added below an image of data contained in the bull details table:
![describebulls](/images/bulldetails.PNG)