def main():
    opt = 0
    while opt != 5:
        menu()
        opt = int(input("Ingresa una opcion: "))

        if 1 <= opt <= 4:
            a = int(input("Ingresa primer numero: "))
            b = int(input("Ingresa segundo numero: "))
            if opt == 1:
                print(sum(a, b))
            if opt == 2:
                print(resta(a, b))
            if opt == 3:
                print(multiplicacion(a, b))
            if opt == 4:
                print(division(a, b))
        elif opt == 5:
            print(salida())
            return
        else:
            print(opt_invalida())



def menu():
    return """
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Salir
        """
def sum(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def salida():
    return "Se salio exitosamente"

def opt_invalida():
    return "Opcion no valida"


if __name__ == "__main__":
    main()