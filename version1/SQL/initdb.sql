CREATE DATABASE stockbullfinder;

use stockbullfinder 

CREATE TABLE bulls (
    code VARCHAR(10) PRIMARY KEY, 
    name VARCHAR(250), 
    breed VARCHAR(250), 
    owner VARCHAR(250)
    );

insert into bulls(code, name, breed, owner) VALUES
("FSZ", "Fiston", "Charlaois", "National Cattle Breeding Centre"),
("BBQ", "Ballyfin Borat", "Belgian Blue", "Dovea Genetics"),
("CWI", "Castleview Casino", "Limousin", "Dovea Genetics"),
("CEQ", "Colosse Et Des Tourelle", "Belgian Blue", "Eurogene"),
("LM2388", "Dimoiwii", "Limousin", "Worldwide Sires Ireland"),
("KCH", "Clenagh Hank", "Charlaois", "Gene Ireland"),
("CH4320", "Liseron", "Charlaois", "National Cattle Breeding Centre");

select * from bulls;

