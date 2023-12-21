from models.base import Base

class Rectangle(Base):
    """Represents a rectangle with width, height, x and y coordinates."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle object with given dimensions and coordinates.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner. Defaults to 0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)  # Call the Base class constructor
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property

    
def
 
width(self):

        
"""Gets the width of the rectangle."""

        
return self.__width

    @width.setter

    
def
 
width(self, value):

        
"""Sets the width of the rectangle, ensuring it's a positive integer."""

        
if
 
not
 
isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be positive")
        self.__width = value

    # ... Similar getters and setters for height, x, and y (implementation omitted for brevity)