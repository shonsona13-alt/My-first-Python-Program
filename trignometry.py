import math

angle = float(input("Enter an angle in degrees: "))

radians = math.radians(angle)

sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

print("Sine:", sin_value)
print("Cosine:", cos_value)
print("Tangent:", tan_value)