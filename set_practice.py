"""Set items are unchangeable, but you can remove items and add new items.
and do not allow duplicate values."""
s={"apple", "banana", "cherry"}
print(s)
#length of a set
print(len(s))
#Duplicate values will be ignored
s = {"apple", "banana", "cherry", "apple"}
print(s)
#Loop through the set, and print the values
for i in s:
    print(i)
if "banana" in s:
    print("YES")
#Add Items
s = {"apple", "banana", "cherry"}
s.add("orange")
print(s)
#To add items from another set into the current set, use the update() method.
s = {"apple", "banana", "cherry"}
s1={"pineapple", "mango", "papaya"}
s.update(s1)
print(s)
"""The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)."""
#To remove an item in a set, use the remove(), or the discard() method.
s = {"apple", "banana", "cherry"}
s.remove("banana")
print(s)
"""Note: If the item to remove does not exist, remove() will raise an error."""
s = {"apple", "banana", "cherry"}
s.discard("banana")
print(s)
"""Note: If the item to remove does not exist, discard() will NOT raise an error."""
#Remove a random item by using the pop() method
s = {"apple", "banana", "cherry"}
s.pop()
print(s)
"""Sets are unordered, so when using the pop() method, you do not know which item that gets removed."""
#The clear() method empties the set
s = {"apple", "banana", "cherry"}
s.clear()
print(s)
#The del keyword will delete the set completely
s = {"apple", "banana", "cherry"}
del s
#Loop through the set, and print the values
s = {"apple", "banana", "cherry"}
for i in s:
    print(i)
#You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Keep ONLY the Duplicates
"""The intersection_update() method will keep only the items that are present in both sets."""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
"""The intersection() method will return a new set, that only contains the items that are present in both sets."""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

