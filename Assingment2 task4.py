sum=0
for i in range(7,601):
    if i%7==0 or i%9==0:
        if i%7!=0 or i%9!=0:
           sum+=i
print(sum)