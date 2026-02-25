def add(a,b):
    return a+b  
add(2,3)
print(add(2,3))
def subtract(a,b):
    return a-b,a
subtract(5,2)
print(subtract(5,2))
add=lambda a,b:a+b
print(type(add))
print(add(2,3))
even=lambda num:num%2==0
print(even(4))
addition=lambda a,b,c:a+b+c
print(addition(1,2,3))
odd=lambda num:num%2!=0
print(odd(5))
print(odd(4))