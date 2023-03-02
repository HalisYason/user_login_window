
import sqlite3 as sql


# veritabanı kodlar

def tablo_olustur():
    with sql.connect("user_login.db") as vt:
        cursor = vt.cursor()

        cursor.execute(""" CREATE TABLE İF NOT EXİSTS user(
        user_name text,
        password text
        )
        """)

        vt.commit()


def ekle(name,password):
    with sql.connect("user_login.db") as vt:
        cursor = vt.cursor()

        data = (name,password)

        ekle_v = "insert into user(user_name, password) values(?,?) "

        cursor.execute(ekle_v,data)

        vt.commit() 


# veritabanındaki kullanıcıları kontrol eder
def kontrol_et(name, password):
    with sql.connect("user_login.db") as vt:
        cursor = vt.cursor()
        data = (name, password)
        ekle_v = "SELECT * FROM user WHERE user_name = ? AND password = ?"
        cursor.execute(ekle_v, data)

        kul = cursor.fetchone() # Sadece bir sonuç tuple'ı varsa fetchone() kullanılabilir

        vt.commit()

        if kul is not None and kul[0] == name and kul[1] == password:
            return True
        else:
            return False



