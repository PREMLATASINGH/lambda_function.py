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
number=[1,2,3,4,5,6,7,8,9,10]
map_object=map(lambda x:x**2,number)
squared_numbers=list(map_object)    
print(squared_numbers)
subtract=lambda a,b:a-b
print(subtract(10,5))
leap_year=lambda year:(year%4==0 and year%100!=0) or (year%400==0)
print(leap_year(2020))
print(leap_year(2021))
palidrome=lambda s:s==s[::-1]
print(palidrome("madam"))
print(palidrome("hello"))
fabionacci=lambda n: n if n<=1 else fabionacci(n-1)+fabionacci(n-2)
print(fabionacci(10))
print(fabionacci(15))
amstrong=lambda num: sum(int(digit)**3 for digit in str(num))==num
print(amstrong(153))