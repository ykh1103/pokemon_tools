import requests
import mysql.connector

# DBに接続
connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='YKH1103nino0617',
                                     database='db_test')
with connection:
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM `db_test`.`pokemons`")
        cursor.execute("ALTER TABLE `db_test`.`pokemons` AUTO_INCREMENT = 1;")

        for i in range(1010):
            pokemons_profile = {
                "id": None,
                "icon": None,
                "name": None,
                "type1": None,
                "type2": None,
            }

            # idの取得
            pokemons_profile["id"] = i + 1

            # iconの取得
            pokemons_url = f"https://pokeapi.co/api/v2/pokemon/{pokemons_profile['id']}"
            pokemons_response = requests.get(pokemons_url)

            pokemons_data = pokemons_response.json()
            # print(pokemons_data['sprites']['front_default'])
            pokemons_profile["icon"] = pokemons_data['sprites']['front_default']

            # typeの取得
            types = pokemons_data['types']
            pokemons_profile["type1"] = int(pokemons_data['types'][0]['type']['url'].split("/")[-2])
            if len(types) > 1:
                pokemons_profile["type2"] = int(pokemons_data['types'][1]['type']['url'].split("/")[-2])

            # nameの取得
            pokemons_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemons_profile['id']}/"
            pokemons_response = requests.get(pokemons_url)
            pokemons_data = pokemons_response.json()
            pokemons_profile["name"] = pokemons_data['names'][0]['name']

            # insert文の発行
            # pokemonsテーブルに挿入
            sql = """
                INSERT INTO `db_test`.`pokemons`
                (
                    `no`,
                    `name`,
                    `type_id1`,
                    `type_id2`,
                    `icon`,
                    `created_date`,
                    `created_by`
                )
                VALUES
                (
                    %(id)s,
                    %(name)s,
                    %(type1)s,
                    %(type2)s,
                    %(icon)s,
                    now(),
                    'kawano'
                );
            """
            cursor.execute(sql, pokemons_profile)
            print(f"ポケモン：{pokemons_profile['name']}が登録されました")
        connection.commit()
        cursor.close()
