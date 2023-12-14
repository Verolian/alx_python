'''The module from basegeometry 7 has been imported'''
Rectangle = __import__("7-rectangle").Rectangle
'''The child class "Square" will inherit from BaseGeometry'''

class Square(Rectangle):
    '''initializing size'''
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size",size)
    
    def __str__(self):
         return "[Square] {}/{}".format(self.__size,self.__size)
    '''to find the area of the Square'''
    def area(self):
        return self.__size **2
# s = Square(13)

# print(s)
# print(s.area())