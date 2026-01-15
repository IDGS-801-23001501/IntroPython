mi_lista = [1, 2, 3, 4, 5]
print(type(mi_lista))
print(mi_lista[:])
print(mi_lista[2])
print(mi_lista[-1])
print(mi_lista[0:3])
print(mi_lista[3:])

lista1 = ["Dario", 33, 9.5, True, "German", 20.8]
lista1.append("Vargas")

lista1.insert(2, "Nadia")
print(lista1)

lista1.extend(["uno", 1.1, False])
print(lista1)

lista1.remove(33)
print(lista1)
lista1.pop()
print(lista1)

lista2 = ["tres", "cuatro"]
lista3 = lista1 + lista2
print(lista3)

print(lista2 * 4)
lista4 = [2, 1, 5, 4, 3]
print(lista4)
print(lista4.sort())

del lista4[0]
print(lista4)