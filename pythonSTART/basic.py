name = input("Enter the name : ")
print(f"hello {name}")

letter = '''Dear <|name|>,
\tYou are selected!
Thanks & Regards,
Date <|date|>'''
print (letter.replace("<|name|>","Deepak" ).replace("<|date|>","12/10/2023")) 

print(letter.find("Thanks"))

print(len(letter))
 

 
l1=[5,4,12,1,10,3,9,2]
l1.sort()

l1.reverse()
print(l1)
print(sum(l1))

n = int(input("Enter the number:"))       #  printing table of any number
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")


for i in range(2,n):
    if(n%2!=0):
        print(f"{n} is Odd number")
        break
        
    elif(n%i==0):
        print(f"{n} is prime number")
        break
       
    elif(n%2==0):
        print(f"{n} is even number")


i = 0 
sum = 0
while(i<=n):
    sum += i
    i +=1
print(sum) 

l = ["sohan", "sachin", "deepak", "saurabh"]
for i in l:
    if(i.startswith("s")):
        print("Good morning", i)

