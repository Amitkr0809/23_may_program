def countCharacterType(string):
    vowels = 0
    consonant = 0
    words = len(string2)
    for i in range(0, len(string)):
        ch = string[i]
        if ( (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') ):
            ch = ch.lower()
            if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
                vowels += 1
            else:
                consonant += 1

    print(words,vowels,consonant)

T=int(input("enter "))
for i in range(T):
    string=input()
    string2 = string.split()
    countCharacterType(string)