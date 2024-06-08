import sqlite3


class Database():
    def create_connect(self):
        try:
            self.database = sqlite3.connect('./data/database.db')
            self.cursor = self.database.cursor()
        except:
            print('[DATABASE] Connection lost!')

    def send_sql_request(self, sql_request: str):
        res = self.cursor.execute(sql_request)
        self.database.commit()
        return res.fetchall()

    def close(self):
        self.database.close()

    @staticmethod
    def add_equipment(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"INSERT INTO sos_oborudovanie(kod_oborud, invent_nomer, sostoyanie, kod_tipa_ucheta) VALUES({data['kod_oborud']}, {data['invent_nomer']}, '{data['sostoyanie']}', {data['kod_tipa_ucheta']});")
        print(f"[COMMAND] INSERT INTO sos_oborudovanie(kod_oborud, invent_nomer, sostoyanie, kod_tipa_ucheta) VALUES({data['kod_oborud']}, {data['invent_nomer']}, '{data['sostoyanie']}', {data['kod_tipa_ucheta']});")
        db.close()

    @staticmethod
    def delete_equipment(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"DELETE FROM sos_oborudovanie WHERE kod_oborud = {data['id']};")
        print(f"[COMMAND] DELETE FROM sos_oborudovanie WHERE kod_oborud = {data['id']};")
        db.close()

    @staticmethod
    def edit_equipment(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"UPDATE sos_oborudovanie SET sostoyanie = '{data['sostoyanie']}', invent_nomer = {data['invent_nomer']} WHERE kod_oborud = {data['kod_oborud']};")
        print(f"[COMMAND] UPDATE sos_oborudovanie SET sostoyanie = '{data['sostoyanie']}', invent_nomer = {data['invent_nomer']} WHERE kod_oborud = {data['kod_oborud']};")
        db.close()

    @staticmethod
    def add_mol(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"INSERT INTO sos_MOL(kod_MOL, nach_otvetst, kod_sotr) VALUES({data['kod_MOL']}, '{data['nach_otvetst']}', {data['kod_sotr']});")
        print(f"[COMMAND] INSERT INTO sos_MOL(kod_MOL, nach_otvetst, kod_sotr) VALUES({data['kod_MOL']}, '{data['nach_otvetst']}', {data['kod_sotr']});")
        db.close()

    @staticmethod
    def edit_mol(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"UPDATE sos_MOL SET kod_sotr = '{data['kod_sotr']}', nach_otvetst = '{data['nach_otvetst']}' WHERE kod_MOL = {data['kod_MOL']};")
        print(f"[COMMAND] UPDATE sos_MOL SET kod_sotr = '{data['kod_sotr']}', nach_otvetst = '{data['nach_otvetst']}' WHERE kod_MOL = {data['kod_MOL']};")
        db.close()

    @staticmethod
    def delete_mol(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"DELETE FROM sos_MOL WHERE kod_MOL = {data['kod_MOL']};")
        print(f"DELETE FROM sos_MOL WHERE kod_MOL = {data['kod_MOL']};")
        db.close()


if __name__ == '__main__':
    # ОБОРУДОВАНИЕ
    # Database.delete_equipment({'id': 1007})
    # Database.add_equipment({
    #     'kod_oborud': 1007,
    #     'invent_nomer': 10107,
    #     'sostoyanie': 'Требует ремонта',
    #     'kod_tipa_ucheta': 107
    # })
    # Database.edit_equipment({
    #     'kod_oborud': 1007,
    #     'invent_nomer': 10107,
    #     'sostoyanie': 'Неисправен',
    #     'kod_tipa_ucheta': 107
    # })

    # МОЛы
    # Database.add_mol({
    #     'kod_MOL': 104,
    #     'nach_otvetst': '2023-04-01',
    #     'kod_sotr': 2,
    # })
    # Database.edit_mol({
    #     'kod_MOL': 104,
    #     'nach_otvetst': '2023-05-01',
    #     'kod_sotr': 2,
    # })
    # Database.delete_mol({'kod_MOL': 103})
    pass