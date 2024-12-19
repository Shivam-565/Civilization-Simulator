import mysql.connector
import endecbysam as endecx

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "tiger",
    "database": "hissim"
}
print(1)
def online(onornot):
    return onornot
def signcheck(onrornot):
    return onornot
print(2)
try:
    conn = mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        database=db_config["database"]
    )
    print(3)
except mysql.connector.errors.DatabaseError:
    print("database is not online")
    online(False)
    exit()
    print(3)
else:
    print(4)
    class signin():
        def __init__(self):
            pass
        def sign(self,namex,passx,email):
            if len(email) > 0 and len(namex) > 0 and len(passx) > 0 and "@" in email and ".com" in email:
                passx = endecx.enc(passx,13)
                cursor = conn.cursor()
                query = f"SELECT * FROM `userinfo` WHERE email = '{email}'"
                cursor.execute(query)
                result = cursor.fetchall()
                if len(result) == 0:
                    try:
                        query = f"INSERT INTO userinfo (name, pass, email) VALUES ('{namex}','{passx}','{email}')"
                        cursor.execute(query)
                        conn.commit()
                    except mysql.connector.Error as warning:
                        conn.rollback()
                        print(warning)
                    else:
                        return True
                        cursor.close()
                        conn.close()
                else:
                    return False
            else:
                return ""

    class login():
        def __init__(self):
            pass
        def log(self,namex,passx,email):
            passx = endecx.enc(passx,13)
            if len(email) > 0 and len(namex) > 0 and len(passx) > 0 and "@" in email and ".com" in email:
                cursor = conn.cursor()
                query = f"SELECT * FROM `userinfo` WHERE name = '{namex}' AND pass = '{passx}' AND email = '{email}'"
                cursor.execute(query)
                result = cursor.fetchone()
                cursor.close()
                if result is not None:
                    return True
                    conn.close()
                else:
                    return False
            else:
                return ""
            

