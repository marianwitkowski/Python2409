
# Python klasa abstrakcyjna
from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def no_sides(self):
        pass


class Triangle(Polygon):
    def no_sides(self):
        return 3

triangle = Triangle()
print(triangle.no_sides())