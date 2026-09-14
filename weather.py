Weather = int(input("Enter the current temperature in Fahrenheit: "))
if Weather < 70:
    print("It's a bit chilly outside. You might want to wear a jacket.")

elif Weather >= 70 and Weather <= 85:
    print("The weather is quite pleasant. Enjoy your day!")
else:
    print("It's quite hot outside. Make sure to stay hydrated and wear light clothing.")