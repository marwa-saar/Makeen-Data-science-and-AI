#Dictionary
contacts = {"Marwa":98790066,"Noor":99096754,"Sahab":99875432}
print(contacts)
oldContacts = dict(contacts)

#Accessing Dictionary Values []
sahabNo = contacts["Sahab"]
print("Sahab Number is: ",sahabNo)
#print(contacts[2]) Error cous we don't have key 2

#print all keys and values
for i in contacts:
    print(i,contacts[i])
    
#Checking Membership    
if "Muna" in contacts:
    print(contacts["Muna"])
else:
    print("You don't have Muna in Contacts")

#Get if not print default
munaNo = contacts.get("Muna","0000") #if no Muna in contacts by default print 0000 
print(munaNo)

#Add new Contacts
contacts["Amira"] = 99999990
print(contacts)

#Input 3 friends in contacts
for i in range(3):
    newcoName = input("Enter a Name: ")
    newcoNo = input("Enter a phone Number: ")
    contacts[newcoName] = newcoNo
print(contacts)
#print only values
for i in contacts.values():
    print(i)

#print only keys
for i in contacts.keys():
    print(i)
    
#print all 
for i in contacts.items():
    print(i)
    
#pop remove the last one
ncontacts = contacts.pop("Noor")
print(ncontacts)