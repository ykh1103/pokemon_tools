import requests
import mysql.connector

# DBに接続
connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='YKH1103nino0617',
                                     database='db_test')

# タイプ一覧取得
types_url = "https://pokeapi.co/api/v2/type/"
types_response = requests.get(types_url)
types_data = types_response.json()

# typesテーブルに挿入
with connection:
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM `db_test`.`types`")
        cursor.execute("ALTER TABLE `db_test`.`types` AUTO_INCREMENT = 1;")
        sql = """
            INSERT INTO `db_test`.`types`
            (
                `name`,
                `created_date`,
                `created_by`
            )
            VALUES
            (
                %s,
                now(),
                'kawano'
            );
        """
        for type_result in types_data['results']:
            type_url = type_result['url']
            type_response = requests.get(type_url)
            type_data = type_response.json()
            cursor.execute(sql, [str(type_data['names'][0]['name'])])

    connection.commit()
cursor.close()
