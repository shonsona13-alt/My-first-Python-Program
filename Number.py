num = int(input("Enter a number: "))

sum = 0

digi = num

while digi > 0:
    digit = digi % 10
    sum += digit
    digi //= 10

print("Sum of digits:", sum)