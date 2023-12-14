'''The  module Square class has a private attribute __size and an area() method'''
class Square:

    '''I will initialize the method here and also make it impossible to access it form outside . If accessed, there will be a TypeError'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    '''The area() method calculates and returns the area of the square. '''
    def area(self):
        return self.__size ** 2


if __name__ == "__main__":
    try:
        my_square_1 = Square(3)
        print("Area:", my_square_1.area())  
    except Exception as e:
        print(e)

    try:
        print(my_square_1.size)  # Output: 'Square' object has no attribute 'size'
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)  # Output: 'Square' object has no attribute '__size'
    except Exception as e:
        print(e)

    try:
        my_square_2 = Square(5)
        print("Area:", my_square_2.area())  # Output: Area: 25
    except Exception as e:
        print(e)
        