import sqlite3

# Это были данные для сравнения и дальнейшего заполнения таблиц

breed = {1: 'domestic shorthair', 2: 'domestic mediumhair', 3: 'siamese', 4: 'russian blue', 5: 'domestic longhair', 6: 'manx', 7: 'ragdoll', 8: 'snowshoe/domestic shorthair', 9: 'snowshoe', 10: 'angora', 11: 'himalayan', 12: 'domestic longhair/persian', 13: 'japanese bobtail', 14: 'domestic longhair/rex', 15: 'siamese/domestic shorthair', 16: 'domestic mediumhair/siamese', 17: 'maine coon', 18: 'devon rex', 19: 'balinese', 20: 'american shorthair', 21: 'british shorthair', 22: 'angora/persian', 23: 'munchkin shorthair', 24: 'domestic shorthair/siamese', 25: 'manx/domestic longhair', 26: 'persian', 27: 'cymric', 28: 'tonkinese', 29: 'siamese/angora', 30: 'burmese', 31: 'sphynx', 32: 'domestic shorthair/domestic mediumhair', 33: 'bengal', 34: 'domestic longhair/russian blue', 35: 'bombay', 36: 'exotic shorthair', 37: 'domestic shorthair/british shorthair', 38: 'abyssinian', 39: 'manx/domestic shorthair', 40: 'norwegian forest cat', 41: 'snowshoe/ragdoll', 42: 'manx/siamese', 43: 'turkish van', 44: 'cornish rex', 45: 'birman', 46: 'american curl shorthair', 47: 'siamese/japanese bobtail', 48: 'havana brown', 49: 'munchkin longhair', 50: 'bengal/domestic shorthair', 51: 'domestic shorthair/domestic shorthair', 52: 'pixiebob shorthair', 53: 'american wirehair', 54: 'domestic mediumhair/maine coon', 55: 'domestic shorthair/maine coon', 56: 'scottish fold', 57: 'oriental sh', 58: 'chartreux', 59: 'turkish angora', 60: 'javanese', 61: 'domestic shorthair/manx', 62: 'domestic longhair/domestic longhair', 63: 'domestic shorthair/abyssinian', 64: 'ocicat', 65: 'domestic mediumhair/manx'}

color1 = {1: 'orange', 2: 'blue', 3: 'white', 4: 'black', 5: 'brown', 6: 'seal', 7: 'Breed Specific', 8: 'cream', 9: 'chocolate', 10: 'silver', 11: 'flame', 12: 'lynx', 13: 'lilac', 14: 'buff', 15: 'blue cream', 16: 'silver lynx', 17: 'gray', 18: 'yellow', 19: 'apricot', 20: 'brown tiger', 21: 'black tiger', 22: 'tan', 23: 'orange tiger', 24: 'sable', 25: 'pink', 26: 'brown merle', 27: 'fawn'}

color2 = {1: 'white', 2: 'black', 3: 'orange', 4: 'blue', 5: 'seal', 6: 'brown', 7: 'blue cream', 8: 'lynx', 9: 'red', 10: 'cream', 11: 'gray', 12: 'buff', 13: 'chocolate', 14: 'silver', 15: 'flame', 16: 'tan', 17: 'apricot', 18: 'yellow', 19: 'lilac'}

years = {1: 2013, 2: 2014, 3: 2015, 4: 2016, 5: 2017, 6: 2018}

os = {1: 'Partner', 2: 'Offsite', 3: 'SCRP', 4: 'Foster', 5: 'In Kennel', 6: 'Suffering', 7: 'Rabies Risk', 8: 'Medical', 9: 'At Vet', 10: 'In Foster', 11: 'Enroute', 12: 'Aggressive', 13: 'Barn', 14: 'Snr', 15: 'Possible Theft', 16: 'In Surgery', 17: 'Underage', 'NULL':None}


ot = {1: 'Transfer', 2: 'Adoption', 3: 'Return to Owner', 4: 'Died', 5: 'Euthanasia', 6: 'Missing', 7: 'Disposal', 8: 'Rto-Adopt', 'NULL': None}



# Это цикл код для сравнения и дальнейшего заполнения данных в таблицу data_animal в поля (name, date_of_birth)

# for r in result:
#     if r[1] == None:
#         query1 = 'INSERT INTO data_animal(name, date_of_birth)'
#         query2 = f'VALUES (NULL, "{r[2]}")'
#         norm_query = query1 + ' ' + query2
#         cursor1.execute(norm_query)
#     else:
#         query3 = f'''
#             INSERT INTO data_animal(name, date_of_birth)
#             VALUES ("{r[1]}", "{r[2]}")
#         '''
#         cursor1.execute(query3)



# for r in result:
#     a = None
#     for key, value in os.items():
#         if r[1] == value:
#             a = key



# CREATE TABLE animal_type
# (
# id integer PRIMARY KEY AUTOINCREMENT,
# type VARCHAR(50)
# );
#
# CREATE TABLE breed_type(
# id integer PRIMARY KEY AUTOINCREMENT,
# type VARCHAR(50)
# );
#
# CREATE TABLE color1(
# id integer PRIMARY KEY AUTOINCREMENT,
# color1 VARCHAR(50)
# );
#
# CREATE TABLE color2(
# id integer PRIMARY KEY AUTOINCREMENT,
# color VARCHAR(50) CONSTRAINT c DEFAULT NULL
# );
#
# CREATE TABLE data_animal(
# id integer PRIMARY KEY AUTOINCREMENT,
# name VARCHAR(50) CONSTRAINT name_ DEFAULT NULL,
# date_of_birth DATE,
# animal_type_id integer,
# breed_id integer,
# color1_id integer,
# color2_id integer,
# FOREIGN KEY (animal_type_id) REFERENCES animal_type(id),
# FOREIGN KEY (breed_id) REFERENCES breed_type(id),
# FOREIGN KEY (color1_id) REFERENCES color1(id),
# FOREIGN KEY (color2_id) REFERENCES color2(id)
# );
#
# CREATE TABLE months(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# month integer
# );
#
# CREATE TABLE years(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# month integer
# );
#
#
# CREATE TABLE arrival_details (
# id integer PRIMARY KEY AUTOINCREMENT,
# month_id integer,
# years_id integer,
# age_upon_outcome_id VARCHAR(100),
# FOREIGN KEY (month_id) REFERENCES months(id),
# FOREIGN KEY (years_id) REFERENCES years(id)
# );
#
# CREATE TABLE outcome_subtype(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# subtype VARCHAR(100)
# );
#
# CREATE TABLE outcome_type(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# type VARCHAR(100)
# );
#
# CREATE TABLE animal (
# id integer PRIMARY KEY AUTOINCREMENT,
# name_id integer,
# animal_id VARCHAR(50),
# arrival_detail_id integer,
# outcome_subtype_id integer,
# outcome_type_id integer,
# FOREIGN KEY (name_id) REFERENCES data_animal(id),
# FOREIGN KEY (arrival_detail_id) REFERENCES arrival_details(id),
# FOREIGN KEY (outcome_subtype_id) REFERENCES outcome_subtype(id),
# FOREIGN KEY (outcome_type_id) REFERENCES outcome_type(id)
# )
