a = []
n = int(input("Enter List size: "))
for x in range(0, n):
      element = input()
      a.append(element)
temp=a[n-1]
a[n-1]=a[0]
a[0]=temp

print(a)
