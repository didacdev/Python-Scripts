""" It prints fizz, buzz or fizzbuzz depending on whether a number is multiple of 3, 5 or both. It not, it prints the number """


def main():
    """
        It prints fizz, buzz or fizzbuzz or a number.

    """

    for number in range(1, 100):
        if (number % 3) == 0 and (number % 5) == 0:
            print("fizzbuzz")
        elif (number % 3) == 0:
            print("fizz")
        elif (number % 5) == 0:
            print("buzz")
        else:
            print(number)


main()
