
#q1
name=str(input("Enter your name"))
age=int(input("Enter age"))
print("Hello",name,", you are",age,"years old.")





#q2
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
sum=num1+num2
print("The sum is",sum,".")





#q3
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
compare=num1>num2
print("Is the first number greater?",compare)




#q4
age=int(input("Enter your age:"))
nationality=str(input(" Enter your nationality: "))
if age>=18 and nationality=="omani" :
    print("You are eligible to vote")
else:
    print("you cant vote")



#q5
numb1=int(input("Enter a number:"))
if numb1>0:
    print("The number is positive")
else:
    print("The number is nigative")
        



#q6
num1=int(input("Enter number:"))
if num1 %2==0:
 print("The number is even. ")
else:
 print("The number is odd.")




#q7
user_mark=int(input("Enter your marks"))
if user_mark >=90:
    print("Exellent")
elif user_mark >=70 and user_mark <90:
    print("Good")
elif user_mark >=50 and user_mark <70:
    print("Pass")
else:
    print("Fail")



#q8
user_age=int(input("Enter your age:"))
license=str(input("Do you have a driving license?"))
if user_age>=18 and license=="yes":
    print("You can drive")
elif user_age>=18 and license=="no":
    print("You need a license to drive")
else:
    print("You are too young drive")
        




#q9
n=0

while n<5:
  n=n+1
  print(n)




#q10
num=int(input("Enter number:"))
count=1
while count<=num:
    if count%2==0:
        print(count)
    count=count+1        

 

    
              


