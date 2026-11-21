age = input("Enter your age: ")
if age.isdigit():
    age = int(age)
    if age % 2 == 0:
        print("Your age is even")
    else:
        print("Your age is odd")
else:
    print("Please enter a valid number for age.")