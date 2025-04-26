'''
#tuple can remain duplicate value and touple is normally unchangeable
'''
fruits = ("apple", "banana", "cherry")
print(fruits)
print(fruits[2:1])

#tuple to list
fruits = ("apple", "banana", "cherry")
x = list(fruits)
#x[1] = "Orange"
x.append("mango")
print(x)
fruits = tuple(x)
print(fruits)


#Tuples Joining
fruits = ("apple", "banana", "cherry")
color = ("red", "green", "yellow")
#join_tuple = fruits
join_tuple = fruits + color
print(join_tuple)



