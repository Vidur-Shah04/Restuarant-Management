import mysql.connector as sql_con
def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-_+="
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    if not has_upper:
        print( "Password must include at least one uppercase letter.")
        return False
    if not has_lower:
        print( "Password must include at least one lowercase letter.")
        return False
    if not has_digit:
        print( "Password must include at least one digit.")
        return False
    if not has_special:
        print( "Password must include at least one special character (!@#$%^&*()-_+=).")
        return False
    return True

def fetch_bill_id():
    DB = sql_con.connect(
       database="dbms_proj",
    host="hostname",
    password="your password",
    port=00000,
    user="user name"
    )
    cursor=DB.cursor()
    cursor.execute("select max(bill_id) from bills;")
    ret=cursor.fetchone()
    DB.close()
    return ret
# print(fetch_bill_id())

def new_user(uname,passwd):
    DB = sql_con.connect(
    database="dbms_proj",
    host="hostname",
    password="your password",
    port=00000,
    user="user name"
    )
    cursor=DB.cursor()
    cursor.execute(f"select user_id from users where user_id = '{uname}';")
    if cursor.fetchone():
        print("User id already exists , pick a different username or sign in")
        return False
    if validate_password(passwd):
        query="insert into users values('{}','{}');".format(uname,passwd)
        # print(query)
        cursor.execute(query)
        DB.commit()
        DB.close()
    else:return False
    print("Sign in Successful")
    return True
# new_user('ok',"boomer")

def login_user(uname,passwd):
    DB = sql_con.connect(
    database="dbms_proj",
    host="hostname",
    password="your password",
    port=00000,
    user="user name"
    )
    cursor=DB.cursor()
    cursor.execute(f"select * from users where user_id = '{uname}';")
    password=cursor.fetchone()
    if not password:
        print("User does not exist")
        return False
    if passwd==password[1]:
        return True
    print("Wrong password")
    DB.close()
    return False    
# login_user("Admin","admin is cool")

# delete from users where user_id = 'u'
''' 
    bills table -> fetch user_id ke past bills (latest 5 bills) , bill. no in increasing order
    fetch bills from json file as per bill_id 
    give option to user to select bill no.
    display said bill
'''
def delete_user(user_id_input):
    DB = sql_con.connect(
    database="dbms_proj",
    host="hostname",
    password="your password",
    port=00000,
    user="user name"
)
    cursor = DB.cursor()
    try:
        cursor.execute(f"DELETE FROM users WHERE user_id = '{user_id_input}' ;")
        print("Cart empty user deleted !!")
        DB.commit()
    except:pass
    DB.close()

def fetch_bills(user_id):
    DB = sql_con.connect(
    database="dbms_proj",
    host="hostname",
    password="your password",
    port=00000,
    user="user name"
)
    cursor = DB.cursor()
    cursor.execute(
                f"SELECT * FROM bills WHERE user_id = '{user_id}' ORDER BY bill_id DESC LIMIT 5 ;"
            )
    results = cursor.fetchall()
    if results:
        return results
    return False

# fetch_bills('a')
