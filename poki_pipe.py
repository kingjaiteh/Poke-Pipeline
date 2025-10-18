from sqlalchemy import create_engine
import pandas as pd
import requests
import json


# Create engine
engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/my_new_database")

def get_pokemon_info(id):
   
    url = f"https://pokeapi.co/api/v2//pokemon/{id}"

    response = requests.get(url)

    if response.status_code == 200:

        pokemon_data = response.json()

        return {
        "id": pokemon_data["id"],
        "name": pokemon_data["name"],
        "types": json.dumps([t["type"]["name"] for t in pokemon_data["types"]]),
        "stats": json.dumps({s["stat"]["name"]: s["base_stat"] for s in pokemon_data["stats"]}),
        "abilities": json.dumps([a["ability"]["name"] for a in pokemon_data["abilities"]])
    }

    else:

        print(f"Failed to retrieve data {response.status_code}")

for i in range(1, 120):
    pokemon_info = get_pokemon_info(i)

    df = pd.DataFrame([pokemon_info])  # Wrap in list 

    with engine.connect() as conn:
        print(pd.io.sql.get_schema(df, name="poke_store", con=conn))

    df.to_sql(
        name="poke_store",
        con=engine,
        if_exists="append",
        index=False
    )
    i += 1
    print (i)
