from prettytable import PrettyTable
import mysql.connector as sql_con
import keyboard
import json
import users

# DB=sql_con.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='temp'
# )
DB = sql_con.connect(
    database="dbms_proj",
    host="hostname",
    password="your password",
    port=00000,
    user="user name"
    )
cursor=DB.cursor()

number_map={
    1:"soup",
    2:"sindian",
    3:"schina",
    4:"scon",
    5:'mind',
    6:"mchi",
    7:"mcon",
    8:"rr",
    9:"des",
    "B1":"mocktails",
    "B2":"juices",
    "B3":"milkshake",
    "B4":"hot"
}
order_list=[]
def show_bill(bill=order_list):
    ttl=0
    pt=PrettyTable()
    pt.field_names=['Item Code','Item Name','Rate','Quantity','Amount']
    for i in range(0,len(bill)):
            pt.add_row(bill[i])
            ttl=ttl+bill[i][4]
    pt.add_row(["","","","Total:",ttl])
    print(pt)

def view_menu(file_name):
    cursor.execute(f"select * from {file_name};")
    pt=PrettyTable()
    pt.field_names=['Item Code','Name','Price']
    pt.align["Name"]="l"
    for i in cursor:
        pt.add_row(i)
    print(pt)
    
def place_order(file):
    view_menu(file)
    odr=(input("enter product code(enter back to return to menu):")).upper()
    if odr=="BACK":
        return
    cursor.execute(f"select * from {file};")
    data=cursor.fetchall()
    for code,item,value in data:
        code=code.upper()
        if code==odr:
            try:qua=int(input('''enter quantity of product(enter 0 if no items to add):'''))
            except:
                print("please enter a integer !")
                return 
            if qua<1:return
            for i in order_list:
                if i[0]==code:
                    i[3]+=qua
                    i[4]=i[2]*i[3]
                    return 
            else:
                order_list.append([code,item,value,qua,value*qua])
                break
    else:
        print("Enter Proper Code !")
        return
    print("Item Added successfully")    

def order_food(user_id):
    while True:
        pt=PrettyTable()
        pt.field_names=['Code','Course']
        pt.add_row([0,"View Previous Order(last 5)"])
        pt.add_row([1,"Soup"])
        pt.add_row([2,"Indian Starters"])
        pt.add_row([3,"Chinese Starters"])
        pt.add_row([4,"Continental Starters"])
        pt.add_row([5,"Indian Maincourse"])
        pt.add_row([6,"Chinese Maincourse"])
        pt.add_row([7,"Continental Maincourse"])
        pt.add_row([8,"Rotis,Rice and more"])
        pt.add_row([9,"Desserts"])
        pt.add_row([10,"Beverages"])
        pt.add_row([11,"View Cart"])
        pt.add_row([12,"Checkout"])
        pt.align["Course"]="l"
        print(pt)
        try:cou=int(input('''enter the numeric code for the course you want to order\n(enter 11 to see your bill) :'''))
        except:
            print("Enter Integer values !!")
            continue
        if cou in number_map:
            place_order(number_map[cou])

        if cou == 0 :
            past = users.fetch_bills(user_id)
            if not past:
                print("No previous orders found")
                continue
            with open ('bills.json','r') as fh:
                DATA=json.load(fh)
                past_order={}
                pt=PrettyTable()
                pt.field_names=(["PAST BILLS"])
                for i in past:
                    bill_no=str(i[0])
                    pt.add_row([bill_no])
                    past_order[bill_no]=DATA[bill_no]
                print(pt)
                sel_past=(input("Enter bill number to view the bill: "))
                if not sel_past in past_order:
                    print("enter proper bill no.")
                    print("Press shift key to return to menu")
                    keyboard.wait("shift")
                    continue
                show_bill(past_order[sel_past])
            print("Press shift key to return to menu")
            keyboard.wait("shift")

        if cou==10:
            bt=PrettyTable()
            bt.field_names=['Code','Beverage']
            bt.add_row(["B1","Mocktails"])
            bt.add_row(["B2","Juices"])
            bt.add_row(["B3","Mlkshakes"])
            bt.add_row(["B4","Hot Drinks"])
            bt.align="l"
            print(bt)
            bev=(input("enter Beverage code(enter back to return to menu):")).upper()
            place_order(number_map[bev])
        elif cou == 11:
            if not order_list:
                print("Cart empty !")
                continue
            show_bill()
            edit=input("Do you wish to edit (yes/no)? ->").lower().strip()
            if edit=="yes":
                pass
                item=input("enter Item code to change it's quantity: ").upper().strip()
                for i in order_list:
                    if item == i[0]:
                        try:qua=int(input("Enter desired quatity(enter 0 to remove the item): "))
                        except:
                            print("Enter proper value !!")
                            break
                        if qua<=0:
                            order_list.remove(i)
                            break
                        i[3]=qua
                        i[4]=i[3]*i[2]
                        break
                else:
                    print("enter proper value")
                    continue
                show_bill()
                print("Press shift key to return to menu")
                keyboard.wait("shift")
            else:
                continue    
        elif cou==12:
            if not order_list:
                print("Cart empty !")
                users.delete_user(user_id)
                break
                
            show_bill()
            print("End of Program")
            bill_no=users.fetch_bill_id()[0] + 1
            print(f"Bill No. {bill_no} added to your profile")
            cursor.execute(f"insert into bills(user_id) values('{user_id}');")
            DB.commit()
            with open("bills.json",'r') as fp:
                DATA=json.load(fp)
            with open("bills.json",'w') as fp:
                DATA[bill_no]=order_list
                json.dump(DATA,fp,indent=4)
            break

def user_auth():
    print("Welcome to our Restaurant. Are you a new user? (yes/no)")
    response = input(">> ").strip().lower()
    if response == "yes":
        user_id = input("Choose a user ID: ").strip().lower()
        password = input("Choose a password: ").strip()
        if users.new_user(user_id,password):
            order_food(user_id)
    

    elif response == "no":
        user_id = input("Enter your user ID: ").strip().lower()
        password = input("Enter your password: ").strip()

        if user_id =='admin' and password == "admin is cool":
            print("Admin access granted.")
            cursor=DB.cursor(dictionary=True)
            while True:
                query = input("Enter SQL query (or type 'exit' to logout):\n>> ").strip().lower()
                if query == "exit":
                    print("Logging out of admin mode.")
                    break
                try:cursor.execute(query)
                except:
                    print("recheck your query ...")
                    continue
                pt=PrettyTable()
                pt.align='l'
                temp=cursor.fetchall()
                pt.field_names=list(temp[0].keys())
                for i in temp:
                    pt.add_row(list(i.values()))
                print(pt)
            cursor=DB.cursor()
            return

        if users.login_user(user_id,password):
            order_food(user_id)
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

user_auth()
