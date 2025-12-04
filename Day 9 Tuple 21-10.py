#can't be change
t1 = (1, 2, 3)
t2 = ("a", "b", "c", "d")
t3 = (200, "A", [4, 5], 3.2)
print(t1)
print(t2)
print(t3[3])
print(t3[3])

lis = t3[2][1] #4.5 print 5 only
print(lis)

myTuple = (200,"A",[2,10,5,[1,4]]) #print 4
print(myTuple[2][3][1])

#reverse
print(myTuple[::-1])

#####
t1 = ("a", "b", "c")
print(t1[::-1])
t2 = ("a", "b", "c")
t3 = t1 + t2
print(t3)
t3 = t3 * 3
print(t3)
for i in t3:
 print(i, end = " ")
print()
#
t4 = ((1, 2, 3), ("a", "b", "c"))
for j in t4:
    for k in j:
     print(k,end = " ")
    print()
    
#####
t = ((10,20,30),(6,7))

for i in range(len(t)):
    for j in range (len(t[i])):
        print(t[i][j])

#####            
t1 = (1, 2, 3, 1, 5, 1)
print(t1.count(1))
print(t1.index(1))
