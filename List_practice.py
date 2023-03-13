a=['a','b','c']
print(a)
print(a[0])#index 
print(a[-1])#last element
print(a[-2])#2nd last element
a=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(a[2:5])#3rd to 5th element
print(a[2:])#after 2nd elemt
print(a[:4])#firth to 4th index
print(a[-4:-1])#last 4 th elemet to 2nd last element 
if "apple" in a:#item exists 
    print("Yes apple exits")
else:
    print("sorry")
a[1]="pinaple"#change item value
print(a)
a[1:3]=["pinaple","watermelon"]
print(a)
#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
a= ["apple", "banana", "cherry"]
a[1:2]=["blackcurrant", "watermelon"]
print(a)
#insert()-inserts an item at the specified index
a= ["apple", "banana", "cherry"]
a.insert(2,"Watermelom")
print(a)
#append() method to append an item
a= ["apple", "banana", "cherry"]
a.append("orange")
print(a)
#To append elements from another list to the current list, use the extend() method
a= ["apple", "banana", "cherry"]
b= ["mango", "pineapple", "papaya"]
a.extend(b)
print(a)
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
a= ["apple", "banana", "cherry"]
b= ("mango", "pineapple", "papaya")
a.extend(b)
#The remove() method removes the specified item
a= ["apple", "banana", "cherry"]
a.remove("banana")
print(a)
#The pop() method removes the specified index
"""If you do not specify the index, the pop() method removes the last item"""
a= ["apple", "banana", "cherry"]
a.pop(1)
print(a)
#The del keyword also removes the specified index
a= ["apple", "banana", "cherry"]
del a[0]
print(a)
"""The del keyword can also delete the list completely."""
a= ["apple", "banana", "cherry"]
del a
#clear() method empties the list
a= ["apple", "banana", "cherry"]
a.clear()
print(a)
#Loop in list
#Print all items in the list, one by one
a= ["apple", "banana", "cherry"]
for i in a:
    print(i)
#rint all items by referring to their index number
for i in range(len(a)):
    print(a[i])

i=0
while i<len(a):
    print(a[i])
    i+=1

new=[]
for i in a:
    if 'a' in i:
        new.append(i)
print(new)

new=[]
for i in a:
    new.append(i.upper())
print(new)

#sort list
a = ["orange", "mango", "kiwi", "pineapple", "banana"]
b=sorted(a)
print(b)

#sort desending
b=sorted(a,reverse=True)
print(b)
