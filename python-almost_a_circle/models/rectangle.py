'''Importing the fuction of base from the module models and has an empty __init__ file'''
from models.base import Base
''''creating the class Rectangle which has inherited from Base which has been stored in models.base'''
class Rectangle(Base):
    '''Using the init function to create various private attributes'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''using the super function to access the values of the parent class'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
       
    '''Creating the getters and setters for the various attributes'''
# setter for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

# setter for height
    @property
    def height(self):
        return self.__height


    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
# setter for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

# setter for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Calculate the area of the rectangle using the public method def area(self)

        Returns:
        The area of the rectangle calculated as width * height. the functions from the decorators have been used'''
    
        
        return self.__width * self.__height
    

    def display(self):
        '''Prints the representation of the Rectangle instance with '#' characters to stdout, accounting for x and y positions.
        '''
        for i in range(self.y):
             print()
        for i in range(self.height):
            print(' ' * self.x +  '#' * self.width)


       
        '''Returns a string representation of the Rectangle instance.'''
    def __str__(self):
        

        ''' Returns:
        - str: A string representing the Rectangle object in the format [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    

    def update(self, *args ,**kwargs ):
        '''
        Updates attributes of the Rectangle instance based on arguments provided.

        Args:
        - *args: Variable number of arguments to update attributes sequentially: id, width, height, x, y.
        '''
        attributes = ['id', 'width','height', 'x', 'y']
        for i , arg in enumerate(args[:5]):
            setattr(self ,attributes[i],arg)

        # kwargs
        for key , value in kwargs.items():
            if key in attributes:
             setattr(self , key,value)


# examples4
# if __name__ == "__main__":

    # r1 = Rectangle(4, 6)
    # r1.display()

    # print("---")

    # r1 = Rectangle(2, 2)
    # r1.display()
#examples
# if __name__ == "__main__":

#     r1 = Rectangle(10, 2)
#     print(r1.id)

#     r2 = Rectangle(2, 10)
#     print(r2.id)

#     r3 = Rectangle(10, 2, 0, 0, 12)
#     print(r3.id)
        
# examples1
# if __name__ == "__main__":

#     try:
#         Rectangle(10, "2")
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         r = Rectangle(10, 2)
#         r.width = -10
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

    # try:
        # r = Rectangle(10, 2)
        # r.x = {}
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         Rectangle(10, 2, 3, -1)
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))   

# example2  
# if __name__ == "__main__":

#     r1 = Rectangle(3, 2)
#     print(r1.area())

#     r2 = Rectangle(2, 10)
#     print(r2.area())

#     r3 = Rectangle(8, 7, 0, 0, 12)
#     print(r3.area())

# examples5
# if __name__ == "__main__":

#     r1 = Rectangle(4, 6, 2, 1, 12)
#     print(r1)

#     r2 = Rectangle(5, 5, 1)
#     print(r2)
    
#examples6
# if __name__ == "__main__":

#     r1 = Rectangle(2, 3, 2, 2)
#     r1.display()

#     print("---")

#     r2 = Rectangle(3, 2, 1, 0)
#     r2.display() 
        
# examples7
# if __name__ == "__main__":

#     r1 = Rectangle(10, 10, 10, 10)
#     print(r1)

#     r1.update(89)
#     print(r1)

#     r1.update(89, 2)
#     print(r1)

#     r1.update(89, 2, 3)
#     print(r1)

#     r1.update(89, 2, 3, 4)
#     print(r1)

#     r1.update(89, 2, 3, 4, 5)
#     print(r1)
                    
#examples8
# if __name__ == "__main__":

#     r1 = Rectangle(10, 10, 10, 10)
#     print(r1)

#     r1.update(height=1)
#     print(r1)

#     r1.update(width=1, x=2)
#     print(r1)

#     r1.update(y=1, width=2, x=3, id=89)
#     print(r1)

#     r1.update(x=1, height=2, y=3, width=4)
#     print(r1)
             