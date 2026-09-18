character = input("Enter a character: ")

alphabet = "abcdefghijklmnopqrstuvwxyz"
if character in alphabet:
    print(character, "is an alphabet.")
else:
    print(character, "is not an alphabet.")