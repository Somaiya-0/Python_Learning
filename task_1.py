a=333
b=200
# print("y") if b>a else print("n")
if not a==b:
    print('yo')

day=4 
month=5
match day:
    case 1|2|3|4|5 if month == 4:
        print("A monday in april")
    case 6|7 if month ==5:
        print("a weekend in may")
    
    case _:
        print("no match")



p='Ab@C12*5a'
if '@' in p or '$' in p or '&' in p or '*' in p:
    if '1' in p or '2' in p or '3' in p or '4' in p or '5' in p or '6' in p or '7' in p or '8' in p or '9' in p or '10' in p:
        if p.isalpha():
            print('strong')
else :
    print('weak')