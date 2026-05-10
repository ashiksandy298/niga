A = float(input("Enter first number: "))
B = float(input("Enter second number: "))
sum= A + B
difference = A - B
product = A * B
print("Sum =", sum)
print("Difference =", difference)
print("Product =", product)
if B != 0:
    quotient = A / B
    print("Quotient =", quotient)
else:
    print("Division by zero is not allowed")
