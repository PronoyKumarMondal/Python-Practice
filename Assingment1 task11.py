s=int(input())
l=0
if s<100:
    l=(3000-(125*s**2))
else:
    l=(12000/(4+((s**2)/14900)))

print(l)
