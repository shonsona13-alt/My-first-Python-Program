def add(a,b):
  print(a+b)
  return(a+b)

def sub(a,b):
  print(a-b)
  return(a-b)

def mult(a,b):
  print(a*b)
  return(a*b)

def div(a,b):
  try:
    print(a/b)
    return(a/b)
  except ZeroDivisionError:
    print("No division by zero")

print("---This is a calculator---")

a1 = int(input("Type first number: "))
b1 = int(input("Type second number: "))

print("Which operation do you want to do (1: Add 2: Subtract 3: Multiply 4: divide):")
try:
    operation = int(input("Enter your operation number: "))
except ValueError:
    print("That's not a valid operation number!")

if operation == 1:
  result = add(a1,b1)
elif operation == 2:
  result = sub(a1,b1)
elif operation == 3:
  result = mult(a1,b1)
elif operation == 4:
  result = div(a1,b1)

print("The result is", result)