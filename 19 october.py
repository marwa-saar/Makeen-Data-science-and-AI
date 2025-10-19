#19 october
"""
values=[1,16,9,4]
values.sort()
print(values)
"""
"""
values=[1,16,9,4]
values.sort(reverse=True)
print(values)
"""
"""
age=20
age2=age#result=20 as value of age2
age=30
print(age2)
"""
"""
lis=[1,2,3,4]
newlis=lis
lis.append(5)
print(newlis)
"""
"""
lis=[1,2,3,4]
newlis=list(lis)#we make  new list not same lis befor
lis.append(5)
newlis.append(6)
print(newlis)
"""
"""
lis=[1,2,3,4,5,6,]
newlis=lis[2:]
#newlis=lis[2:4] from 2 to 4 but 4 not included
print(newlis)
"""
"""
lis=[]
while True:
     inputstr=input("enter an element or q to exit/stop:")
     if inputstr.isdigit():
          lis.append(int(inputstr))
     elif inputstr[0]=='-' and inputstr[1:].isdigit():
          lis.append(int(inputstr[1:])*-1)
     elif inputstr=="q":
       break
     else:
        lis.append(inputstr)
print(lis)
"""
"""
positve=[]
negative=[]
while True:
    inputInteger=input("enter integer")
    if inputInteger=="q":
        break
    else:
        inputInteger=int(inputInteger)
    if inputInteger >=0:
        positve.append(inputInteger)
    else:
     negative.append(inputInteger)
print("posive numbers:",positve)
print("negative numbers:",negative)
"""
"""
#another soulution 

positve=[]
negative=[]
while True:
    inputInteger=input("enter integer")
    if inputInteger=="q":
        break
    
    if   inputInteger.isdigit():
          
        inputInteger =int(inputInteger)
        positve.append(inputInteger)
    elif inputInteger[0]=='-':
        inputInteger=int(inputInteger[1:])*-1
        negative.append(inputInteger)
print("posive numbers:",positve)
print("negative numbers:",negative)
"""


numbers=[]
while True:
    inputInteger=input("enter integer or done to stop/exit:")
    if inputInteger=="done":
        break
    elif inputInteger.isdigit():
        numbers.append(int(inputInteger))
    
    elif inputInteger[0]=='-':
        inputInteger=int(inputInteger[1:])*-1
        numbers.append(inputInteger)
     
print (sum(numbers))
        
    


             
    
         





                         

    
    
    
    
    
    
    
    
    
    
    












