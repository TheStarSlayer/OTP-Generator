import random

list1 = [x for x in range(0,10)]

while True:
   
    a = random.choice(list1)
    list1.remove(a)
    b = random.choice(list1)
    list1.remove(b)
    c = random.choice(list1)
    list1.remove(c)
    d = random.choice(list1)
    list1.remove(d)
    e = random.choice(list1)
    list1.remove(e)
    f = random.choice(list1)


    print("Your OTP is:")
    print(a,b,c,d,e,f, sep="")

    x = input("Generate another OTP? (Press y if yes)\n")
    
    if x == 'y':
        list1.append(a)
        list1.append(b)
        list1.append(c)
        list1.append(d)
        list1.append(e)
        pass

    else:
        exit()