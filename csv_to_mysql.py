#ran it only once to transfer csv to mysql
import os
import csv
import mysql.connector as sql_con
# DB=sql_con.connect(
#     host='localhost',
#     user='root',
#     password='12345678',
#     database='dbms_proj'
# )
DB = sql_con.connect(
    database="dbms_proj",
    host="mysql-129d035c-dbms-proj.h.aivencloud.com",
    password="AVNS_lsv-j0cT7m3_tAcZhMz",
    port=24830,
    user="avnadmin"
    )

cursor=DB.cursor()
cursor.execute("SET SESSION sql_require_primary_key = 0;")
DB.commit()
csv_files=(i for i in os.listdir() if i.endswith(".csv"))

for file_name in csv_files:     
    with open (file_name,'r') as fh:
        reader=csv.reader(fh,delimiter=",")
        for i in reader:
            if i[0]=="Item Code":
                query=f"Create table {file_name[:-4].lower()} (item varchar(50),name varchar(100),price int);"
                # print(query)
                cursor.execute(query)
                # DB.commit()
            else:
                query=f"insert into {file_name[:-4].lower()} values(\'{i[0].upper()}\',\'{i[1]}\',{i[2]})"
                print(query)
                cursor.execute(query)
DB.commit()
DB.close()

