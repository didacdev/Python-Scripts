def getsFibonacci(number: int):
    """
        It prints the fibonacci sequence

        Parameters:
        number (int): the length of the sequence

    """

    number1 = 0
    number2 = 1

    print(number1)
    print(number2)

    for i in range(3, number):
        suma = number1 + number2
        print(suma)
        number1 = number2
        number2 = suma


getsFibonacci(50)
