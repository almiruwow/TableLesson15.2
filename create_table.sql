----- СОЗДАНИЕ ТАБЛИЦ ------

CREATE TABLE animal_type
(
id integer PRIMARY KEY AUTOINCREMENT,
type VARCHAR(50)
);

CREATE TABLE breed_type(
id integer PRIMARY KEY AUTOINCREMENT,
type VARCHAR(50)
);

CREATE TABLE color1(
id integer PRIMARY KEY AUTOINCREMENT,
color1 VARCHAR(50)
);

CREATE TABLE color2(
id integer PRIMARY KEY AUTOINCREMENT,
color VARCHAR(50) CONSTRAINT c DEFAULT NULL
);

CREATE TABLE data_animal(
id integer PRIMARY KEY AUTOINCREMENT,
name VARCHAR(50) CONSTRAINT name_ DEFAULT NULL,
date_of_birth DATE,
animal_type_id integer,
breed_id integer,
color1_id integer,
color2_id integer,
FOREIGN KEY (animal_type_id) REFERENCES animal_type(id),
FOREIGN KEY (breed_id) REFERENCES breed_type(id),
FOREIGN KEY (color1_id) REFERENCES color1(id),
FOREIGN KEY (color2_id) REFERENCES color2(id)
);

CREATE TABLE months(
id INTEGER PRIMARY KEY AUTOINCREMENT,
month integer
);

CREATE TABLE years(
id INTEGER PRIMARY KEY AUTOINCREMENT,
month integer
);


CREATE TABLE arrival_details (
id integer PRIMARY KEY AUTOINCREMENT,
month_id integer,
years_id integer,
age_upon_outcome_id VARCHAR(100),
FOREIGN KEY (month_id) REFERENCES months(id),
FOREIGN KEY (years_id) REFERENCES years(id)
);

CREATE TABLE outcome_subtype(
id INTEGER PRIMARY KEY AUTOINCREMENT,
subtype VARCHAR(100)
);

CREATE TABLE outcome_type(
id INTEGER PRIMARY KEY AUTOINCREMENT,
type VARCHAR(100)
);

CREATE TABLE animal (
id integer PRIMARY KEY AUTOINCREMENT,
name_id integer,
animal_id VARCHAR(50),
arrival_detail_id integer,
outcome_subtype_id integer,
outcome_type_id integer,
FOREIGN KEY (name_id) REFERENCES data_animal(id),
FOREIGN KEY (arrival_detail_id) REFERENCES arrival_details(id),
FOREIGN KEY (outcome_subtype_id) REFERENCES outcome_subtype(id),
FOREIGN KEY (outcome_type_id) REFERENCES outcome_type(id)
);


--- Внесение данных в таблицу цветов

INSERT INTO color1(color)
VALUES ('orange'),('blue'),('white'),('black'),('brown'),('seal'),('Breed Specific'),('cream'),('chocolate'),('silver'),('flame'),('lynx'),('lilac'),('buff'),('blue cream'),('silver lynx'),('gray'),('yellow'),('apricot'),('brown tiger'),('black tiger'),('tan'),('orange tiger'),('sable'),('pink'),('brown merle'),('fawn')

