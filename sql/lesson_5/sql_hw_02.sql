USE my_db;

-- Task 4
CREATE TABLE IF NOT EXISTS citizen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    social_number VARCHAR(30),
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(100)
);

-- Task 5
CREATE TABLE goods(
    id INT PRIMARY KEY ,
    title VARCHAR(30),
    quantity INT CHECK (quantity > 0),
    in_stock CHAR(1) CHECK (in_stock IN ('Y', 'N'))
);

-- Task 6
INSERT INTO citizen (social_number, first_name, last_name, email) VALUES ('AG63704698','Amado', 'Gorczany', 'A.Gorczany@gmail.com');
INSERT INTO citizen (social_number, first_name, last_name, email) VALUES ('YG17430251','Amado', 'Gislason', 'Y.Gislason@gmail.com');
INSERT INTO citizen (social_number, first_name, last_name, email) VALUES ('AF683519957','Amado', 'Funk', 'A.Funk@gmail.com');

INSERT INTO citizen (social_number, first_name, last_name, email) VALUES ('MG440899932','Malorie', '', 'M.Gerlach@gmail.com');
INSERT INTO citizen (social_number, first_name, last_name, email) VALUES ('CC813990293','Carleen', '', 'C.Collier@gmail.com');

-- Task 7
ALTER TABLE citizen
MODIFY COLUMN first_name VARCHAR(30) NOT NULL;

ALTER TABLE citizen
MODIFY COLUMN last_name VARCHAR(30) NOT NULL;

-- Task 8
ALTER TABLE citizen
ADD CONSTRAINT UNIQUE (first_name, last_name);

SELECT * FROM citizen;

-- Task 9
DROP TABLE IF EXISTS citizen;

CREATE TABLE IF NOT EXISTS citizen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    social_number VARCHAR(30),
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(100),
    UNIQUE (first_name, last_name)
);

-- Task 10
INSERT INTO citizen (social_number, first_name, last_name, email) VALUES ('AG63704698','Amado', 'Gorczany', 'A.Gorczany@gmail.com');

-- Добавление данных с нарушением ограничений
INSERT INTO citizen (social_number, last_name, email) VALUES ('YG17430251', 'Gislason', 'Y.Gislason@gmail.com');
INSERT INTO citizen (social_number, first_name, last_name, email) VALUES ('YG17430251','Amado', 'Gorczany', 'Y.Gislason@gmail.com');
INSERT INTO citizen (social_number, first_name, email) VALUES ('AF683519957','Amado', 'A.Funk@gmail.com');


