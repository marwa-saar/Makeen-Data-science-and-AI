pin1=1234
balance=int(100)
total=int
withdrawal_amount=0
new_balance=int
c=int
attempts=3

while attempts > 0:
    pin=int(input("Enter your PIN:"))
    if pin == pin1:
        print("Welcome!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect PIN .Tray again.")
        else:
            print("Account locked. Try again later.")
while pin1==pin:    
 type=int(input("Display a menu:\n 1.Check Balance\n 2.Deposit Money\n 3.Withdraw Money\n 4. Exit\n"))
 if type>5 and type==1:
  print(type)
 if type==1:
     print("Your balane is:",balance,"OMR")
 elif type==2:
     amount=int(input("Enter deposit amount"))
     total=amount+balance
     print("Deposit successful! New balance is",total,"OMR")
 elif type==4:
   print("Thank you for using our ATM!") 
   break
 elif int(withdrawal_amount) <= int(balance):
    withdrawal_amount=int(input("Enter withdrawal_amount:"))
    withdrawal_amount=0+withdrawal_amount
    new_balance=balance-withdrawal_amount
    print("Now your balance is:",new_balance)
    if int(withdrawal_amount) > int(balance):
        print("Insufficient balance.")
        
    