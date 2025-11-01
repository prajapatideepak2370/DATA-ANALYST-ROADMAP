n = int(input("Enter the number: " ))
def pattern1(n):
    for i in range(1, n+1):
         for j in range(1, n+1):
            print("*", end=" ")
         print()
for i in range(n+1,-1):
    for j in range(n-i+1, 0, -1):
        print("*", end=" ")
    print()    

# print(pattern1(n))
'''
  *
 ***
*****
'''
for i in range(1,n+1):
    print(" "*(n-i), end="") #this print satement is used to print space 
    print("*" * (2*i - 1), end= "")
    print("")

'''
*
**
***
'''

for i in range(1,n+1):
    print("*" * i, end= "")
    print("")

'''
* * *
*   *
* * *
'''
for i  in range(1,n+1):
    if(i==1 or i==n):
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")

for i  in range(1,11):
    print(f"{n}X{11-i} = {n*(11-i)}")
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 


for i in range(1,n+1):
    for j in range(n,i+1):
        print(j , end=" ")
    print()
'''

def pattern3(n):
    for i in range(0,n):
        for j in range(n-i-1):
            print(" ", end=" ")
        for j in range(2*i+1):
            print("*", end=" ")
        for j in range(n-i-1):
            print(" ", end=" ")
        print()
def pattern4(n):
    for i in range(0,n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(2*n-(2*i+1)):
            print("*", end=" ")
        for j in range(i):
            print(" ", end=" ")
        print()

pattern3(n)
pattern4(n)
