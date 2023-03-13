t=("apple", "banana", "cherry")
print(t)
#tupple length
print(len(t))
#Print the second item in the tuple
print(t[1])
#Print the last item of the tuple
print(t[-1])
#Return the third, fourth, and fifth item
t=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(t[2:5])
"""The search will start at index 2 (included) and end at index 5 (not included).
    the first index has 0"""
print(t[:4])
print(t[2:])
print(t[-4:-1])
#Check if "apple" is present in the tuple
if "apple" in t:
    print("YES")
"""Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
   But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple."""
#Convert the tuple into a list to be able to change it
x=list(t)
x[1]="kiwi"
t=tuple(x)
print(t)
#Unpacking a Tuple
"""When we create a tuple, we normally assign values to it. This is called "packing" a tuple
    But, in Python, we are also allowed to extract the values back into variables. This is called unpacking"""
t=("apple", "banana", "cherry") 
x,y,z=t 
print(x)
#and all of this is like list

    

