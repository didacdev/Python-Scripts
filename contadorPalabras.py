import re


def main():
    frase = input("> ")
    print("Las palabras de la frase y su número de apariciones son:")
    palabras = contador(frase)

    for palabra in palabras:
        print(f"{palabra}: {palabras[palabra]}")


def contador(cadena: str):
    """
        Devuelve un contador con las palabras que forman la frase y el número
        de veces que aparce cada palabra.

        Return:
        dict: diccionario con el recuento de palabras
    """

    palabras = re.findall(r'\w+', cadena.lower())
    contador = {}

    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return contador


if __name__ == '__main__':
    main()
