""" El módulo comprueba si un número es primo o no e imprime la lista de los números primos del 1 al 100 """


def isPrime(number: int):
    """
        Comprueba si un número es primo o no

        Parameters:
        number (int): el número a comprobar

        Returns:
        boolean: true si es el número es primo o false si no lo es
    """

    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def main():
    """
        Ejecuta las instrucciones principales del script
    """

    list = []
    n = int(input("Write a number: "))
    prim = isPrime(n)

    if prim:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

    for i in range(1, 100):
        if isPrime(i):
            list.append(i)

    print(list)


main()
