s=input("enter string : ")
vowel= 0
const=0
vowels=["a","e","i","o","u","A","E","I","O","U"]
for i in s:
    if i in vowels:
        vowel+=1
    else:
        const+=1

print("vowel : ",vowel)
print("const : ", const)