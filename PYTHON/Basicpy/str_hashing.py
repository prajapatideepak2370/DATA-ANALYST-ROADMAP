s = "ancysfbzbrwaaagksxvfn"
q = ["a", "g","c","n","x","z","b","s","f","v","w"]

def str_func(s, q):
    hash_list = [0] * 26

    for ch in s:
        ascii_value = ord(ch) - ord('a')
        hash_list[ascii_value] += 1
    for ch in q:
        ascii_value = ord(ch) - ord('a')
        if ascii_value < 0 or ascii_value >= 26:
            print(0, end=" ")
            continue
        print(hash_list[ascii_value], end=" ")
    

#print(str_func(s, q))

#Reverse a vowels of a string
s = "IceCreAm"
def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    s_list = list(s)
    left, right = 0, len(s_list) - 1

    while left < right:
        if s_list[left] not in vowels:
            left += 1
        elif s_list[right] not in vowels:
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

    return ''.join(s_list)
print(reverse_vowels(s))