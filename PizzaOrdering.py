import webbrowser

def open_gdb_link():
    # เปิดลิงก์ GDB ในเบราว์เซอร์เพื่อรันโค้ด
    webbrowser.open("https://www.gnu.org/software/gdb/")

def show_code():
    # แสดงโค้ดที่ต้องการ
    code = '''
import datetime

# ลิส
Pizzadough_list = ["Soft Crust Pizza", "Crust Pizza"]
Topping_list = ["Seafood", "Tom Yum Kung", "Hawaiian", "Double Cheese", "Spicy Seafood", "Cheese & Bacon", "Classic Mushroom"]
Addtopping_list = ["Mozzarella Cheese", "Bacon Bits", "Mushrooms", "Prawn", "Seafood", "Red & Green Chilli", "Tomato"]
Drink_list = ["Mineral Water", "Beer", "Cola", "Soda", "Orange juice", "Watermelon"]

Amount = []
Order = []

# เมนูหลัก
def mainmenu():
    print("\\n[เมนูหลัก]")
    print("1.เลือกแป้ง")
    print("2.เลือกหน้า")
    print("3.ท็อปปิ้งเพิ่มเติม")
    print("4.น้ำ")
    print("0.ออกจากโปรแกรม")

# แป้ง
def Pizzadough():
    while True:
        print("\\n[กรุณาเลือกแป้ง]")
        print("1.", Pizzadough_list[0])
        print("2.", Pizzadough_list[1])
        print("9.กลับหน้าเดิม")
        print("0.ออกจากโปรแกรม")
        try:
            Dought = int(input("กรุณาเลือก : "))
        except ValueError:
            print("\\n--------------------------")
            print("กรุณาใส่ตัวเลข")
            print("--------------------------")
            Pizzadough()
        if Dought == 0:
            farewell(myname)
            break
        elif Dought == 9:
            return 9
        elif Dought == 1:
            Order.append(Pizzadough_list[0])
            Topping()
        elif Dought == 2:
            Order.append(Pizzadough_list[1])
            Topping()
        else:
            print("\\n----------------------------------------")
            print("ขอโทษค่ะ ไม่มีแป้งที่คุณต้องการเลือก")
            print("----------------------------------------")
            Pizzadough()
    '''
    print("โค้ดโปรแกรม:")
    print(code)

def main():
    print("เลือกตัวเลือกที่คุณต้องการทำ:")
    print("1. กดลิ้งค์ GDB เพื่อรันโค้ด")
    print("2. ดูโค้ดโปรแกรม")
    
    choice = input("กรุณาเลือก (1/2): ")
    
    if choice == "1":
        open_gdb_link()
    elif choice == "2":
        show_code()
    else:
        print("เลือกไม่ถูกต้อง กรุณาลองใหม่.")

if __name__ == "__main__":
    main()
