#Set (can't use index access)
#creating set
numberSet ={22,3,-1,5}
print(numberSet)

#creating empty set
emptySet = {} #This creating dictionary
print(type(emptySet))

emptySet = set() #This creating set
print(type(emptySet))

#set of mixed datatypes
my_set = {1.0,"Hello",(1,2,3)}
print(my_set)

#convert a list to set using set function
set_with_lists = set ([1,2,3])
print(type(set_with_lists))
print(set_with_lists)

# Set Operations
A = {1,2,3,4}
B = {2,4,6,8, 6, 6}
print("A= ",A)
print("B= ",B)
s1 = A | B   # elements in a or b or both
print("Union: A | B =",s1)
s2 = A & B   # elements in both a and b (common factor)
print("Intersection: A & B =",s2)
s3 = A - B   # elements in a but not in b
print("Difference: A - B =",s3)
s4 = A ^ B   # elements in a or b but not both (not common factor)
print("Symmetric Diff: A ^ B =",s4)

#adding elements to set
my_set1 = set ()
my_set1.update([9,12])
my_set1.update("Maryam")
my_set1.update(("India","China"))
print(my_set1)

#Set Comprehensions

L = [1,3,2,6,4]
ll = [x*10 for x in L]
print(ll)

ss = {x*10 for x in L}
print(ss)

L.extend([1,2])
print(L)

ss = {x*10 for x in L}
print(ss)
##

a = {1,2,3}
b = {x*2 for x in a|{4,5}}
print(b)
print(type(b))
