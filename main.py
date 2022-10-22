from flask import Flask, jsonify
from functions import search_pet_id

app = Flask('__main__')

@app.route('/<itemid>')
def search_pet(itemid):
    spi = search_pet_id(int(itemid))

    data = {
        "id":f"{spi[0]}",
        "name":f"{spi[4]}",
        "date_of_birth": f"{spi[8]}",
        "animal_id":f"{spi[2]}",
        "animal_type":f"{spi[3]}",
        "breed": f"{spi[5]}",
        "color1": f"{spi[6]}",
        "color2": f"{spi[7]}",
        "outcome_subtype": f"{spi[9]}",
        "outcome_type":f"{spi[10]}",
        "age_upon_outcome":f"{spi[1]}",
        "outcome_month":f"{spi[11]}",
        "outcome_year":f"{spi[-1]}"
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run()