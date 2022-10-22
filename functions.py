import sqlite3


def search_pet_id(value):

    with sqlite3.connect('new_animals.sqlite') as connection:
        cursor = connection.cursor()

        query_result = f'''
            SELECT animal.id,
                   arrival_details.age_upon_outcome_id,
                   animal.animal_id,
                   animal_type.type,
                   data_animal.name,
                   breed_type.type,
                   color1.color,
                   color2.color,
                   data_animal.date_of_birth,
                   outcome_subtype.subtype,
                   outcome_type.type,
                   months.month,
                   years.month
            FROM animal
            LEFT JOIN data_animal ON animal.name_id = data_animal.id
            INNER JOIN animal_type ON data_animal.animal_type_id = animal_type.id
            INNER JOIN breed_type ON data_animal.breed_id = breed_type.id
            INNER JOIN color1 ON data_animal.color1_id = color1.id
            LEFT JOIN color2 ON data_animal.color2_id = color2.id
            LEFT JOIN outcome_subtype ON animal.outcome_subtype_id = outcome_subtype.id
            LEFT JOIN outcome_type on animal.outcome_type_id = outcome_type.id
            INNER JOIN arrival_details ON animal.arrival_detail_id = arrival_details.id
            INNER JOIN months on arrival_details.month_id = months.id
            INNER JOIN years ON arrival_details.years_id = years.id
            WHERE animal.id = {value}
        '''

        cursor.execute(query_result)

        result = cursor.fetchall()

        return result[0]

