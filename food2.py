
import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",passwd="toor",database="test11")
mycursor=db.cursor()

def intro():
    print("\t\t\t*********************")
    print("\t\t\t WELCOME TO THE LIBRARY")
    print("\t\t\t*********************")
    print("Press Enter:")
    input()

def writeAccount():
    FstName=input('Enter The First Name :')
    LstName=input('Enter The Last Name :')
    data1=mycursor.fetchall()
    n=1
    for i in data1:
        if i!=n:
            ID=i
    
    mycursor.execute("insert into accounts values('"+str(FstName)+"','"+str(LstName)+"','"+str(ID)+"'");")
    db.commit()
    print("Account Created")

def writeBook():
