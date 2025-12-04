#pass by value
#int, float, str, tuple, etc. behave like pass by value.
#Immutable (acts like pass by value)
#Changes inside the function don't affect the original variable.
def modify(x):
    x = x + 10
    print("Inside function:", x)

a = 5
modify(a)
print("Outside function:", a)

#pass by reference
#Modifying it inside the function does affect the original list
#list, dict, set, etc. behave like pass by reference.
#Mutable (acts like pass by reference)
def modify(lst):
    lst.append(4)
    print("Inside function:", lst)

my_list = [1, 2, 3]
modify(my_list)
print("Outside function:", my_list)
