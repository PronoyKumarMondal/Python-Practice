maxi=0
mini=0
sum=0
n=int(input())
a=int(input())
maxi=a
mini=a
sum=a
for i in range(1,n):
    a=int(input())
    if a>maxi:
        maxi=a
    if a<mini:
        mini=a
    sum+=a
print("Maximum "+str(maxi))
print("Minimum "+str(mini))
print("Average is "+str(sum/n))