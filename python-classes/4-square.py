'''the module will introduce new concepts ie getter and setter '''
class Square:

    '''definition of the self inclusive of the size which as of the previous assignment is set to private'''
    def __init__(self, size=0):
        self.size = size
    '''the @property will hold the data for the size class'''
    @property 
    def size(self):
        return self.__size

    '''the decorator setter will be used to set values for the self'''
    @size.setter 
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()
    print("--")

    my_square.size = 10
    my_square.my_print()
    print("--")

    my_square.size = 0
    my_square.my_print()
    print("--")


help(Square)    