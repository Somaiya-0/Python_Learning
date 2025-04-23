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