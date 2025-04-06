import mysql.connector as sql_con
# import json
# DB=sql_con.connect(
#     host='mysql-129d035c-dbms-proj.h.aivencloud.com',
#     user='avnadmin',
#     password='AVNS_lsv-j0cT7m3_tAcZhMz',
#     database='dbms_proj'
# )
# if not DB:
#     print("not connected")
#     exit()
# print(DB)
# cursor=DB.cursor()
# cursor.execute('show tables;')
# for i in cursor:
#     print(i)

connection = sql_con.connect(
    database="defaultdb",
    host="mysql-129d035c-dbms-proj.h.aivencloud.com",
    password="AVNS_lsv-j0cT7m3_tAcZhMz",
    port=24830,
    user="avnadmin"
    )

try:
    cursor = connection.cursor(dictionary=True)
    # cursor.execute("CREATE TABLE mytest (id INT PRIMARY KEY)")
    cursor.execute("INSERT INTO mytest (id) VALUES (1), (2),(3),(4)")
    cursor.execute("SELECT * FROM mytest")
    print(cursor.fetchall())
finally:
    connection.close()

# for i in cursor:
#     js=json.loads(i[0])
#     js["is ok"]=212
#     cursor.execute(f"update temp set ok_bro = '{json.dumps(js)}';")
#     DB.commit()
# def func(a):
#     return a**2
# print(func(5))
# import asyncio
