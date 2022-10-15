def main():

    numero = int(input("> "))
    numeroBinario = toBinary(numero)
    print(f"{numero} en binario es {numeroBinario}")


def toBinary(numero: int):
    """
        Convierte un número decimal en binario.

        Return:
        str: cadena con el número en binario
    """
    numeroBinario = ""
    cociente = int(numero / 2)
    resto = numero % 2

    if cociente >= 1:
        numeroBinario += toBinary(cociente)

    numeroBinario += str(resto)
    return numeroBinario


if __name__ == '__main__':
    main()
