def Check(number,choice,prime):
    x = []
    for i in range(2, int(number) + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            x.append(i)
    print("\n")
    if choice == 'O':
        Odd(number,prime,x)
    elif choice == 'E':
        Even(number,prime,x)
    elif choice == 'B':
        Both(number,prime,x)

def Odd(number,prime,x):
    if number == 0:
        return 0
    if prime in "Y":
        Odd((number - 1),prime,x)
        if (number % 2) != 0:
            print(number,"prime  number")
    else:
        Odd((number - 1),prime,x)
        if (number % 2) != 0:
            if number in x:
                print(number,"prime number")
            else:
                print(number,"not  prime number")

def Even(number,prime,x):
    if number == 0:
        return 0
    if prime in "Y":
        Even((number - 1),prime,x)
        if (number % 2) != 0:
            print(number,"prime  number")
    else:
        Even((number - 1),prime,x)
        if (number % 2) != 0:
            if number in x:
                print(number,"prime  number")
            else:
                print(number,"not  prime  number")

def Both(number,prime,x):
    if number == 0:
        return 0
    if prime.upper() in "Y":
        Both((number - 1),prime,x)
        if number in x:
            print(number," prime  number")
    else:
        Both((number - 1),prime,x)
        if number in x:
            print(number,"prime  number")
        else:
            print(number,"not  prime  number")


number = input("Enter Max Value : ")
number = int(number)
prime = input("Enter Y/N (OnlyPrime ?) : ")
choice = input("Enter O/E/B (Odd or Even or Both) : ")
Check(number,choice,prime)
