#strig basic
n=input()
print(n)
for i in n:
  print(i,end="")
print()
#present in string or not
if "r" in n:
  print("Yes r present")
else:
  print("NO")
if "k" not in n:
  print("Yes k is not here")
else:
  print("Opps k is here")
  
#string reverse
def reverse(n):
  return n[::-1]
print("Reverse: "+reverse(n))

#Slicing Strings
"""Get the characters from position 2 to position 5"""
k=("Hello, world!")
print(k[2:5])
"""Get the characters from the start to position 5 """
print(k[:5])
"""Get the characters from position 2, and all the way to the end"""
print(k[2:])
"""Get the characters: From: "o" in "World!" (position -5) To, but not included: "d" in "World!" (position -2)"""
print(k[-5:-2])

#Uppercase
print(k.upper())
#lowercase
print(k.lower())
#Strip()-Removes space from the beginning or the end
k=" Hello, World!"
print(k.strip())
#replace() method replaces a string with another string
k="Hello, World!"
print(k.replace("H","J"))
#split() method splits the string into substrings if it finds instances of the separator
print(k.split())
#format() method to insert numbers into strings
age =22
k="My age is {}"
print(k.format(age))

result=3.48
income=0
k="My name is pronoy. My age is {}. My cgpa is {}. My monthly income is {}."
print(k.format(age,result,income))
k="My name is pronoy. My age is {2}. My cgpa is {0}. My monthly income is {1}."
print(k.format(result,income,age))
k="My name is \"Pronoy\""
print(k)
