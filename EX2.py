n = input("Enter your Number Row: ")
k = input("Enter your Number Item: ")
n = int(n)
h = int(n / 2)


def star(h,k):
    for l in range(int(k)):
        x = 1
        y = int(h)
        print("")

        for i in range(1, h + 1, 1):
            print((" " * y) + ("*" * x))
            y -= 1
            x += 2
        for j in range(1, h + 2, 1):
            print((" " * y) + ("*" * x))
            y += 1
            x -= 2


star(h,k)