"""
greet="good morning"
print("greet".upper())
capital="marwa".upper()
small="ARWA".lower()
print(capital)
print(small)


title="python for everyone"
title=title.replace("for everyone","programm")
print(title)

title2="python for everyone python for everyone "
title2=title2.upper()
title2=title2.replace("for everyone","programm",1)
print(title2)


name="python for for everyone python for everyone"
print(name.find("for",5,20))

"""
"""
floor= input("enter thr floor: ")
floor=int(floor)
if floor==13:
    print("invalid input please enter floor again")

floor=input("enter thr floor: ")
floor=int(floor)

if floor>13:
    actualfloor=floor-1

else:
    actualfloor=floor
print("the actual floor is:" ,actualfloor)
"""


buy=float(input("enter how much you buy:"))
if buy>200:
     buy=buy-buy*0.05
     print(buy)
else:
    print(buy)
     
     
     


