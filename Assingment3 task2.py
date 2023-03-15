n=input()
i=int(input())
k=n[:i+1][::-1]+n[i+1:]
print(k)