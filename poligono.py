import abc


def main():
    """Main function"""
    area(Triangle(10.0, 5.0))
    area(Square(6.0))
    area(Rectangle(10.0, 3.4))


def area(poligon):
    """
        It calculates and prints the area of a given polygon.

        Parameters:
        poligon (Polygon): the polygon of which you want to know it area
    """

    poligon.printArea()


class Polygon(abc.ABC):
    """An interface to describe polygons"""

    def area(self):
        pass

    def printArea(self):
        pass


class Triangle(Polygon):

    """ This class provides a triangle"""

    def __init__(self, base, height):
        """ Constructor"""

        self.base = base
        self.height = height

    def area(self):
        """
            It calculates the area of the triangle

            Parameters:
            self

            Returns: 
            double: the area of the triangle

        """

        area = self.base * self.height / 2
        return area

    def printArea(self):
        """
            It prints the area of the triangle

            Parameters:
            self
        """

        print(f"El area del triángulo es {self.area()}")


class Square(Polygon):
    """ This class provides a square"""

    def __init__(self, side):
        """ Constructor"""

        self.side = side

    def area(self):
        """
            It calculates the area of the square.

            Parameters:
            self

            Returns:
            double: the area of the square
        """

        area = self.side ** 2
        return area

    def printArea(self):
        """
            It prints the area of the square.

            Parameters:
            self
        """

        print(f"El area del cuadrado es {self.area()}")


class Rectangle(Polygon):
    """ This class provides a rectangle"""

    def __init__(self, base, height):
        """Constructor"""

        self.base = base
        self.height = height

    def area(self):
        """
            It calculates the area of the rectangle.

            Parameters:
            self

            Returns:
            double: the area of the rectangle
        """

        area = self.base * self.height
        return area

    def printArea(self):
        """
            It prints the area of the rectangle.

            Parameters:
            self
        """

        print(f"El area del rectangulo es {self.area()}")


main()
