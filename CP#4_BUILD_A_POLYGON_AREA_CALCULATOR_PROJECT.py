class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f"{self.__class__.__name__}(width = {self.width}, height = {self.height})"
    def setWidth(self, update_width):
        self.width = update_width
    def setHeight(self, update_height):
        self.height = update_height
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return 2 * self.width + 2 * self.height
    def getDiagonal(self):
        return (self.width**2 + self.height**2)**.5
    def getPicture(self):
        if self.width > 50 or self.height > 50:
            return "Too large to picture."
        else:
            return '\n'.join(self.width * '*' for unit in range(self.height)) + '\n'
    def getAmountInside(self, another_shape):
        if isinstance(another_shape, Rectangle) or isinstance(another_shape, Square):
            return self.width // another_shape.width * self.height // another_shape.height
        else: None
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(width = side_length, height = side_length)
        self.side_length = side_length
    def __str__(self):
        return f"{self.__class__.__name__}(side = {self.side_length})"
if __name__ == "__main__":
    test_rectangle = Rectangle(3, 4)
    test_square = Square(5)
    print(test_rectangle)
    print(test_rectangle.getPicture())
    print(test_square)
    print(test_square.getPicture())