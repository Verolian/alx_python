'''The module will import some functionalities from another module'''
BaseGeometry = __import__("5-base_geometry").BaseGeometry
'''A class that has inherited from Basegeometry'''
class Rectangle(BaseGeometry):
    '''instantiating the child class functions and also the imported ones'''
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

        '''The function will find the area of the rectangle'''
    def area(self):
         return self.__width*self.__height
        
    def __str__(self):
         return "[Rectangle] {:d}/{:d}".format(self.__width,self.__height)
    
#test example 
# r = Rectangle(3, 5)

# print(r)
# print(r.area())
   