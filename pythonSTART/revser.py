from math import *

x = int(input("Enter the number: "))
reversed_x = 0
while x > 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x = x // 10
print("Reversed number is:", reversed_x)
sign = -1 if x<0 else 1
# num = n
# while num>0:
#     lastdigit = num % 10
#     print(lastdigit, end=" ")
#     num = num // 10

'''
 Reverse the digits of a number and print them in reverse order


'''
'''
Count the digits of a number and print 
count =0
while num>0:
    count +=1
    num = num//10
   
print(count)  

        or

def count(num):
    return int(log10(num)+1)

print(count(n))
'''