import requests
import mysql.connector

# DBに接続
connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='YKH1103nino0617',
                                     database='db_test')

with connection:
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM `db_test`.`skills`")
        cursor.execute("ALTER TABLE `db_test`.`skills` AUTO_INCREMENT = 1;")

        for i in range(900):
            # 登録内容
            skills_profile = {
                "id": None,
                "name": None,
                "type_id": None,
            }
            # nameの取得
            skills_profile["id"] = i + 1
            skills_url = f"https://pokeapi.co/api/v2/move/{skills_profile['id']}/"
            skills_response = requests.get(skills_url)
            skills_data = skills_response.json()
            skills_profile["name"] = skills_data['names'][0]['name']

            # type_idの取得
            skills_profile["type_id"] = int(skills_data['type']['url'].split("/")[-2])

            # insert文の発行
            # skillsテーブルに挿入
            sql = """
                INSERT INTO `db_test`.`skills`
                (
                    `name`,
                    `type_id`,
                    `created_date`,
                    `created_by`
                )
                VALUES
                (
                    %(name)s,
                    %(type_id)s,
                    now(),
                    'kawano'
                );
             """
            cursor.execute(sql, skills_profile)
            print(f"わざ：{skills_profile['name']}が登録されました")

        connection.commit()
        cursor.close()


