from ast import Break
import datetime

#ลิส
Pizzadough_list = ["Soft Crust Pizza","Crust Pizza"]   
Topping_list = ["Seafood","Tom Yum Kung","Hawaiian","Double Cheese","Spicy Seafood","Cheese & Bacon","Classic Mushroom"]
Addtopping_list = ["Mozzarella Cheese","Bacon Bits","Mushrooms","Prawn","Seafood","Red & Green Chilli","Tomato"]
Drink_list = ["Mineral Water","Beer","Cola","Soda","Orange juice","Watermelon"]

Amount = []
Order = []

#เมนูหลัก
def mainmenu():
    print("\n[เมนูหลัก]")
    print("1.เลือกแป้ง")
    print("2.เลือกหน้า")
    print("3.ท็อปปิ้งเพิ่มเติม")
    print("4.น้ำ")
    print("0.ออกจากโปรแกรม")


#แป้ง   
def Pizzadough() :
    while True :
        print("\n[กรุณาเลือกแป้ง]")
        print("1.",Pizzadough_list[0])
        print("2.",Pizzadough_list[1])
        print("9.กลับหน้าเดิม")
        print("0.ออกจากโปรแกรม")
        try:
            Dought = int(input("กรุณาเลือก : "))
        except ValueError :
            print("\n--------------------------")
            print("กรุณาใส่ตัวเลข")
            print("--------------------------")
            Pizzadough()
        if Dought == 0 :
            farewell(myname)
            break
        elif Dought == 9 :
            return 9  
        elif Dought == 1 :
            Order.append(Pizzadough_list[0])
            Topping()
        elif Dought == 2 :
            Order.append(Pizzadough_list[1])
            Topping()
        else:
            print("\n----------------------------------------")
            print("ขอโทษค่ะ ไม่มีแป้งที่คุณต้องการเลือก")
            print("----------------------------------------")
            Pizzadough()
            

#ท็อปปิ้ง
def Topping() :
    while True :
        try:
            print("\n[กรุณาเลือกหน้าพิซซ่า]")
            print("1.",Topping_list[0])
            print("2.",Topping_list[1])
            print("3.",Topping_list[2])
            print("4.",Topping_list[3])
            print("5.",Topping_list[4])
            print("6.",Topping_list[5])
            print("7.",Topping_list[6])
            print("9.กลับหน้าเดิม")
            print("0.ออกจากโปรแกรม")
            try :
                Top = int(input("กรุณาเลือก : "))   
            except ValueError :
                print("\n--------------------------")
                print("กรุณาใส่ตัวเลข")
                print("--------------------------")
                Topping()    
            if Top == 0 :
                farewell(myname)
            elif Top == 9 :
                return 9 
            elif Top == 1 :
                Order.append(Topping_list[0])
                Amount.append(250)
                Addtop()
            elif Top == 2 :
                Order.append(Topping_list[1])
                Amount.append(250)
                Addtop()
            elif Top == 3 :
                Order.append(Topping_list[2])
                Amount.append(300)
                Addtop()
            elif Top == 4 :
                Order.append(Topping_list[3])
                Amount.append(350)
                Addtop()
            elif Top == 5 :
                Order.append(Topping_list[4])
                Amount.append(320)
                Addtop()
            elif Top == 6 :
                Order.append(Topping_list[5])
                Amount.append(300)
                Addtop()
            elif Top == 7 :
                Order.append(Topping_list[6])
                Amount.append(310)
                Addtop()
            else:
                print("\n----------------------------------------")
                print("ขอโทษค่ะ ไม่มีหน้าพิซซ่าที่คุณต้องการเลือก")
                print("----------------------------------------")
                Topping()
        except NameError :
            continue
        

#ท็อปปิ้งเพิ่มเติม
def Addtop() :
    while True :
        try:
            print("\n[ท็อปปิ้งเพิ่มเติม]")
            print("1.",Addtopping_list[0])
            print("2.",Addtopping_list[1])
            print("3.",Addtopping_list[2])
            print("4.",Addtopping_list[3])
            print("5.",Addtopping_list[4])
            print("6.",Addtopping_list[5])
            print("7.",Addtopping_list[6])
            print("9.กลับหน้าเดิม")
            print("0.ออกจากโปรแกรม")
            try :
                Atop = int(input("กรุณาเลือก : "))
            except ValueError :
                print("\n--------------------------")
                print("กรุณาใส่ตัวเลข")
                print("--------------------------")
                Addtop()
            if Atop == 0 :
                farewell(myname)
            elif Atop == 9 :
                return 9       
            elif Atop == 1 :
                Order.append(Addtopping_list[0])
                Amount.append(50)
                Drinks()
            elif Atop == 2 :
                Order.append(Addtopping_list[1])
                Amount.append(40)
                Drinks()
            elif Atop == 3 :
                Order.append(Addtopping_list[2])
                Amount.append(40)
                Drinks()
            elif Atop == 4 :
                Order.append(Addtopping_list[3])
                Amount.append(35)
                Drinks()
            elif Atop == 5 :
                Order.append(Addtopping_list[4])
                Amount.append(30)
                Drinks()
            elif Atop == 6 :
                Order.append(Addtopping_list[5])
                Amount.append(30)
                Drinks()
            elif Atop == 7 :
                Order.append(Addtopping_list[6])
                Amount.append(25)
                Drinks()
            else:
                print("\n----------------------------------------")
                print("ขอโทษค่ะ ไม่มีท็อปปิ้งเพิ่มเติมที่คุณต้องการเลือก")
                print("----------------------------------------")
                Addtop()
        except NameError :
            continue
        

