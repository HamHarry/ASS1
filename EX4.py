x = input("Enter Harmonic step: ")
print("------------------------------------------")
x = int(x)

def loop(x):
    if x == 0:
        return 0
    else:
        result = (1/x+loop(x-1))
        print(f"Limit = {x}  result = {result}")
        return result
loop(x)