#linear search
numbers = [2,12,5,3,20,13]
target = int(input("Enter number: "))

position = -1       #without break

for i in range(len(numbers)):
    if target == numbers[i]:
        position = i
        
print("The Target is on position: ",position)