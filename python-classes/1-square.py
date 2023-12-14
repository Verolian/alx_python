'''the module will cover all the properties of the class Square inclusive of the attributes . And defines the Square class'''
class Square:
    
    '''the function is initialized and  defined as per the previous module ie 0-square'''
    
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size 


if __name__ == "__main__":
    try:
        my_square_1 = Square(3)
        print(type(my_square_1))  # Output: <class '__main__.Square'>
        print(my_square_1.__dict__)  # Output: {'_Square__size': 3}
    except Exception as e:
        print(e)

    try:
        my_square_2 = Square()
        print(type(my_square_2))  # Output: <class '__main__.Square'>
        print(my_square_2.__dict__)  # Output: {'_Square__size': 0}
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
        my_square_3 = Square("3")  # Output: size must be an integer
        print(type(my_square_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(-89)  # Output: size must be >= 0
        print(type(my_square_4))
        print(my_square_4.__dict__)
    except Exception as e:
        print(e)