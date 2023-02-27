"""
Write the Python code of a program that finds the number of hours, 
minutes, and seconds in a given number of seconds. The number of seconds 
is taken as input from the user.
"""

s=int(input())
h=(s//(60*60))
s=(s%(60*60))
m=(s//60)
s=(s%60)
print("Hours: "+str(h)+" Minutes: "+str(m)+" Seconds: "+str(s))


