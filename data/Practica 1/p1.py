import random


def ejercicio1():
    adivina = int(random.random() * 100)

    print(adivina)

    x = int(input("Intento 1.\nIntroduce un numero:"))
    intentos = 1

    while adivina != x and intentos < 10:
        if x < adivina:
            print("El numero buscado es mayor.")
        else:
            print("El numero buscado es menor.")
        intentos += 1
        print("Intento", intentos, end="")
        x = int(input("Introduce un numero:"))

    if(intentos != 10):
        print("Has encontrado el numero!")
    else:
        print("Has agotado el numero de intentos!")


def ejercicio3(n=-1):

    if n == -1:
        n = int(input("Introduce un numero:"))

    criba = [0] * (n+1)
    primos = []

    for i in range(2, n+1):
        if criba[i] == 0:
            primos = primos + [i]
            for i in range(i, n+1, i):
                criba[i] = 1

    print(primos)
    return primos


def fibonacci(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def ejercicio4(nombre_fichero):

    f = open(nombre_fichero, "r")

    n = f.read()

    if n.isdigit():

        n = int(n)

        salida = open("salida.txt", "w")

        salida.write(str(fibonacci(n)))

        salida.close()


def ejercicio5(cad):

    c = 0

    for i in cad:
        if i == '[':
            c += 1
        if i == ']':
            c -= 1

    if c != 0:
        return False
    else:
        return True


print(ejercicio5('[[][]][]'))

#ejercicio4("entrada.txt")
