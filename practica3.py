x = int(input("Dame un numero para imprimir su tabla de multiplicar: "))

for i in range(10):
    print(f"{x} x {i + 1} = {x * (i + 1)}")