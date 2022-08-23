from PIL import Image


def main():
    try:
        image = getImage()
        aspectRatio = calculateAspectRatio(image)
        print(getAspectRatio(aspectRatio))
    except FileNotFoundError:
        print("El archivo introducido no existe")


def getImage():
    """
        It converts the file into an Image object

        Returns:
        Image: the file converted into an Image object
    """
    url = input("Imagen: ")

    image = Image.open(url)

    return image


def calculateAspectRatio(image: Image):
    """
        It calculates the aspect ratio of the image

        Parameters:
        image (Image): an Image object

        Returns:
        float: a floating number that represents the aspect ratio
    """
    exif = image.size
    aspectRatio: float

    if (exif[0] > exif[1]):

        aspectRatio = round((exif[0] / exif[1]), 2)

    else:
        aspectRatio = round((exif[1] / exif[0]), 2)

    return aspectRatio


def getAspectRatio(aspectRatio: float):
    """
        It checks what is the aspect ratio.

        Parameters:
        aspectRatio (float): a floating number that represents the aspect ratio

        Returns:
        string: a string with the aspect ratio
    """

    if (aspectRatio == 1.0):
        return "La relación de aspecto es 1/1"
    elif (aspectRatio == 1.334):
        return "La relación de aspecto es 4/3"
    elif (aspectRatio == 1.78):
        return "La relación de aspecto es 16/9"
    elif (aspectRatio == 1.60):
        return "La relación de aspecto es 16/10"
    elif (aspectRatio == 1.25):
        return "La relación de aspecto es 5/4"
    elif (aspectRatio == 1.5):
        return "La relación de aspecto es 3/2"
    else:
        return "La imagen no tiene una relación de aspecto válida:\n16/9, 4/3, 5/4, 16/10, 1/1"


main()
