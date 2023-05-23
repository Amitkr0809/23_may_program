string=input("enter string : ").split()
rev_word=[]
for i in string:
    rev_word.append(i[::-1])
out=" ".join(rev_word)
print(out)


string=input("enter string : ").split()
N=len(string)
rev_str=[]
for i in range(N):
    rev_str.append(string[N-i-1])
out=" ".join(rev_str)
print(out)