import csv
from prettytable import PrettyTable
 
bill=[]
cou=0
while cou!=12:
    pt=PrettyTable()
    pt.field_names=['Code','Course']
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
    pt.align="l"
    print(pt)
    cou=int(input('''enter the numeric code for the course you want to order
(enter 11 to get your bill):'''))
    if cou==1:
        sp=PrettyTable()
        f1=open('Soup.csv',"r")
        spr=csv.reader(f1,delimiter=",")
        for ok in spr:
            if ok[0]=="Item Code":
                sp.field_names=ok
            else:
                sp.add_row(ok)
        sp.align='l'
        print(sp)
        odr=(input("enter product code(enter back to return to menu):")).upper()
        f1.seek(0,0)
        for ko in spr:
            if ko[0]==odr:
                qua=int(input('''enter quantity of product
(enter negative quantity to remove the item ordered):'''))
                var=0
                for i in bill:
                    if odr==i[0]:
                        var=1
                        i[3]=i[3]+qua
                        if i[3]<0:
                            i[3]=0
                        else:
                            i[4]=int(i[2])*int(i[3])
                        break
                if var!=1 and qua>0:
                    temp=ko+[qua]+[int(ko[2])*qua]
                    bill.append(temp)
                    break
            elif odr.lower()=='back':
                break
        f1.close()
    if cou==2:
        sp=PrettyTable()
        f1=open('SIndian.csv',"r")
        spr=csv.reader(f1,delimiter=",")
        for ok in spr:
            if ok[0]=="Item Code":
                sp.field_names=ok
            else:
                sp.add_row(ok)
        sp.align='l'
        print(sp)
        odr=(input("enter product code(enter back to return to menu):")).upper()
        f1.seek(0,0)
        for ko in spr:
            if ko[0]==odr:
                qua=int(input('''enter quantity of product
(enter negative quantity to remove the item ordered):'''))
                var=0
                for i in bill:
                    if odr==i[0]:
                        var=1
                        i[3]=i[3]+qua
                        if i[3]<0:
                            i[3]=0
                        else:
                            i[4]=int(i[2])*int(i[3])
                        break
                if var!=1 and qua>0:
                    temp=ko+[qua]+[int(ko[2])*qua]
                    bill.append(temp)
                    break
            elif odr.lower()=='back':
                break
        f1.close()
    if cou==3:
        sp=PrettyTable()
        f1=open('SChina.csv',"r")
        spr=csv.reader(f1,delimiter=",")
        for ok in spr:
            if ok[0]=="Item Code":
                sp.field_names=ok
            else:
                sp.add_row(ok)
        sp.align='l'
        print(sp)
        odr=(input("enter product code(enter back to return to menu):")).upper()
        f1.seek(0,0)
        for ko in spr:
            if ko[0]==odr:
                qua=int(input('''enter quantity of product
(enter negative quantity to remove the item ordered):'''))
                var=0
                for i in bill:
                    if odr==i[0]:
                        var=1
                        i[3]=i[3]+qua
                        if i[3]<0:
                            i[3]=0
                        else:
                            i[4]=int(i[2])*int(i[3])
                        break
                if var!=1 and qua>0:
                    temp=ko+[qua]+[int(ko[2])*qua]
                    bill.append(temp)
                    break
            elif odr.lower()=='back':
                break
        f1.close()
    if cou==4:
        sp=PrettyTable()
        f1=open('SCon.csv',"r")
        spr=csv.reader(f1,delimiter=",")
        for ok in spr:
            if ok[0]=="Item Code":
                sp.field_names=ok
            else:
                sp.add_row(ok)
        sp.align='l'
        print(sp)
        odr=(input("enter product code(enter back to return to menu):")).upper()
        f1.seek(0,0)
        for ko in spr:
            if ko[0]==odr:
                qua=int(input('''enter quantity of product
(enter negative quantity to remove the item ordered):'''))
                var=0    
                for i in bill:
                    if odr==i[0]:
                        var=1
                        i[3]=i[3]+qua
                        if i[3]<0:
                            i[3]=0
                        else:
                            i[4]=int(i[2])*int(i[3])
                        break
                if var!=1 and qua>0:
                    temp=ko+[qua]+[int(ko[2])*qua]
                    bill.append(temp)
                    break
            elif odr.lower()=='back':
                break
        f1.close()
    if cou==5:
        sp=PrettyTable()
        f1=open('Mind.csv',"r")
        spr=csv.reader(f1,delimiter=",")
        for ok in spr:
            if ok[0]=="Item Code":
                sp.field_names=ok
            else:
                sp.add_row(ok)
        sp.align='l'
        print(sp)
        odr=(input("enter product code(enter back to return to menu):")).upper()
        f1.seek(0,0)
        for ko in spr:
            if ko[0]==odr:
                qua=int(input('''enter quantity of product
(enter negative quantity to remove the item ordered):'''))
                var=0
                for i in bill:
                    if odr==i[0]:
                        var=1
                        i[3]=i[3]+qua
                        if i[3]<0:
                            i[3]=0
                        else:
                            i[4]=int(i[2])*int(i[3])
                        break
                if var!=1 and qua>0:
                    temp=ko+[qua]+[int(ko[2])*qua]
                    bill.append(temp)
                    break
            elif odr.lower()=='back':
                break
        f1.close()
    if cou==6:
        sp=PrettyTable()
        f1=open('mchi.csv',"r")
        spr=csv.reader(f1,delimiter=",")
        for ok in spr:
            if ok[0]=="Item Code":
                sp.field_names=ok
            else:
                sp.add_row(ok)
        sp.align='l'
        print(sp)
        odr=(input("enter product code(enter back to return to menu):")).upper()
        f1.seek(0,0)
        for ko in spr:
            if ko[0]==odr:
                qua=int(input('''enter quantity of product
(enter negative quantity to remove the item ordered):'''))
                var=0
                for i in bill:
                    if odr==i[0]:
                        var=1
                        i[3]=i[3]+qua
                        if i[3]<0:
                            i[3]=0
                        else:
                            i[4]=int(i[2])*int(i[3])
                        break
                if var!=1 and qua>0:
                    temp=ko+[qua]+[int(ko[2])*qua]
                    bill.append(temp)
                    break
            elif odr.lower()=='back':
                break
        f1.close()
    if cou==7:
        sp=PrettyTable()
        f1=open('mcon.csv',"r")
        spr=csv.reader(f1,delimiter=",")
        for ok in spr:
            if ok[0]=="Item Code":
                sp.field_names=ok
            else:
                sp.add_row(ok)
        sp.align='l'
        print(sp)
        odr=(input("enter product code(enter back to return to menu):")).upper()
        f1.seek(0,0)
        for ko in spr:
            if ko[0]==odr:
                qua=int(input('''enter quantity of product
(enter negative quantity to remove the item ordered):'''))
                var=0
                for i in bill:
                    if odr==i[0]:
                        var=1
                        i[3]=i[3]+qua
                        if i[3]<0:
                            i[3]=0
                        else:
                            i[4]=int(i[2])*int(i[3])
                        break
                if var!=1 and qua>0:
                    temp=ko+[qua]+[int(ko[2])*qua]
                    bill.append(temp)
                    break
            elif odr.lower()=='back':
                break
        f1.close() 
    if cou==8:
        sp=PrettyTable()
        f1=open('mcon.csv',"r")
        spr=csv.reader(f1,delimiter=",")
        for ok in spr:
            if ok[0]=="Item Code":
                sp.field_names=ok
            else:
                sp.add_row(ok)
        sp.align='l'
        print(sp)
        odr=(input("enter product code(enter back to return to menu):")).upper()
        f1.seek(0,0)
        for ko in spr:
            if ko[0]==odr:
                qua=int(input('''enter quantity of product
(enter negative quantity to remove the item ordered):'''))
                var=0
                for i in bill:
                    if odr==i[0]:
                        var=1
                        i[3]=i[3]+qua
                        if i[3]<0:
                            i[3]=0
                        else:
                            i[4]=int(i[2])*int(i[3])
                        break
                if var!=1 and qua>0:
                    temp=ko+[qua]+[int(ko[2])*qua]
                    bill.append(temp)
                    break
            elif odr.lower()=='back':
                break
        f1.close()
    if cou==9:
        sp=PrettyTable()
        f1=open('des.csv',"r")
        spr=csv.reader(f1,delimiter=",")
        for ok in spr:
            if ok[0]=="Item Code":
                sp.field_names=ok
            else:
                sp.add_row(ok)
        sp.align='l'
        print(sp)
        odr=(input("enter product code(enter back to return to menu):")).upper()
        f1.seek(0,0)
        for ko in spr:
            if ko[0]==odr:
                qua=int(input('''enter quantity of product
(enter negative quantity to remove the item ordered):'''))
                var=0
                for i in bill:
                    if odr==i[0]:
                        var=1
                        i[3]=i[3]+qua
                        if i[3]<0:
                            i[3]=0
                        else:
                            i[4]=int(i[2])*int(i[3])
                        break
                if var!=1 and qua>0:
                    temp=ko+[qua]+[int(ko[2])*qua]
                    bill.append(temp)
                    break
            elif odr.lower()=='back':
                break
        f1.close()
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
        if bev=='B1':
            sp=PrettyTable()
            f1=open('mocktails.csv',"r")
            spr=csv.reader(f1,delimiter=",")
            for ok in spr:
                if ok[0]=="Item Code":
                    sp.field_names=ok
                else:
                    sp.add_row(ok)
            sp.align='l'
            print(sp)
            odr=(input("enter product code(enter back to return to beverages menu):")).upper()
            f1.seek(0,0)
            for ko in spr:
                if ko[0]==odr:
                    qua=int(input('''enter quantity of product
    (enter negative quantity to remove the item ordered):'''))
                    var=0
                    for i in bill:
                        if odr==i[0]:
                            var=1
                            i[3]=i[3]+qua
                            if i[3]<0:
                                i[3]=0
                            else:
                                i[4]=int(i[2])*int(i[3])
                            break
                    if var!=1 and qua>0:
                        temp=ko+[qua]+[int(ko[2])*qua]
                        bill.append(temp)
                        break
                elif odr.lower()=='back':
                    break
            f1.close()
        if bev=='B2':
            sp=PrettyTable()
            f1=open('juices.csv',"r")
            spr=csv.reader(f1,delimiter=",")
            for ok in spr:
                if ok[0]=="Item Code":
                    sp.field_names=ok
                else:
                    sp.add_row(ok)
            sp.align='l'
            print(sp)
            odr=(input("enter product code(enter back to return to beverages menu):")).upper()
            f1.seek(0,0)
            for ko in spr:
                if ko[0]==odr:
                    qua=int(input('''enter quantity of product
    (enter negative quantity to remove the item ordered):'''))
                    var=0
                    for i in bill:
                        if odr==i[0]:
                            var=1
                            i[3]=i[3]+qua
                            if i[3]<0:
                                i[3]=0
                            else:
                                i[4]=int(i[2])*int(i[3])
                            break
                    if var!=1 and qua>0:
                        temp=ko+[qua]+[int(ko[2])*qua]
                        bill.append(temp)
                        break
                elif odr.lower()=='back':
                    break
            f1.close()
        if bev=='B3':
            sp=PrettyTable()
            f1=open('Milkshake.csv',"r")
            spr=csv.reader(f1,delimiter=",")
            for ok in spr:
                if ok[0]=="Item Code":
                    sp.field_names=ok
                else:
                    sp.add_row(ok)
            sp.align='l'
            print(sp)
            odr=(input("enter product code(enter back to return to beverages menu):")).upper()
            f1.seek(0,0)
            for ko in spr:
                if ko[0]==odr:
                    qua=int(input('''enter quantity of product
    (enter negative quantity to remove the item ordered):'''))
                    var=0
                    for i in bill:
                        if odr==i[0]:
                            var=1
                            i[3]=i[3]+qua
                            if i[3]<0:
                                i[3]=0
                            else:
                                i[4]=int(i[2])*int(i[3])
                            break
                    if var!=1 and qua>0:
                        temp=ko+[qua]+[int(ko[2])*qua]
                        bill.append(temp)
                        break
                elif odr.lower()=='back':
                    break
            f1.close()
        if bev=='B4':
            sp=PrettyTable()
            f1=open('Hot.csv',"r")
            spr=csv.reader(f1,delimiter=",")
            for ok in spr:
                if ok[0]=="Item Code":
                    sp.field_names=ok
                else:
                    sp.add_row(ok)
            sp.align='l'
            print(sp)
            odr=(input("enter product code(enter back to return to beverages menu):")).upper()
            f1.seek(0,0)
            for ko in spr:
                if ko[0]==odr:
                    qua=int(input('''enter quantity of product
    (enter negative quantity to remove the item ordered):'''))
                    var=0
                    for i in bill:
                        if odr==i[0]:
                            var=1
                            i[3]=i[3]+qua
                            if i[3]<0:
                                i[3]=0
                            else:
                                i[4]=int(i[2])*int(i[3])
                            break
                    if var!=1 and qua>0:
                        temp=ko+[qua]+[int(ko[2])*qua]
                        bill.append(temp)
                        break
                elif odr.lower()=='back':
                    break
            f1.close()
    if cou==11:
        print(bill)
        if len(bill)==0:
            print("No items Ordered")
        else:
            bil=PrettyTable()
            bil.field_names=['Item Code','Item Name','Rate','Quantity','Amount']
            ttl=0
            for i in range(0,len(bill)):
                bil.add_row(bill[i])
                ttl=ttl+int(bill[i][4])
            bil.add_row(["","","","Total:",ttl])
            print(bil)
            edi="yes"
            while edi=="yes":
                rev=input("enter product code to edit(from cart):").upper()
                for i in bill:
                    if rev==i[0]:
                        qua=int(input('''enter quantity of product
(enter negative quantity to remove the item ordered):'''))
                        i[3]=i[3]+qua
                        if i[3]<=0:
                            i[3]=0
                            i[4]=0
                        else:
                            i[4]=int(i[2])*int(i[3])
                        ttl=0
                        new=PrettyTable()
                        new.field_names=['Item Code','Item Name','Rate','Quantity','Amount']
                        for i in range(0,len(bill)):
                            new.add_row(bill[i])
                            ttl=ttl+int(bill[i][4])
                        new.add_row(["","","","Total:",ttl])
                        print(new)
                        edi=input("do wish to continue editing(yes or no):").lower()
                        break
    if cou==12:
        if len(bill)==0:
            print("No items ordered")
            print("Do visit again")
            print("End of Program")
        else:
            for i in bill:
                if i[3]==0:
                    bill.remove(i)
            ttl=0
            billl=PrettyTable()
            billl.field_names=['Item Code','Item Name','Rate','Quantity','Amount']
            for i in range(0,len(bill)):
                billl.add_row(bill[i])
                ttl=ttl+int(bill[i][4])
            billl.add_row(["","","","Total:",ttl])
            print(billl)
            print("Do visit again")
            print("End of Program")
