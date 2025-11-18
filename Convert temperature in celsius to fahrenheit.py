# Q: Which formula is used for Celsius → Fahrenheit conversion?
c = float(input('Enter the Temperature in Celsius : '))
f = (c * (9/5)) + 32

# Q: Why do we convert numbers to string before concatenation?
print(str(c) + ' degree Celsius is equal to ' + str(f) + ' degree Fahrenheit')
