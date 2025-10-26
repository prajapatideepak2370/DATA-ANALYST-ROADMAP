num = [1,4,2,7,1,4,9,5,3,7,2,6,3,4]
# n = len(num)
dic = {}
for i in range(0,len(num)):
    if num[i] in dic:
        dic[num[i]] += 1
    else:
        dic[num[i]] = 1
print(dic.get(4))

def storedic(num):
    n = len(num)
    dic = {}
    for i in range(0,n):
        dic[num[i]] = dic.get(num[i], 0) + 1
    return dic
print(storedic(num))

x = [1,2,3,4,5,6,7,8,9]
y = [1,4,2,6,3,6,5,2,9,1,4,9,2]
hash_dict= {}
for num in y:
    hash_dict[num] = hash_dict.get(num, 0) + 1
for num in x:
    if num < 0 or num > 10:
        print(0)
    else:
        print(hash_dict.get(num, 0), end=" ")