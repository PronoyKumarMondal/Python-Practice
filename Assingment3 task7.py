n=input()
for i in n:
    k=ord(i)
    k+=1
    if(k>122):
        k=(96+(k-122))
    print(chr(k),end="")