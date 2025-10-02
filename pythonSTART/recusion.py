
# Head Recursion print 1 to n
def rec1(i,n):
    if i>n:
        return 
    print (i)
    rec1(i+1,n)

#rec1(1,9)

# Tail Recursion print 1 to n
def rec2(i,n):
    if n<i:
        return
    rec2(i,n-1)
    print(n)
  
#rec2(1,7)

#parameterized Recursion using function

def rec3(sum,i,n):
    if i>n:
        print(sum)
        return 
    rec3(sum+i,i+1,n)
#rec3(0,1,5)

#Extended Recursion using function
def rec4(n):
    if n==1:
        return 1
    return n+rec4(n-1)
#print(rec4(5))
# ---------------------------------------------------------------------
n = input("Enter the name:")
def pal(s):
    left = 0
    right = len(s)-1
    
    while left<right:
        if s[left]!= s[right]:
            return False
        left +=1
        right -=1
    return True

print(pal(n))
N=5
result = []
for i in range(1,N+1):
    if N%i==0:
        result.append(i)
        print(result)
count = len(result)
print(count)

# --------------------------------------------------------------------
a = 885
b = 885
result = []
for i in range(1,max(a,b)+1):
    if a%i==0 and b%i==0:
        result.append(i)
        print(result)
fac = len(result)
print(fac)