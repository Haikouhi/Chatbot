CREATE TABLE class (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    lastname VARCHAR(40) NOT NULL,
    firstname VARCHAR(40) NOT NULL,
    city VARCHAR(40) NOT NULL,
    birthdate DATE NOT NULL,
    email VARCHAR(40) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    gender VARCHAR(5) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB;




INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Dao', 'Mai', 'St Genis Laval', '1989-12-15', 'md.maidao@gmail.com', '776990433', 'F');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Tin', 'William', 'Villeurbanne', '1980-05-08', 'tin.wiliam@gmail.com', '664037832', 'M');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Flaus', 'Theo', 'Lagnieu', '1996-09-16', 'flaus.theo69@gmail.com', '695311989', 'M');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Ros', 'Hugo', 'Lyon', '1988-11-18', 'hros38@gmail.com', '782581856', 'M');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Kettab', 'Bachir', 'Villeurbanne', '1987-07-08', 'kettab.bachir@gmail.com', '630944171', 'M');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Dentand', 'Arthur', 'Lyon', '1995-04-01', 'arthurdentand@gmail.com', '668482061', 'M');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Toblome', 'Kodjo', 'La Tour du Pin', '1983-05-30', 'ferdinantoblome@gmail.com', '751052474', 'M');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Merel', 'Caroline', 'Lyon', '1997-12-29', 'carolinemerel@gmail.com', '646813231', 'F');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Scheurer', 'Timothée', 'Lyon', '1993-09-03', 't.scheurer@yahoo.fr', '632362103', 'M');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Arethens', 'Emmanuel', 'Villeurbanne', '1995-04-10', 'emmanuel.arethens1@gmail.com', '637836269', 'M');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Fulleringer', 'Adrien', 'Lyon', '1993-12-22', 'fuladri38@gmail.com', '635488439', 'M');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Coste', 'Christine', 'Lyon', '1981-09-02', 'christine.costeduvaud@gmail.com', '610571581', 'F');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Guseynov', 'Rustam', 'Grenoble', '1991-03-17', 'rustamguseynov38@gmail.com', '769018988', 'M');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Vavrille', 'Nory', 'Saint Romain en Gal', '1988-01-06', 'noryvavrille88@gmail.com', '781836349', 'M');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Oroudjian', 'Haikouhi', 'Villeurbanne', '1989-09-11', 'h.oroudjian@protonmail.com', '658175807', 'F');
INSERT INTO class (lastname, firstname, city, birthdate, email, phone_number, gender) 
    VALUES ('Champredon', 'Marina', 'Villeurbanne', '1990-06-26', 'marina.champredon@gmail.com', '698008570', 'F');


ALTER TABLE class 
ADD COLUMN gender VARCHAR NOT NULL;

UPDATE class 
SET gender='F'
WHERE id=2, 3, 4, 5, 6, 7;