/* 
Data Representation Big Project
John Dunne G00273895
Command used to create database and tables and populate the tables with data in MySQL
*/

-- create the bullfinder database
CREATE DATABASE bullfinder;

-- use bullfinder database
use bullfinder 

-- create bulls table
CREATE TABLE bulls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(10),
    name VARCHAR(250), 
    breed VARCHAR(250), 
    owner VARCHAR(250)
    );

-- insert data into bulls table
insert into bulls(code, name, breed, owner) VALUES
("FSZ", "Fiston", "Charlaois", "National Cattle Breeding Centre"),
("BBQ", "Ballyfin Borat", "Belgian Blue", "Dovea Genetics"),
("CWI", "Castleview Casino", "Limousin", "Dovea Genetics"),
("CEQ", "Colosse Et Des Tourelle", "Belgian Blue", "Eurogene"),
("LM2388", "Dimoiwii", "Limousin", "Worldwide Sires Ireland"),
("KCH", "Clenagh Hank", "Charlaois", "Gene Ireland"),
("CH4320", "Liseron", "Charlaois", "National Cattle Breeding Centre");

-- to select all entries in bulls table
select * from bulls;

-- create the second table in the database 
-- adding a foreign key reference https://www.w3schools.com/sql/sql_foreignkey.asp
CREATE TABLE bulldetails (
    code VARCHAR(10),
    sire VARCHAR(200),
    dam VARCHAR(200),
    stars INT NOT NULL,
    starvalue INT NOT NULL,
    reliability INT NOT NULL,
    id INT NOT NULL,
    PRIMARY KEY(code),
    FOREIGN KEY (id) REFERENCES bulls(id)
    );

-- insert into bulldetails table
insert into bulldetails(code, sire, dam, stars, starvalue, reliability, id) VALUES
("FSZ", "Tinor", "Baronne", 5, 127, 98, 1)
("BBQ", "As De Trefle Du Vanove", "Ballyfin Unity", 5, 120, 98, 2)
("CWI", "Otan", "F040", 5, 124, 98, 3)
("CEQ", "Du Coin Jobeline", "Heroique", 1, 49, 93, 4)
("LM2388", "Ondit", "Tinusa", 5, 116, 68, 5)
("KCH", "Goldstar Echo", "Clenagh Urania", 1, 18, 74, 6)
("CH4320", "Castor", "Gaffe", 4, 90, 57, 7);

-- to select all entries in the bulldetails table
select * from bulldetails;