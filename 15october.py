"""
grade=55
flag=grade>95
print(flag)

if flag:
    print("exellent")
else:
    print("good")
"""
"""

time1=input("Enter time1 in HH:MM format:")

result = text.split()
print(result) # Output: ['Hello,', 'world!']
"""

"""
num=int(input("enter number"))
flag=num>0
print(flag)

if flag>0:
    print("positive")
else:
    print("nigative")
"""
"""
from datetime import datetime

time1=input("Enter time1 in HH:MM format:")
time2=input("Enter time2 in HH:MM format:")

time1= datetime.strptime(time1,"%H:%M").time()
time2= datetime.strptime(time2,"%H:%M").time()
if time1>time2:
    print(time1,"comes after",time2)
elif time1<time2:
     print(time1,"comes befor",time2)
else:  
    print("You entered the  same time")
"""
"""
numb=int(input("number"))
previous=int(numb)

while numb!="":
    numb=int(input("number"))
    if numb==pervious and numb!="":
      print("same previous")
    previous= numb
"""
"""

login_username = input("Enter username: ")
login_password = input("Enter password: ")

username="admin"
password="1234"

if login_username == username and login_password == password  :
    
    print("Access granted")
else:
    print("Access denied")
"""

        
