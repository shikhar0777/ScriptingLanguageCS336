def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter your choicer: "))
if c==1:
    print("Addition:", add(a, b))
elif c==2:
print("Subtraction:", subtract(a, b))
elif c==3:
print("Multiplication:", multiply(a, b))


