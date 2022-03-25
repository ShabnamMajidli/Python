#Calculator
try:
    print("1.a+b")
    print("2.a-b")
    print("3.a*b")
    print("4.a:b")
    emel = int(input("Addimi secin: "))
    if emel > 4:
        print("Duzgun daxil edin!")
    else:
        print("ededleri daxil edin: ")
        a = int(input("ilk eded: "))
        b = int(input("ikinci eded: "))
    if emel == 1:
        print(a + b)
    elif emel == 2:
        print(a - b)
    elif emel == 3:
        print(a * b)
    else:
        print(a / b)
except ValueError as Xeta:
    print("Yalniz eded daxil edin!")
    print("Orginal xeta mesaji: ",Xeta)
except ZeroDivisionError as Xeta:
    print("Sifra bolme emeliyyati mumkun deyil")
    print("Orginal xeta mesaji: ",Xeta)

#Password 3
'''
passwrd="shebnem2003"
username = "Shebnem"
m = input("Username: ")
count = 0
if m == username:
    while count < 3:
        password = input("Password: ")
        if password != passwrd:
            count+=1
            print("Try againg")
        else:
            print("Correct password")
            break
'''
#password error
'''
result = False
while not result:
    password = input("Password: ")
    if not (8 <= len(password) <= 13):
        print("Incorrect password")
    else:
        isCorrect = True
        print("Correct password")
        break
'''
#random
'''
import random
print("3 cehdiniz var")
say = 1
while say <=3:
    eded_1 = int(input("0 ile 100 arasinda bir ede daxil edin: "))
    
    eded_2 = random.randint(1, 3)
    
    if eded_1  == eded_2:
        print("Siz dogru tapdiniz. Ededimiz {}-dir".format(eded_2))
    else:
        print("Siz dogru tapmadiz..")
        
        say += 1
    
print("Siz uduzduz.... Reqemimiz {} idi".format(eded_2))
'''
'''
#randommy
import random
print("3 cehdiniz var")
say = 1
while say <=3:
    eded_1 = int(input("0 ile 100 arasinda bir eded daxil edin: "))
    eded_2 = random.randint(1, 3)
    if eded_1 == eded_2:
        print("Tebrik edirik! Ededimiz {}-dir".format(eded_2))
        say += 1
        break
    else:
        print("Dogru deyil!..")

print("Siz tapa bilmediniz.... Ededimiz {} idi".format(eded_2))
'''

# range1
'''
x = range(3, 6)
for n in x:
print(n)
'''
#range2
'''
x = range(3, 20, 2)
for n in x:
print(n)
'''