#เครื่องดื่ม 
def Drinks() :
    while True :
        try:
            print("\n[กรุณาเลือกเครื่องดื่ม]")
            print("1.",Drink_list[0])
            print("2.",Drink_list[1])
            print("3.",Drink_list[2])
            print("4.",Drink_list[3])
            print("5.",Drink_list[4])
            print("6.",Drink_list[5])
            print("9.กลับหน้าเดิม")
            print("0.ออกจากโปรแกรม")
            try :
                Dink = int(input("กรุณาเลือก : "))
            except ValueError :
                print("\n--------------------------")
                print("กรุณาใส่ตัวเลข")
                print("--------------------------")
                Drinks()
            if Dink == 0 :
                farewell(myname)
            elif Dink == 9 :
                return 9      
            if Dink == 1 :
                Order.append(Drink_list[0])
                Amount.append(10)
            elif Dink == 2 :
                Order.append(Drink_list[1])
                Amount.append(50)
            elif Dink == 3 :
                Order.append(Drink_list[2])
                Amount.append(20)
            elif Dink == 4 :
                Order.append(Drink_list[3])
                Amount.append(30)
            elif Dink == 5 :
                Order.append(Drink_list[4])
                Amount.append(45)
            elif Dink == 6 :
                Order.append(Drink_list[5])
                Amount.append(35)
            else:
                print("\n----------------------------------------")
                print("ขอโทษค่ะ ไม่มีเครื่องดื่มที่คุณต้องการเลือก")
                print("----------------------------------------")
                Drinks()
        except NameError :
            continue
        out()
    
        
#ต้อนรับ
def greet (name) :
    thistime=datetime.datetime.now().hour
    if(thistime<=12) :
        thegreet="ตอนเช้า"
    else :
        thegreet="ตอนบ่าย"
    print (f"สวัสดี{thegreet} คุณ{name}\n")


#บอกลา
def farewell(name) :
    print(f"ขอบคุณที่ใช้บริการคุณ{name}")
    exit()


#ทำงานต่อไหม
def out():
    while True:
        keepwork = str(input(" คุณต้องการสั่งอาหารอีกไหม ใช่/ไม่ :"))
        if keepwork == "ไม่":
            moth() 
        elif keepwork == "ใช่":
            Pizzadough()
        else:
            print("\n-------------------------------")
            print(":  กรุณาพิมพ์ ใช่ หรือ ไม่  :")
            print("-------------------------------")


#คิดเงิน
def moth() :
    print()
    print("เมนูที่คุณเลือก",Order)
    print("ทั้งหมดราคา",sum(Amount),"บาท")
    print()  
    money = int(input("กรุณาใส่จำนวนเงิน :"))
    sum_mon = money-sum(Amount)
    print("เงินทอน =",sum_mon)
    if money < sum(Amount):
        money = int(input("กรุณาใส่จำนวนเงินอีกครั้ง :"))
        sum_mon = money-sum(Amount)
        print("เงินทอน =",sum_mon) 
    farewell(myname)
    exit()


#เริ่มต้นการทำงาน                
myname = input("ชื่อ:")
greet(myname)
while True :
    try:
        mainmenu()
        try :
            work=int(input("เลือกหัวข้อเพื่อทำงาน : "))
        except ValueError:
            print("\n-------------------")
            print("โปรดใส่ตัวเลข !!!")
            print("-------------------")
        if work == 0 :
            farewell(myname)
            break
        elif work==1:
            Pizzadough()
            farewell(myname)
            break
        elif work==2:
            Topping()
            farewell(myname)
            break
        elif work==3:
            Addtop() 
            farewell(myname)
            break
        elif work==4:
            Drinks()
            farewell(myname)
            break
        else:
            print("\n---------------------------------")
            print("ขอโทษค่ะ ไม่มีหัวข้อที่คุณต้องการ")
            print("---------------------------------")
            pass
    except NameError :
        continue
