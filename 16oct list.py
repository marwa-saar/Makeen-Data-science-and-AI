#function 16oct
"""
def main():
    result=cubvolume(2)
    return result
def cubvolume(sidelength):
 return sidelength*sidelength*sidelength
print(main())
"""
"""
def main():
    sidelength=2
    result=cubvolume()
    return result# if i write return sidelength output=2
def cubvolume():
    sidelength=6
    return sidelength*sidelength*sidelength
print(main())
"""
"""
balance = 10000    # A global variable
def withdraw(amount) :
    # This function intends to access the 
    # global ‘balance’ variable and deduct the amount
    global balance 
    if balance >= amount :
        balance = balance - amount

withdraw(350)
print('balance after withdraw = ', balance)

def deposit(amount):
    global balance
    balance += amount # balance = balance + amount
def check():
    global balance
    return balance
deposit(500)
withdraw(200)
print(check())
print('balance after deposit and withdraw = ', balance)
"""
"""
#lists
cotactnumber=["345677889"]
numbers=[1,2,3,4,5]
col="white"
color=["red","green","black","yellow",col] #we can add variable col
print(len(color))
print(len(numbers))#add len 
print(len(cotactnumber))
"""
"""
name="Ali"
traineename=["Azam","Noor","Marwa","Noof",name]
for i in range(5):
    print(i,traineename[i])#when add i we get position and name

"""
"""
name="Ali"
traineename=["Azam","Noor","Marwa","Noof",name,"nada"]
n=len(traineename)
for i in range(n):# n mean lengh can be less or more can be change
    print(i,traineename[i])#when add i we get position and name
"""
"""
#to find max number in list
num=[2,4,-2,20,4]
max=num[0]
for i in num:
    if i > max:
     max = i
print(max)
"""
"""
num=[2,4,-2,20,4]
max=num[0]
for i in num:
    if i < max:#find minimum number in list
     max = i
print(max)
"""
"""
#to know which number is odd or even in list
numbers=[3,2,5,6]
for i in range(len(numbers)):
    if numbers[i]%2==0:
        print(numbers[i],"the number of is even")
    else:
        print(numbers[i],"the number is odd")

"""
"""
#allow user to enter and make list
numbers=[]
newno=0
while True:
    newno=input("you must enter anumber or q to stop:")
    if newno== "q":
        break
    numbers.append((newno))
print("the list of numbers is",numbers)
"""
"""
number=input("you must enter anumber:")
print(number)
flag=number.isdigit()
print(flag)
"""
"""
newlist=["ali",2,"noor"]
newlist.insert(2,"4")
print(newlist)
"""
"""
# no result because sami not in the list
name=["omar","noof","marwa"]
if "sami" in name:
    n=name.index("sami")
    print(n)
"""
"""
#if i write sami in the list output =3 position of sami
name=["omar","noof","marwa","sami"]
if "sami" in name:
    n=name.index("sami")
    print(n)
"""
"""
name=["omar","noof","marwa","sami"]
if "sami" in name:
    n=name.index("sami")# we can use remove instade of index
    print(n)
name.pop(2)#delete marwa which in position 2
print(name)
"""
"""
oldfrinds=["omar","noof","marwa","sami"]
newfrds=["mari","ali"]
allfrds=oldfrinds+newfrds
print(allfrds)
"""
"""
lis=[1,2,3]
newlis=lis*100
print(newlis)
"""

"""
lis=[1,2,3]
print(max(lis))#can use max ,sum,min
"""








































    
    
    
    























