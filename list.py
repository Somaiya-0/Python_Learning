'''
fruits = ["apple", "banana", "cherry"]   
fruits = ['apple', 'banana', 'cherry'] 
print(fruits)
print(len(fruits))
'''
'''
#Another way to making List
fruits = ["apple", "banana", "cherry","apple"]  #List e duplicate thakte pare
test = list(('apple', 'banana', 'cherry', 'apple'))
print(test)
print(type(test))
'''
#t(type(test))
'''
fruits = ['apple', "banana", "cherry","apple",4 ,0]
print(fruits[4])
print(fruits[3])
print(fruits[-3])

print(fruits[1:4])  #starting:jeta dekhte chai+1
print(fruits[:4])   #starting from start 
print(fruits[1:])
t(type(test))
'''
'''
#Ekta List e oi value ache ki na
fruits = ['apple', "banana", "cherry","apple",4 ,0]
if "apple" in fruits:
    print("yes")
else:
    print("no")  

if "sunny" in fruits:
    print("yes")
else:
    print("no") 

#Replacement
fruits[4] = "Sunny"
fruits.insert(5,"Sunny")
print(fruits)     


#Without Replacement Entry
fruits.append("orange")
print(fruits)
'''
#List Concatenation
boys = ["Abul", "Rafi"]
girls = ["Jorina", "Sabana"]

girls.insert(1, "Sokina")  #inserting Sokina 
girls.remove("Sabana")    #removing
boys.extend(girls)
boys.pop(2)
girls.clear()   #For doing the list Empty

print(boys)
print(girls)


#SOrting
names = [ 5,1,100,25]
#names.sort(reverse=True)
names.reverse()
print(names)







fruits = ['apple', 'banana', 'cherry','mango',4,0]
test = list(('a','b','c'))
print(len(fruits))
print(type(test))
print(fruits[1:4])
print(fruits[:4])

if 'apple' in fruits:
    print('yes')
else:
    print('no')

fruits[4]='yo'
fruits.insert(5, 'yo')
fruits.append('orange')
print(fruits)

boys = ['abul', 'rafi']
girls= ['jorina', 'Sabana']
girls.insert(1,'sokina')

boys.extend(girls)

print(boys)

yo = ['sunny', 'rafi', 'tonmoy', 'sokina', 'sabana']

yoyo=[]

for x in yo:
    if 's' in x:
        yoyo.append(x)
print(yoyo)

n= [1,5,2,8,4]
n.sort(reverse=True)
print(n)