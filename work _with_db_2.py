import sqlite3
import requests
import time

url = "https://jsonplaceholder.org/users?id"
data = requests.get(url)

# print(data.json())
# print(data.status_code)

con = sqlite3.connect("./login.db",check_same_thread=False)
cur = con.cursor()

# sql = """CREATE TABLE user(
#     id IDENTITY(1,1) PRIMARY KEY,
#     name TEXT,
#     username TEXT,
#     email TEXT,
#     address TEXT,
#     phone TEXT,
#     website TEXT,
#     company TEXT);"""

for i in data.json():
    sql=f"""INSERT INTO user(id,name,username,email,address,phone,website,company)
            VALUES(
            {int(i.get('id'))},
            "{i.get('name')}",
            "{i.get('username')}",
            "{i.get('email')}",
            "{i.get('address')['street']} {i.get('address')['city']}",
            "{i.get('phone')}",
            "{i.get('website')}",
            "{i.get('company')['name']}");
"""
# print(sql)
    try:
        cur.execute(sql)
    except sqlite3.DatabaseError as eror:
        print(eror)
    else:
        con.commit()
        time.sleep(1)
        print("ok")
else:
    cur.close()
    con.close()