x = [1,4,2,6,3,6,5,2,9,1,4,9,2]
y = [1,2,3,4,5,6,7,8,9]
hash_list = [0]*11
for num in x:
    hash_list[num] +=1
for num in y:
    if(num<0 or num>10):
        print(0)
    else:
        print(hash_list[num], end=" ")

