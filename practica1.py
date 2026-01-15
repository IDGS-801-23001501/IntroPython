
# Multiply a by b using additions

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
i = 0
result = 0

while i < b:
    i += 1
    result += a

print(result)