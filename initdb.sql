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

-- adding a foreign key reference https://www.w3schools.com/sql/sql_foreignkey.asp
CREATE TABLE bulldetails (
    code VARCHAR(10),
    sire VARCHAR(20),
    dam VARCHAR(20),
    calving INT NOT NULL,
    id INT NOT NULL,
    PRIMARY KEY (code),
    FOREIGN KEY (id) REFERENCES bulls(id)
    );

-- insert into bulldetails table
insert into bulldetails(code, sire, dam, calving, id) VALUES
("FSZ", "Tinor", "Baronne", 10, 1);