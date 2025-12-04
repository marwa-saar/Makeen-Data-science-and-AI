readfile=open("story.txt","r")# open is function
# r is by deafult for reading
# if using 'w'--> it will delete every thing in the file to update
#a to append some text

#new line \n

firstline = readfile.readline()
secondline = readfile.readline()

print(firstline)
print(secondline)


readfile.close() # is method
#it must to close the file

#------------------------------------------------------
""" read all text using while loop """

readfile=open("story.txt","r")

line = readfile.readline()

while line !="":
    print(line)
    line=readfile.readline()
    

readfile.close()

"""read and put all text in new list """

readfile=open("story.txt","r")
l=[]
line = readfile.readline()

while line !="":
    
    line=readfile.readline()
    l.append(line)
print(l)

readfile.close()


#-----------------------
"""read all lines using read """
readfile=open("story.txt","r")

line=readfile.read()
print(line)  

readfile.close()

#---------------------------
"""print the total and average """
readfile=open("numbers.txt","r")
total=0
count=0

line=readfile.readline()

while line !="":
    total=total+int(line)
    line=readfile.readline()
    count=count+1
    #print(count)
    
average=total/count
   
print("the total is: ",total)
print("the average is: ",average)
    
readfile.close()

#------------------------------------
"""Ask the user to enter 5 student names and write them into a file called students.txt."""
"""read all lines using read """
readfile=open("students.txt","w")

lis=[]
for i in range(5):
    sname=input("Enter your name: ")
    lis.append(sname)

readfile.write("students names are %s" %(lis))

readfile.close()

#------------------------------
"""Ask the user to enter 5 student names and write them into a file called students.txt."""
"""read all lines using read """
readfile=open("students.txt","w")

for i in range(5):
    sname=input("Enter your name: ")
    readfile.write("students names are %s \n" %(sname))

readfile.close()

#-----
fullName=("Fatima Said Al-Amri")
x=fullName.split()
print(x)

#-----------------------------

"""2 Answers: """
readfile=open("story.txt","r")

line=readfile.read()
word=line.split()
#print(word)
count=0
for i in word:
    count=count+1
print(count)

readfile.close()


#-------
readfile=open("story.txt","r")

line=readfile.read()
word=line.split()
print(len(word))
print(line)
print(type(line))

readfile.close()

#---------------------------------------------------------------------------------