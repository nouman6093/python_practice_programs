# Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

print("converting temperature from celsius to fahrenheight: ")
c = int(input("enter temperature in celsius: ").title())
f = (c * 9/5) + 32
print(f"{c} in fahrenheit is: {f}")

print("converting temperature from fahrenheit to celsius: ")
f2 = int(input("enter temperature in fahrenheit: ").title())
c2 = (f2 - 32) * 5/9
print(f"{f2} in celsius is: {c2}")
