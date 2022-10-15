
def main():

    cadena = input("> ")

    cadena_invertida = invert(cadena)

    print(cadena_invertida)


def invert(cadena: str):
    """
        It inverts a string

        Returns:
        string: an inverted string
    """

    lista_letras = []
    cadena_invertida = ""

    for letra in cadena:
        lista_letras.insert(0, letra)

    cadena_invertida = cadena_invertida.join(lista_letras)

    return cadena_invertida


if __name__ == '__main__':
    main()
