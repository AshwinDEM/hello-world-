import pymysql
conn=pymysql.connect(host='localhost',user='root',password='toor',database='food')
a=conn.cursor()

def intro():
    print("\t\t\t*********************")
    print("\t\t\t WELCOME TO FOOD DASH")
    print("\t\t\t*********************")
    print("Press Enter:")
    input()

def contactUs():
    input("Tell Us Your Problem:")
    print("Thank You for Your Report")
    
def writeAccount():
    Username=input('Enter The Username :')
    Password=input('Enter The Password :')
    a.execute("insert into accounts values('"+str(Username)+"','"+str(Password)+"');")
    conn.commit()
    print("Account Created")
    
def order():
    show_food_table='select * from food_items;'
    a.execute(show_food_table)
    conn.commit()
    data1=a.fetchall()
    print('S.No Item Name Price')
    for i in data1:
        for j in i:
            print(j,end='\t')
        print()

    print("")
    print("")
    
    ab=''
    num=0
    while ab != 2:
        print("1. Select Item") 
        print("2. Pay Bill")
        print("Select your choice")
        ab=input()
 
        if ab=='1':
            Slno=int(input("Enter the S.NO of the item : "))
            Quant=int(input("Enter Quantity : " ))
            if Slno<=16:
                      a.execute("INSERT INTO orders (Sno,Item_Name,Price) SELECT Sno,Item_Name,Price FROM food_items WHERE Sno="+str(Slno)+";")
                      conn.commit()
                      a.execute("UPDATE orders SET Quantity="+str(Quant)+" WHERE Sno="+str(Slno)+";")
                      conn.commit()
                      print("Item Added")
            else:
                print("Item Does Not Exist") 
        elif ab=='2':
            a.execute("select * from orders;")
            conn.commit()
            data21=a.fetchall()
            if data21==():
                print("NO ITEMS SELECTED")
            else:
                print('Sno  Item Name Quantity Price/Item')
                for i in data21:
                    for j in i:
                        print(j,end='\t')
                    print()
                    a.execute("SELECT SUM(Price * quantity) AS Total FROM orders;")
                    conn.commit()
                    data212=a.fetchall()
                print("")
                print('Total Price')
                for i in data212:
                    for j in i:
                        print(j,end='\t')
                    print()

                a.execute("delete from orders;")
                conn.commit()
                break
            
        else:
            print("Invalid Choice")
        print("")
        ab = input("Press Enter:")    
            
def showMenu():
    show_food_table='select * from food_items;'
    a.execute(show_food_table)
    conn.commit()
    data1=a.fetchall()
    print('S.No Item Name Price')
    for i in data1:
        for j in i:
            print(j,end='\t')
        print()

def allShow():
    show_accounts_table='select * from accounts;'
    a.execute(show_accounts_table)
    data2=a.fetchall()
    if data2==():
        print("No accounts available")
    else:
        print('User Name\tPassword')
        for i in data2:
            for j in i:
                print(j,end='\t\t')
            print()
            
def modifyAccount():
    Passworda=input('Enter The Password : ')
    NewPassword=input('Enter The New Password : ')
    a.execute("update accounts set Password='"+str(NewPassword)+"' ""where Password='"+str(Passworda)+"';")
    conn.commit()
    print("New Changes were Saved")

def deleteAccount():
    Passwordaa=input('Enter Your Password : ')
    a.execute("delete from accounts where Password='"+str(Passwordaa)+"';")
    conn.commit()
    print("Account Deleted")
    
# program starts

ch=''
num=0
intro()

while ch != 8:
    print("MAIN MENU")                   
    print("1. CREATE NEW ACCOUNT")           
    print("2. MODIFY ACCOUNT")               
    print("3. SHOW MENU")                    
    print("4. ORDER FOOD")                   
    print("5. ALL ACCOUNT HOLDER LIST")
    print("6. DELETE YOUR ACCOUNT")          
    print("7. CONTACT US")                   
    print("8. EXIT")                         
    print("-->Select Your Option (1-8)<--")
    ch = input()
    if ch == '1':
        writeAccount()            
        
    elif ch =='2':
        modifyAccount()
        
    elif ch == '3':
        showMenu()            
        
    elif ch == '4':
        order()
        
    elif ch == '5':
        allShow()
        
    elif ch == '6':
        deleteAccount()
        
    elif ch == '7':
        num = input("Enter Your Name : ")
        print("Report From ",num)
        contactUs()
        
    elif ch == '8':
        print("Thank You For Using This App")
        break
    else :
        print("Invalid Choice")
        print("Select Between [1,8] Only")
    
    ch = input("Press Enter:")
