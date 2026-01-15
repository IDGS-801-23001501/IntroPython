i = 0
lista = []

while i < 20:
    i += 1
    n = int(input(f"Ingrese numero #{i}: "))
    lista.append(n)

lista.sort()

contados = []
pares = []
impares = []

print("\nNÚMEROS PARES REPETIDOS:")
for num in lista:
    ya_contado = False

    for c in contados:
        if num == c:
            ya_contado = True

    if not ya_contado:
        contados.append(num)
        contador = 0

        for x in lista:
            if x == num:
                contador += 1

        if num % 2 == 0:
            pares.append(num)
            print(f"{num} se repite {contador} veces")

contados = []

print("\nNÚMEROS IMPARES REPETIDOS:")
for num in lista:
    ya_contado = False

    for c in contados:
        if num == c:
            ya_contado = True

    if not ya_contado:
        contados.append(num)
        contador = 0

        for x in lista:
            if x == num:
                contador += 1

        if num % 2 != 0:
            impares.append(num)
            print(f"{num} se repite {contador} veces")
