n = input("Enter your Number Row: ")
n = int(n)
h = int(n/2)
x = 1
y = int(h)

for i in range(1,h+1,1):
    print((" " * y )+("*" * x ))
    y -= 1
    x += 2
for j in range(1,h+2,1):
    print((" "* y ) + ("*"* x ))
    y += 1
    x -= 2