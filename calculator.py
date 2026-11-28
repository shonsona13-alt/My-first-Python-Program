def add(p,q):
    print("Number 1:", p)
    print("Number 2:", q)
    addition = p + q
    return addition
def subtract(p,q):
    print("Number 1:", p)
    print("Number 2:", q)
    subtraction = p - q
    return subtraction
def multiply(p,q):
    print("Number 1:",p)
    print("Number 2:",q)
    multiplication = p * q
    return multiplication
def divide(p,q):
    print("Number 1:",p)
    print("Number 2:",q)
    division = p/q
    return division

print("Choose which operation you want to perform:")
print("a) add")
print("b) subtract")
print("c) multiply")
print("d) divide")

operation = input("Enter your choice (a/b/c/d): ")

p = int(input("Enter the first number: "))
q = int(input("Enter the second number: "))

if operation == "a":
    a1 = add(p,q)
    print("Addition:", a1)
elif operation == "b":
    s1 = subtract(p,q)
    print("Subtraction:", s1)
elif operation == "c":
    m1 = multiply(p,q)
    print("Multiplication:",m1)
elif operation == "d":
    d1 = divide(p,q)
    print("Division:",d1)
else:
    print("That option is not available.")