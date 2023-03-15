n=input()
l=len(n)
for i in range(0,l):
    if i!=0 and i%2!=0:
        k=ord(n[i])
        if k>97:
            k-=32
        print(chr(k),end="")
    