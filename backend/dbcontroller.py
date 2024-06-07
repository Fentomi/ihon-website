import sqlite3


class Database():
    def create_connect(self):
        try:
            self.database = sqlite3.connect('./data/database.db')
            self.cursor = self.database.cursor()
            print('[DATABASE] Connection access!')
        except:
            print('[DATABASE] Connection lost!')

    def send_sql_request(self, sql_request: str):
        res = self.cursor.execute(sql_request)
        self.database.commit()
        return res.fetchall()

    def close(self):
        self.database.close()

    #Функция, конвертирующая данные в json-формат, удобный формат для front-end'a
    @staticmethod
    def convert_data_in_json(data: list, type_data: str) -> dict:
        result = list()
        if type_data == 'services':
            for item in data:
                result.append({'id_service': item[0], 'name_service': item[1]})
        elif type_data == 'requests':
            for item in data:
                db = Database()
                db.create_connect()
                if db.send_sql_request(
                        f"""select services.name_service
                            from addictions, services 
                            where addictions.id_req = {item[0]} and services.id_service = addictions.id_service"""):
                    list_services = db.send_sql_request(
                        f"""select services.name_service
                            from addictions, services 
                            where addictions.id_req = {item[0]} and services.id_service = addictions.id_service""")
                    services = list()
                    for item1 in list_services:
                        services.append(item1[0])
                else:
                    services = list()

                result.append({
                    'id_request': item[0],
                    'FIO': item[1],
                    'email': item[2],
                    'phone': item[3],
                    'device': item[4],
                    'desc_problem': item[5],
                    'services': services
                })
        elif type_data == 'addictions':
            for item in data:
                result.append({
                    'service_name': item[0],
                    'id_request': item[1]
                })
        return result

    @staticmethod
    def write_data_in_database(data: dict, type_data: str):
        db = Database()
        db.create_connect()
        if type_data == "request":
            db.send_sql_request(f"INSERT INTO requests(FIO, email, device, desc_problem, phone_number) VALUES('{data['FIO']}', '{data['email']}', '{data['device']}', '{data['desc_problem']}', '{data['phone']}');")
            if data['services']:
                print(data)
                Database.write_data_in_database(data, 'addiction')
        elif type_data == "addiction":
            print(data)
            #получим id всех выделенных сервисов перед добавлением их в базу данных
            list_id_services = list()
            id_requests = db.send_sql_request("Select requests.id_req from requests")
            id_request = id_requests[-1][0]
            for item in data['services']:
                list_id_services.append(db.send_sql_request(f"SELECT services.id_service FROM services WHERE name_service = '{item}'"))
            for item in list_id_services:
                db.send_sql_request(f"INSERT INTO addictions VALUES({item[0][0]}, {id_request});")
        else:
            print("Ошибка записи данных в базу данных")
        db.close()

    @staticmethod
    def delete_data_in_database(data: dict, type_data: str):
        print(data)
        db = Database()
        db.create_connect()
        if data['services']:
            db.send_sql_request(f"DELETE FROM addictions WHERE addictions.id_req = {data['id_request']}")
        db.send_sql_request(f"DELETE FROM requests WHERE requests.id_req = {data['id_request']}")
        db.close()


if __name__ == '__main__':
    db = Database()
    # db.write_data_in_database({'services': ['Установка антивируса', 'Чистка компьютера'], 'id_req': 6}, 'addiction')
    # db.create_connect()
    # res = db.send_sql_request("SELECT * FROM addictions")
    # print(res)
    # db.close()
