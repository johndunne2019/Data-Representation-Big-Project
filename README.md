# Data-Representation-Big-Project
My project submission for the Data Representation module at GMIT 2020

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