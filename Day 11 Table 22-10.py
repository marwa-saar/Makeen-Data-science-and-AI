lis = [
    [0,3,0],
    [0,0,1],
    [0,0,1]
    ]
candaGold = lis[0][0]
candaSilver = lis [0][1]
print(lis[0][0])
print(candaGold)
print(candaSilver)

# loop to print all element
for i in lis:
    for j in i :
        print(j)
        
#index nasted loop
for i in range(len(lis)):
    print(lis[i])
    for j in range(len(lis)):
        print(lis[i][j])