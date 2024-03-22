'''importing the module from models.rectangle which has various properties and methods'''
from models.rectangle import Rectangle
'''the class Square which has inherited from the Rectangle class'''
class Square(Rectangle):
    '''Initializes a Square instance.'''
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        '''
        Initializes a Square instance.'''

        
        
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        Returns a string representation of the Square instance.

        Returns:
        - str: A string representing the Square object in the format [Square] (<id>) <x>/<y> - <size> - in our case, width or height
        '''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    
    
    @property
    def size(self):
        return self.__width
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    # @property
    # def size(self):
    #     return self.width

    # @size.setter
    # def size(self, value):
        
    #     if not isinstance(value, int):
    #         raise TypeError("width must be an integer")
    #     elif value <= 0:
    #         raise ValueError("width must be > 0")
    #     self.width = value
    #     self.height = value
   
    
#EXAMPLES
# if __name__ == "__main__":

#     s1 = Square(5)
#     print(s1)
#     print(s1.area())
#     s1.display()

#     print("---")

#     s2 = Square(2, 2)
#     print(s2)
#     print(s2.area())
#     s2.display()

#     print("---")

#     s3 = Square(3, 1, 3)
#     print(s3)
#     print(s3.area())
#     s3.display()